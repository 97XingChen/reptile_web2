import json
import queue
import requests
import pandas as pd
import asyncio
import aiohttp
from urllib import parse
import re
import tool
import os
from multiprocessing.pool import ThreadPool

def get_domain_by_urllib(u):
    return parse.urlparse(u).netloc

def requests_shopify(url):
    return requests.get(url=url,timeout=4,)



sem=asyncio.Semaphore(5)


async def get(url):
    session =aiohttp.ClientSession()
    response= await session.get(url)
    await session.close()
    return response

def save_picture(picture_path,picture_code):
    with open(picture_path, 'wb') as f:
        f.write(picture_code)

def requests_all_store(store_shopify):
    for store_url in store_shopify:
        Store=get_domain_by_urllib(store_url)
        url=f'https://{Store}/products.json?limit=250&page=1'
        try:
            while True:
                res = requests_shopify(url)
                products = res.json()['products']
                if res.status_code == 200:
                    products_list_dict=[
                        tool.down_jsonlines('shopify.jsonl',{"Store":Store,"title":product['title'],"id":product['id'],"images":[image['src'] for image in  product['images']]})
                        for product in products
                    ]
                print(url, len(products))
                if len(products) == 250:  ##获取下一页的链接
                    page = re.findall('=(.*)', re.findall('=(.*)', url)[0])[0]
                    url = url[0:-len(page)] + str(int(page) + 1)
                else:
                    break
        except Exception as e:
            print(e)
            pass



def down_shopify_picture(save_dir,picture_list):
    try:
        images=picture_list['images']
        for i in range(0,len(images)):
            f= requests_shopify(images[i]).content
            picture_path=os.path.join(save_dir,str(picture_list['id'])+f'_{str(i)}.jpg')
            save_picture(picture_path,f)
            tool.down_jsonlines('down_shopify_title.jsonl',{"image_url":images[i],"save_path":picture_path})
            print(picture_path)
    except Exception as e:
        print(e)


# async def down_shopify_picture(save_dir,picture_list):
#     async with sem:
#         images=picture_list['images']
#         for i in range(0,len(images)):
#             f= await get(images[i])
#             picture_path=os.path.join(save_dir,str(picture_list['id'])+f'_{str(i)}.jpg')
#             save_picture(picture_path,f.content.read())
#             await tool.down_jsonlines('down_shopify_title.jsonl',{"image_url":images[i],"save_path":picture_path})
#             print(picture_path)
#






if __name__ == '__main__':

    load_jsonl='shopify.jsonl'
    picture_dict = tool.land_jsonlines(load_jsonl)
    picture_dict2 = tool.land_jsonlines('down_shopify_title.jsonl')
    picture_id =list(set([int(json.loads(picture)['save_path'].replace('E:\\shopify_picture\\','').split('_')[0]) for picture in picture_dict2 if len(picture)>100]))
    picture_data = pd.DataFrame([json.loads(picture) for picture in picture_dict ])
    picture_data = pd.merge(picture_data,pd.DataFrame({'id':picture_id,"isture":[0 for _ in range(0,len(picture_id))]}),how='left')
    picture_data=picture_data[picture_data['isture']!=0]

    picture_data=picture_data.reset_index(drop=True)
    print(picture_data)
    save_dir='E:\shopify_picture'

    pool = ThreadPool(10)
    for i in range(0,len(picture_data)):
        pool.apply_async(down_shopify_picture, args=(save_dir, {"id":picture_data.loc[i,"id"],"images":picture_data.loc[i,"images"]}))
    pool.close()
    pool.join()






    #
    # tasks=[asyncio.ensure_future(down_shopify_picture(save_dir,picture_dict))  for  picture_dict in  picture_dict_list]
    # loop=asyncio.get_event_loop()
    # loop.run_until_complete(asyncio.wait(tasks))
    # loop.close()
    #




    #
    # store=pd.read_excel('女装网站整理.xlsx')
    # store_shopify=store['网站'][store['系统']=='shopify'].tolist()
    # requests_all_store(store_shopify)












