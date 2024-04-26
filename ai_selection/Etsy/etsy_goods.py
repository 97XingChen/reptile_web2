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




def get_products_message(goods_url,get_proxies=None):
    proxies = {'http': 'http://' + get_proxies, 'https': 'http://' + get_proxies} if get_proxies is not None else None
    headers = Config.headers_goods
    cookies= Config.cookies_goods
    goods_message_dict={}
    try:
        # response = requests.get(f'https://www.etsy.com/listing/{goodsid}', proxies=proxies,headers=headers,timeout=3)
        response = requests.get(f'{goods_url}',headers=headers, proxies=proxies)
        if response.status_code==200:
            soup = response.text
            sold_out = re.findall('wt-circle wt-flex-xs-none wt-p-xs-1 wt-bg-white wt-text-black wt-mr-xs-2(.*?)<span class="etsy-icon',soup, re.S)
            if len(sold_out) > 0:
                print(str(goods_url) + 'this item is sold out')
            else:
                goods_message = re.findall("Etsy.Context.data : {},(.*?)\);\n", soup)
                mes_to_dict = json.loads(goods_message[0])
                goods_message_dict['currency'] = mes_to_dict['locale_settings']['currency']['code']
                goods_message_dict['productid'] = str(mes_to_dict['granify']['product']['id'])
                goods_message_dict['title'] = mes_to_dict['granify']['product']['title']
                goods_message_dict['in_stock'] = int(mes_to_dict['granify']['product']['in_stock'])
                goods_message_dict['regular_price'] = float(mes_to_dict['granify']['product']['regular_price'])
                goods_message_dict['price'] = float(mes_to_dict['granify']['product']['price'])
                goods_message_dict['image'] = mes_to_dict['granify']['product']['image']
                goods_message_dict['shopId'] = mes_to_dict['shopId']
                goods_message_dict['shop_name'] = mes_to_dict['shop_name']


                goods_message2 = re.findall('<script type="application/ld(.*?)</script', str(soup), re.S)
                goods_message2 = [message2.replace('+json">', '') for message2 in goods_message2]
                goods_message3 = re.findall('<script type="text/json" data-neu-spec-placeholder-data="1">(.*?)</script', str(soup),re.S)
                mes_to_dict1 = json.loads(goods_message2[0])
                goods_message_dict['category'] = mes_to_dict1['category']

                # mes_to_dict2 = json.loads(goods_message3)
                print(mes_to_dict1)
                # goods_message_dict['listing_tags'] = str(mes_to_dict2['args']['listing_tags'])


                review_num_html = re.findall('<span class="wt-badge wt-badge--status-02 wt-ml-xs-2">(.*?)</span>', str(soup), re.S)
                if len(review_num_html) > 0:
                    goods_message_dict['review_num'] = int(review_num_html[0].replace('\n', '').replace(' ', '').replace(',', ''))
                else:
                    goods_message_dict['review_num'] = 0

                favorite_html = re.findall('wt-display-flex-xs wt-align-items-baseline wt-flex-direction-row-xs(.*?)Report this item to Etsy',soup, re.S)

                if 'favorite' in favorite_html[0]:
                    favorite_html = re.findall('ref=l2-collection-count">(.*?)favorite', favorite_html[0], re.S)
                    if len(favorite_html) > 0 :
                        goods_message_dict['favorites'] = favorite_html[0].replace('\n', '').replace(',','').strip()

                country_html = re.findall('wt-grid__item-xs-12 wt-text-black wt-text-caption">(.*?)</div>',soup,re.S)
                if len(country_html) > 0:
                    goods_message_dict['country'] = country_html[0].replace('\n', '').replace(',', '').strip()

                if 'bestseller-badge-explanation' in soup:
                    goods_message_dict['product_label'] = goods_message_dict['product_label'] + 'Bestseller,'
                if 'Etsy’s Pick' in soup:
                    goods_message_dict['product_label'] = goods_message_dict['product_label'] + 'Etsy’s Pick,'
                elif 'wt-badge wt-badge--status-03 wt-pl-xs-2' in soup:
                    print(goods_message_dict['product_label'])
                    goods_message_dict['product_label'] = goods_message_dict['product_label'] + 'Bestseller,'

                product_label_html = re.findall('<p class="wt-position-relative wt-text-caption">(.*?)</p>', soup,re.S)

                if len(product_label_html) > 0:
                    product_label_html = [
                        re.findall('</strong>(.*)', product_label, re.S)[0].replace('\n', '').strip() for product_label in product_label_html]
                    goods_message_dict['product_label'] = goods_message_dict['product_label'] + ','.join(product_label_html)

                product_label_html2 = re.findall('<p class="wt-position-relative wt-text-title-01 wt-text-brick">(.*?)</p>', soup,re.S)
                if len(product_label_html2) > 0:
                    product_label_html2 = product_label_html2[0].replace('\n', '').strip()
                    goods_message_dict['product_label'] = goods_message_dict['product_label'] + ','+product_label_html2
                print(goods_message_dict)
        else:
            pass

    except Exception as e:
        print(e)

goodsid_list=[1099387713,1472780756,714811221,1560653315,1602351351,1383499614,1646575089,1146854200,1205562352,1180904310,1145724755,1276868377,1265367098,1287825215,1405027031]


for goodsid in goodsid_list:
    get_products_message(f'https://www.etsy.com/listing/{goodsid}')
    time.sleep(3)
