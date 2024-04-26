import time

import requests
import re
import json
import pandas as pd
import datetime
from config import  Config
from requests.adapters import HTTPAdapter
from ai_selection.mysqldb import db
from ai_selection.mysqldb.db import db_cfg
import queue
from multiprocessing.pool import ThreadPool

q = queue.Queue()


def use_category_get_goodsid(path,line,get_proxies=None):
    headers=Config.headers
    proxies = {'http': 'http://'+get_proxies,'https': 'http://'+get_proxies} if get_proxies is not None else None
    i=1
    while True:
        params = {
            'explicit': '1',
            'ship_to': 'US',
            'order': 'date_desc',
            'category_landing_page': 'true',
            'ref': 'pagination',
            'page': i,
        }
        pysql = db.MysqlDbUtils(db_cfg['host'], db_cfg['port'], db_cfg['user'], db_cfg['password'], db_cfg['database'])
        try:
            k=0
            while k<=2:
                with requests.Session() as s:
                    s.mount('http://', HTTPAdapter(max_retries=3))
                    s.mount('https://', HTTPAdapter(max_retries=3))
                    response = requests.get(f'https://www.etsy.com/c/{path}', params=params, headers=headers,proxies=proxies,timeout=6)

                if response.status_code==200:
                    soup = response.text
                    date = datetime.datetime.now().strftime('%F')
                    if 'data-shop-id'not in soup:
                        print(f"第{line}线程",path,'page-->',i,'抓取结束')
                        k=3
                        break
                    else:
                        goods_message = re.findall('<ol class="wt-grid wt-grid--block wt-pl-xs-0 tab-reorder-container"(.*?)</ol>',str(soup), re.S)[0]
                        goods_message = goods_message.split("</li><li")
                        goods_list = []
                        for goods in goods_message:
                            try:
                                goods_dict = {}
                                goods_dict['goodsid'] = re.findall('data-palette-listing-id="(.*?)"\n', goods)[0] if len(re.findall('data-palette-listing-id="(.*?)"\n', goods)) > 0 else None
                                goods_dict['shopid'] = re.findall('data-shop-id="(.*?)"\n', goods)[0] if len(re.findall('data-shop-id="(.*?)"\n', goods)) > 0 else None
                                goods_dict['path'] = 'jewelry/bracelets/bangles/kadas'
                                goods_dict['title'] = re.findall('title="(.*?)"', goods, re.S)[0] if len(re.findall('title="(.*?)"', goods, re.S)) > 0 else None
                                goods_dict['picture_url'] = re.findall('src="(.*?)"', goods, re.S)[0] if len(re.findall('src="(.*?)"', goods, re.S)) > 0 else None
                                goods_dict['is_ad'] = re.findall('vertisement</span> (.*?)</span>', goods, re.S)[0] if len(re.findall('vertisement</span> (.*?)</span>', goods, re.S)) > 0 else None
                                goods_dict['shopname'] = re.findall('wt-screen-reader-only">From shop (.*?)</span>', goods)[0] if len(re.findall('wt-screen-reader-only">From shop (.*?)</span>', goods)) > 0 else None
                                goods_dict['date'] = date
                                goods_list.append(goods_dict)
                            except Exception as e:
                                print(e)
                                goods_list=[]
                                k += 1
                                break
                        if len(goods_list)>0:
                            goods_data = pd.DataFrame(goods_list)
                            pysql.pd_to_table(goods_data, 'etsy_goods_url', 'append')
                            print(f"第{line}线程",path, 'page-->', i)
                        pysql.close()
                        k=3
                else:
                    k+=1

        except Exception as e:
            print(f"第{line}线程",path,'page-->',i,e,'False')
            pysql.close()
        i+=1
        time.sleep(0.2)



def producer():
    """
    生产者模型 ## 放入关键词，抓取排序，页面
    :return:
    """
    category_all_data=pd.read_excel(r'Category_all_data.xlsx')
    path_list=list((category_all_data['path']))
    path_data=[   path        for path in path_list    if 'jewelry'==path.split("/")[0]  ]

    sorted_data = sorted(path_data, key=len, reverse=True)
    # 定义一个新的空列表用于存储不具有包含关系的字符串
    filtered_data = []
    for path in sorted_data:
        # 检查该路径是否是其它任何已过滤路径的前缀
        if not any(path in filtered for filtered in filtered_data):
            filtered_data.append(path)
    filtered_data=sorted(filtered_data, key=len)
    for filtered in filtered_data:
        q.put(filtered)


def consumer(i):
    """
    消费者模型 同时该消费者模型比较奇特，获取后续要爬取的链接
    :return:
    """

    global q
    try:
        while True:
            keywords_message = q.get(block=True, timeout=10)
            use_category_get_goodsid(keywords_message,i)
    except Exception as e:
        print(e,'一个线程结束')




