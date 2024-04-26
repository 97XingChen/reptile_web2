import time
import pandas as pd
import datetime
import sys
from mysqldb import db
import random
import requests


cookies = {
    '__gads': 'ID=6cf972babc429860:T=1702869357:RT=1702869357:S=ALNI_ManPuniC1mg8rugpxYpdqBDZzjuCw',
    '__gpi': 'UID=00000cb349d5642a:T=1702869357:RT=1702869357:S=ALNI_MYzvHJBGTURLytfEDX9MopTMyvHog',
    '_ga_LWDZ3KY9Q1': 'GS1.1.1703053937.7.0.1703053937.0.0.0',
    'user_mouse': '20231220143217_a0wv96sq1',
    'AliexpressSession': 'o5GmLuKXrPCHRxjD8BfxYJnGOBene3GuLFvvC6gK',
    'email': '',
    'user_id': '82162',
    'level': 'undefined',
    'ad_login_token': 'f3b1ede7ba934220351eec0871e1f6eb',
    'language': 'zh',
    'sidebarStatus': '0',
    '_gid': 'GA1.2.1366079758.1713433396',
    'is_w_tip': '1',
    '_gat_gtag_UA_161819767_1': '1',
    '_ga_49HDCB1VE6': 'GS1.1.1713521907.16.1.1713521909.0.0.0',
    '_ga': 'GA1.1.1748720882.1702292147',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    # 'Cookie': '__gads=ID=6cf972babc429860:T=1702869357:RT=1702869357:S=ALNI_ManPuniC1mg8rugpxYpdqBDZzjuCw; __gpi=UID=00000cb349d5642a:T=1702869357:RT=1702869357:S=ALNI_MYzvHJBGTURLytfEDX9MopTMyvHog; _ga_LWDZ3KY9Q1=GS1.1.1703053937.7.0.1703053937.0.0.0; user_mouse=20231220143217_a0wv96sq1; AliexpressSession=o5GmLuKXrPCHRxjD8BfxYJnGOBene3GuLFvvC6gK; email=; user_id=82162; level=undefined; ad_login_token=f3b1ede7ba934220351eec0871e1f6eb; language=zh; sidebarStatus=0; _gid=GA1.2.1366079758.1713433396; is_w_tip=1; _gat_gtag_UA_161819767_1=1; _ga_49HDCB1VE6=GS1.1.1713521907.16.1.1713521909.0.0.0; _ga=GA1.1.1748720882.1702292147',
    'Origin': 'https://ixspy.com',
    'Referer': 'https://ixspy.com/data',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
    'currpagePath': '/etsy-product/etsy-product-search',
    'page': 'etsy_product_search',
    'prevpagePath': '/',
    'sec-ch-ua': '"Microsoft Edge";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'siteId': '7',
}

json_data = {
    'category_id': [
        1179,
    ],
    'title': '',
    'sales_total_start': '',
    'sales_total_end': '',
    'favorites_total_start': 0,
    'favorites_total_end': 0,
    'reviews_total_start': 20,
    'reviews_total_end': 40,
    'offer_price_start': 18,
    'offer_price_end': 19,
    'page': 1,
    'size': 1000,
    'rate_start': 0,
    'rate_end': 0,
    'orderBy': 'stat_7days-favorites_count',
    'orderType': 'desc',
    'shipFrom': [],
    'best_seller': '',
    'personalization': '',
    'created_time': '',
    'latest_sale_time': '',
    'process_min': 0,
    'process_max': 0,
    'received_min': 0,
    'received_max': 0,
    'cost_start': 0,
    'cost_end': 0,
    'total_price_start': 0,
    'total_price_end': 0,
    'day': [],
    'is_ad': '',
    'materials': '',
    'etsy_pick': '',
    'rare_find': '',
    'first_ad_time_start': '',
    'first_ad_time_end': '',
    'latest_ad_time_start': '',
    'latest_ad_time_end': '',
    'choice': '',
    'store_id': 0,
    'store_name': '',
}


offer_price_start=0##50是个界限+10 ##200是个界限+50 ##500是个界限+200 ##1000到达峰值
while True:
    json_data['offer_price_start'] = offer_price_start
    if offer_price_start<50:
        offer_price_end=offer_price_start+1
    elif 50<=offer_price_start and offer_price_start<200:
        offer_price_end=offer_price_start+10
    elif 200 <= offer_price_start and offer_price_start <500:
        offer_price_end = offer_price_start + 50
    elif 500 <= offer_price_start and offer_price_start < 1000:
        offer_price_end = offer_price_start + 200
    else:
        offer_price_end=10000000

    json_data['offer_price_end'] = offer_price_end
    reviews_total_start = 0  ##1000是个界限
    while True:
        json_data['reviews_total_start'] = reviews_total_start

        if  reviews_total_start == 0:
            reviews_total_end=10
        elif reviews_total_start > 1000:
            reviews_total_end =10000000
        else:
            reviews_total_end=reviews_total_start * 2

        json_data['reviews_total_end']=reviews_total_end
        i = 1
        while True:
            json_data['page'] = i
            task = {"offer_price_start": offer_price_start, "offer_price_end": offer_price_end,"reviews_total_start": reviews_total_start, "reviews_total_end": reviews_total_end, "page": i}
            try:
                print("开始抓取",task)
                response = requests.post('https://ixspy.com/etsy-goods-search', cookies=cookies, headers=headers, json=json_data)
                if response.status_code==200:
                    ixspy_data=pd.DataFrame(response.json()['data']['list'])
                    date = datetime.datetime.now().strftime('%F')
                    normalized_df = pd.json_normalize(ixspy_data['stat_7days'])
                    ixspy_data = ixspy_data.merge(normalized_df, left_index=True, right_index=True)
                    ixspy_data_need = ixspy_data[
                        ['state', 'product_id', 'product_url', 'product_image', 'product_name', 'video', 'category_id',
                         'category_path', 'ships_from', 'keywords', 'store_id', 'store_name', 'homepage', 'ad',
                         'ad_days', 'created_time', 'rare_find', 'best_seller', 'reviews_total', 'favorites_total',
                         'real_carts_total', 'carts_total', 'stat_7days', 'favorites_count', 'sales_count',
                         'reviews_count', 'update_date', 'offer_price', 'max_price', 'min_price', 'est_sales_total',
                         'sales_total']]

                    ixspy_data_need[['keywords','category_path','stat_7days']]=ixspy_data_need[['keywords','category_path','stat_7days']].astype('str')
                    ixspy_data_need.loc[:,'date']=date
                    try:
                        db.c.pd_to_table(ixspy_data_need, "etsy_goods_ixspy", 'append')
                    except:
                        ixspy_data_need.to_csv('example.csv', mode='a', index=False)
                    print("任务成功",f"抓取量:{len(ixspy_data_need)}",task,)
                    if len(ixspy_data_need)==1000:
                        i+=1
                    else:
                        break
                else:
                    print("任务无法抓取代码非200",task)
                time.sleep(random.uniform(3, 5))
            except:
                print("任务代码报错",task)
                break
        reviews_total_start=reviews_total_end
        if reviews_total_start==10000000:
            break
    offer_price_start=offer_price_end


# ixspy_data_need=pd.read_excel('ixspy.xlsx')






