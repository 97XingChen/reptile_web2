import os

import requests
from bs4 import BeautifulSoup
import tool
import json
from urllib import parse


def get_url(url,headers):
    return BeautifulSoup(requests.get(url, headers=headers).content, "lxml")

def down_land_picture(url,headers):
    return requests.get(url,headers).content

def get_domain_by_urllib(u):
    return parse.urlparse(u).netloc

def get_domain_by_path(u):
    return parse.urlparse(u).path

def get_petallush_goods_html(headers,down_jsonl):

    for i in range(1,24):
        url=f'https://www.petallush.com/new-arrival_p_{i}/'
        soup = get_url(url,headers)
        goods_url_html=soup.find_all('h3',attrs={'class':'product-name'})
        goods_list=[{"href":goods.find('a').get("href"),"target":goods.find('a').get("target"),"title": goods.find('a').get("title")}   for  goods in  goods_url_html ]
        [ tool.down_jsonlines(down_jsonl,good)    for good in  goods_list]

def get_petallush_goods_picture(load_jsonl,down_jsonl,headers):

    goods_dict=tool.land_jsonlines(load_jsonl)
    href_list=[ json.loads(goods)['href']    for goods in goods_dict]
    for href in href_list:

        soup=get_url(href,headers)
        picture_url_html=soup.find('ul',attrs={'class':'lof-navigator'}).find_all('a',attrs={'class':'cloud-zoom-gallery'})
        picture_url=[ picture.get("href")  for picture in   picture_url_html  ]
        tool.down_jsonlines(down_jsonl, {"href":href,"picture_url":picture_url})
        print(href, 'success')

def down_petallush_picture(load_jsonl,headers):
    picture_dict = tool.land_jsonlines(load_jsonl)
    picture_list=[  picture for goods in picture_dict  for picture in  json.loads(goods)['picture_url']]
    for picture in picture_list:
        picture_path=get_domain_by_urllib(picture)+'/'+get_domain_by_path(picture).split('/')[-1]
        os.makedirs(get_domain_by_urllib(picture),exist_ok=True)
        picture_code=down_land_picture(picture,headers)
        with open(picture_path,'wb') as f:
            f.write(picture_code)
        print(picture_path)





if __name__=="__main__":
    goods_down_jsonl = 'goods_html.jsonl'
    picture_down_jsonl = 'picture_url.jsonl'
    headers = {
        'authority': 'www.petallush.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        # 'cookie': 'frontend=9umt9h79lnr0kpfstfpt13ejv3; frontend_cid=6zUE4MROV5qAJzRg; cid=9372369efc4e90fd793fb6e40e4e6feb; first_time=1703059626; last_time=1703059628.066; _ga=GA1.1.2667966.1703059628; _uetsid=c57598109f0e11eea438998ba5bc1cfe; _uetvid=c5759e909f0e11eeaac54dba5ba18e8e; AWSALB=T4CcuMMKY4D6r/mIMP9Xudk+MlSd1ZtMYgNa56sU7CVddrpYENCQEq20ELysAjS+HdkCpJlCQBw7AfKbGHVjL47LE0l4yph48CwlxjojwruKindd1rP/oWgGfOOi; AWSALBCORS=T4CcuMMKY4D6r/mIMP9Xudk+MlSd1ZtMYgNa56sU7CVddrpYENCQEq20ELysAjS+HdkCpJlCQBw7AfKbGHVjL47LE0l4yph48CwlxjojwruKindd1rP/oWgGfOOi; ad_title=; ad_id=; _ga_L8HKV9XTN9=GS1.1.1703059628.1.1.1703059651.37.0.0',
        'referer': 'https://www.petallush.com/',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
    }
    # get_petallush_goods_picture(goods_down_jsonl,picture_down_jsonl,headers)
    down_petallush_picture(picture_down_jsonl,headers)