producer()
pool = ThreadPool(10)
i=0
for _ in range(3):
    i+=1
    pool.apply_async(consumer, args=(i,))
pool.close()
pool.join()









# use_keyword_get_goodsid('jewelry',2)











# def get_shop_messages(shopname,get_proxies,shop_messages_list):
#     i=0
#     while True:
#
#         shop_dict={
#             'shop_name':'null',
#             'logo':'null',
#             'url': 'null',
#             'goods_total':0,
#             'shop_sales': 0,
#             'Admirers': 0,
#             'reviews': 0,
#             'updated':'null',
#             'since':'null',
#         }
#         proxies = {
#             'http': 'http://'+get_proxies,
#             'https': 'http://'+get_proxies
#         }
#         try:
#             headers = {
#                 # 'authority': 'www.etsy.com',
#                 # 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#                 # 'accept-language': 'zh-CN,zh;q=0.9',
#                 # # Requests sorts cookies= alphabetically
#                 # # 'cookie': 'user_prefs=M8URTHxOWbSbufT77Iu5a7MB1VhjZACC5Nwfp6D0w2il0GAXJZ280pwcHaXUPN3QYCUdJRABFjGCULiIWAYA; fve=1668151521.0; ua=531227642bc86f3b5fd7103a0c0b4fd6; _gcl_au=1.1.2046852476.1668151524; _pin_unauth=dWlkPU16bGpOMll6WlRNdE1UQXlaQzAwWmpnNExXSTFaV0V0TkRaa1lUZzVZamxrTlRKbA; _tt_enable_cookie=1; _ttp=3c3aadcc-1198-4505-a266-c3ccab55dbbd; __pdst=0dd326799c2c418fa2eaa55a09078af8; uaid=BTPaBy0_HjntZuXXDDfMzRYPmY1jZACC5Nwfp8B0Q-eyaqXSxMwUJSulAqMC02xD3zzTdBfzMG-_HOMi99yiSg_j8BRfD6VaBgA.; _gid=GA1.2.1342961002.1669598715; G_ENABLED_IDPS=google; g_state={"i_p":1669713526066,"i_l":2}; search_options={"prev_search_term":"Garnet%20Silver","item_language":null,"language_carousel":null}; pla_spr=1; search_history_v2=NztvdT5VVI7-rRjvp2oruSjqKspjZACC5IbOZWC6bUd9tVJxamJRckZqsZJVdLVSYWlqUaWSlZJ7YlFeaolCcGZOWWqRko5SSWZuanxxSWJugZKVoZmZpbm5sYmxpY5SRmJxfFFqcWlOCVB_SVFpaq0OwpCizLz0YqyaDQ1NTAhoDkjNS0nMK8Gq39DY2MiYgH5Xx6AgTz93LNrNDC0MjEyxaY-tZQAA; __zlcmid=1DClPjw7VStUSIf; last_browse_page=https%3A%2F%2Fwww.etsy.com%2Fshop%2FEfratMakovJewelry; _ga=GA1.1.1511495713.1668151525; _uetsid=83042a406ebb11edbb85af45aec67cc4; _uetvid=026458f0619211ed98f959a03b3b8be6; granify.uuid=e2bdb1fd-0f22-4cb8-a5d1-cd3e8c0feb01; granify.new_user.qivBM=false; _ga_KR3J610VYM=GS1.1.1669780078.17.1.1669781822.41.0.0; granify.session.qivBM=-1',
#                 # 'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
#                 # 'sec-ch-ua-mobile': '?0',
#                 # 'sec-ch-ua-platform': '"Windows"',
#                 # 'sec-fetch-dest': 'document',
#                 # 'sec-fetch-mode': 'navigate',
#                 # 'sec-fetch-site': 'none',
#                 # 'sec-fetch-user': '?1',
#                 # 'upgrade-insecure-requests': '1',
#                 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
#             }
#
#             params = {
#                 'sort_order': 'date_desc',
#                 'page': '1',
#             }
#
#             response = requests.get(f'https://www.etsy.com/shop/{shopname}', params=params,proxies=proxies, headers=headers,timeout=3)
#             if response.status_code==200:
#                 soup = response.text
#                 shop_message = re.findall("Etsy.Context.data : {},(.*?)\);", str(soup))
#                 shop_message2 = re.findall('<script type="application/ld(.*?)</script', str(soup), re.S)
#                 shop_message2 = [message2.replace('+json">', '') for message2 in shop_message2]
#                 shop_to_dict = json.loads(shop_message[0])
#                 shop_dict['Admirers'] = shop_to_dict['trust_signals']['num_favorers']
#                 shop_dict['goods_total'] = shop_to_dict['listings_total_count']
#                 shop_dict['shop_name'] = shopname
#                 updated_html = re.findall('<div class="wt-text-gray wt-text-caption">(.*?)</div>', soup, re.S)
#                 if len(updated_html) > 0:
#                     updated = re.findall('">(.*?)</span>', updated_html[0])
#                     if len(updated) > 0:
#                         timeArray = time.strptime(updated[0], "%b %d, %Y")
#                         shop_dict['updated'] = str(time.strftime("%Y-%m-%d", timeArray))
#                 shop_sales_html = re.findall('<span class="wt-text-caption wt-no-wrap">(.*?)</span>', soup, re.S)
#                 if len(shop_sales_html) > 0:
#                     if 'class' in shop_sales_html[0]:
#                         shop_sales_html = re.findall('class="">(.*?)</a>', shop_sales_html[0])
#                         shop_dict['shop_sales'] = int(
#                             shop_sales_html[0].replace(',', '').replace(' Sale', '').replace('s', ''))
#                     else:
#                         shop_dict['shop_sales'] = int(
#                             shop_sales_html[0].replace(',', '').replace(' Sale', '').replace('s', ''))
#
#                 for message2 in shop_message2:
#                     if '"url":' in str(message2):
#                         shop_to_dict2 = json.loads(message2)
#                         if 'logo' in shop_to_dict2:
#                             shop_dict['logo'] = shop_to_dict2['logo']
#                         if 'aggregateRating' in str(shop_to_dict2):
#                             shop_dict['reviews'] = int(shop_to_dict2['aggregateRating']['reviewCount'])
#                         shop_dict['url'] = shop_to_dict2['url']
#                 shop_since_html = re.findall('On Etsy since(.*?)</span>', soup)
#                 if len(shop_since_html) > 0:
#                     shop_dict['since'] = re.findall('">(.*)', shop_since_html[0])[0]
#                 print(shopname, 'success')
#                 shop_messages_list.append(shop_dict)
#                 break
#             else:
#                 break
#         except Exception as e:
#             i=i+1
#             print(shopname,e,'False')
#             if i>4:
#                 break
#             else:
#                 continue
#
#
# def get_products_message(goodsid,get_proxies,goods_message_list):
#     i=0
#     while True:
#         proxies = {
#             'http': 'http://'+get_proxies,
#             'https': 'http://'+get_proxies
#         }
#         goods_message_dict={
#             'productid':'null',
#             'title': 'null',
#             'image': 'null',
#             'country': 'null',
#             'currency': 'null',
#             'price': 0,
#             'regular_price': 0,
#             'in_stock': 0,
#             'category':'null',
#             # 'goods_description': 'null',
#             'review_num':0,
#             # 'review': 'null',
#             # 'review_publish': 'null',
#             'favorites':'null',
#             'listing_tags': 'null',
#             'product_label':'',
#             'shopId': 'null',
#             'shop_name': 'null',
#         }
#         try:
#             headers = {
#                 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
#             }
#             # response = requests.get(f'https://www.etsy.com/listing/{goodsid}', proxies=proxies,headers=headers,timeout=3)
#             response = requests.get(f'https://www.etsy.com/listing/{goodsid}', headers=headers,timeout=3)
#             if response.status_code==200:
#
#                 soup = response.text
#                 print(soup)
#                 sold_out = re.findall('wt-circle wt-flex-xs-none wt-p-xs-1 wt-bg-white wt-text-black wt-mr-xs-2(.*?)<span class="etsy-icon',soup, re.S)
#                 if len(sold_out) > 0:
#                     print(str(goodsid) + 'this item is sold out')
#                     break
#                 else:
#                     # print(soup)
#
#                     goods_message = re.findall("Etsy.Context.data : {},(.*?)\);\n", soup)
#                     #
#                     mes_to_dict = json.loads(goods_message[0])
#                     goods_message_dict['currency'] = mes_to_dict['locale_settings']['currency']['code']
#                     goods_message_dict['productid'] = str(mes_to_dict['granify']['product']['id'])
#                     goods_message_dict['title'] = mes_to_dict['granify']['product']['title']
#                     goods_message_dict['in_stock'] = int(mes_to_dict['granify']['product']['in_stock'])
#                     goods_message_dict['regular_price'] = float(mes_to_dict['granify']['product']['regular_price'])
#                     goods_message_dict['price'] = float(mes_to_dict['granify']['product']['price'])
#                     goods_message_dict['image'] = mes_to_dict['granify']['product']['image']
#                     # start_timestamp=mes_to_dict['granify']['product']['promotion']['start_timestamp']
#                     # in_cart_count=mes_to_dict['in_cart_count']
#                     goods_message_dict['shopId'] = mes_to_dict['shopId']
#                     goods_message_dict['shop_name'] = mes_to_dict['shop_name']
#
#
#                     goods_message2 = re.findall('<script type="application/ld(.*?)</script', str(soup), re.S)
#                     goods_message2 = [message2.replace('+json">', '') for message2 in goods_message2]
#                     goods_message3 = re.findall('<script type="text/json" data-neu-spec-placeholder-data="1">(.*?)</script', str(soup),re.S)
#                     mes_to_dict1 = json.loads(goods_message2[0])
#                     goods_message_dict['category'] = mes_to_dict1['category']
#
#                     mes_to_dict2 = json.loads(goods_message3[1])
#                     goods_message_dict['listing_tags'] = str(mes_to_dict2['args']['listing_tags'])
#                     # goods_message_dict['goods_description']="'"+mes_to_dict1['description']
#
#                     review_num_html = re.findall('<span class="wt-badge wt-badge--status-02 wt-ml-xs-2">(.*?)</span>', str(soup), re.S)
#                     if len(review_num_html) > 0:
#                         goods_message_dict['review_num'] = int(review_num_html[0].replace('\n', '').replace(' ', '').replace(',', ''))
#                     else:
#                         goods_message_dict['review_num'] = 0
#                     # if 'reviewBody' in str(goods_message2[0].text):
#                     #     if goods_message_dict['review_num']!=0:
#                     #         goods_message_dict['review']=str([review['reviewBody'] for review in mes_to_dict1['review']])
#                     #         goods_message_dict['review_publish']=str([review['datePublished'] for review in mes_to_dict1['review']])
#
#                     favorite_html = re.findall('wt-display-flex-xs wt-align-items-baseline wt-flex-direction-row-xs(.*?)Report this item to Etsy',soup, re.S)
#
#                     if 'favorite' in favorite_html[0]:
#                         favorite_html = re.findall('ref=l2-collection-count">(.*?)favorite', favorite_html[0], re.S)
#                         if len(favorite_html) > 0 :
#                             goods_message_dict['favorites'] = favorite_html[0].replace('\n', '').replace(',','').strip()
#
#                     country_html = re.findall('wt-grid__item-xs-12 wt-text-black wt-text-caption">(.*?)</div>',soup,re.S)
#                     if len(country_html) > 0:
#                         goods_message_dict['country'] = country_html[0].replace('\n', '').replace(',', '').strip()
#
#                     if 'bestseller-badge-explanation' in soup:
#                         goods_message_dict['product_label'] = goods_message_dict['product_label'] + 'Bestseller,'
#                     if 'Etsy’s Pick' in soup:
#                         goods_message_dict['product_label'] = goods_message_dict['product_label'] + 'Etsy’s Pick,'
#                     elif 'wt-badge wt-badge--status-03 wt-pl-xs-2' in soup:
#                         print(goods_message_dict['product_label'])
#                         goods_message_dict['product_label'] = goods_message_dict['product_label'] + 'Bestseller,'
#
#
#
#                     product_label_html = re.findall('<p class="wt-position-relative wt-text-caption">(.*?)</p>', soup,re.S)
#
#                     if len(product_label_html) > 0:
#                         product_label_html = [
#                             re.findall('</strong>(.*)', product_label, re.S)[0].replace('\n', '').strip() for product_label in product_label_html]
#                         goods_message_dict['product_label'] = goods_message_dict['product_label'] + ','.join(product_label_html)
#
#                     product_label_html2 = re.findall('<p class="wt-position-relative wt-text-title-01 wt-text-brick">(.*?)</p>', soup,re.S)
#                     if len(product_label_html2) > 0:
#                         product_label_html2 = product_label_html2[0].replace('\n', '').strip()
#                         print(product_label_html2)
#                         goods_message_dict['product_label'] = goods_message_dict['product_label'] + ','+product_label_html2
#                     goods_message_list.append(goods_message_dict)
#
#                 break
#             else:
#
#                 break
#         except Exception as e:
#             i=i+1
#             print(e)
#             if i>4:
#                 break
#             else:
#                 continue
#     return(goods_message_dict['shopId'],goods_message_dict['shop_name'])
#
# # 商品
# proxies_list='154.195.51.206:2000'
# goods_message_list=[]
# get_products_message('675476599',proxies_list,goods_message_list)
# print(goods_message_list)
#


#关键词
# goodsid_adsid_list=[]
# keyword='rings'
# page=1
# order='date_desc'
# use_keyword_get_goodsid(keyword,page,order,'0',goodsid_adsid_list)
# print(goodsid_adsid_list)