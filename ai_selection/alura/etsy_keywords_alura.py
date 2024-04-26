import pandas as pd
import requests
from ai_selection.mysqldb import db
from ai_selection.mysqldb.db import db_cfg
import datetime
import queue
from multiprocessing.pool import ThreadPool
import copy
q = queue.Queue()

date = datetime.datetime.now().strftime('%F')
headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'origin': 'https://app.alura.io',
    'priority': 'u=1, i',
    'referer': 'https://app.alura.io/',
    'sec-ch-ua': '"Chromium";v="124", "Microsoft Edge";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0',
}





def reuslt_to_mysql(results_data,table,mode):
    pysql = db.MysqlDbUtils(db_cfg['host'], db_cfg['port'], db_cfg['user'], db_cfg['password'], db_cfg['database'])
    pysql.pd_to_table(results_data,table,mode)
    pysql.close()


def get_first_page():
    params = {
        'offset': '0',
        'limit': '10000',
    }
    response = requests.get('https://alura-api-3yk57ena2a-uc.a.run.app/api/keywords/trending', params=params, headers=headers)

    results_list=response.json()['results']
    results_data=pd.DataFrame(results_list)
    results_data['date']=date
    type_dict = {
                 'monthly_search_volumes':'str',
                 'stemmed_array':'str',
                 }

    results_data = results_data.astype(type_dict)

    reuslt_to_mysql(results_data,'etsy_keywords_alura','append')

# get_first_page()

def get_keywords_page(key_words):
    params = {
        'forceUpdate': 'false',
        'tool': 'keyword-finder-new',
    }

    response = requests.get(
        f'https://alura-api-3yk57ena2a-uc.a.run.app/api/keywords/{key_words}/similar',
        params=params,
        headers=headers,
    )
    results_list=response.json()['results']
    results_data=pd.DataFrame(results_list)
    keyword_search=key_words
    results_data['date'] = date
    results_data['keyword_search']=keyword_search

    type_dict = {
        'monthly_search_volumes': 'str',
        'stemmed_array': 'str',
        'related_keywords':'str',
        'etsy_related_keywords':'str',
        'gpt_related_keywords': 'str'

    }

    type_dict_new=type_dict.copy()
    for key in type_dict.keys():
        if key in results_data.columns:
            pass
        else:
            del type_dict_new[key]

    results_data = results_data.astype(type_dict_new)
    reuslt_to_mysql(results_data, 'etsy_keywords_alura_keysear', 'append')

    return len(results_data)

def producer():
    pysql = db.MysqlDbUtils(db_cfg['host'], db_cfg['port'], db_cfg['user'], db_cfg['password'], db_cfg['database'])
    keyword_search=pysql.query(f"select * from etsy_keywords_alura t  where t.keyword  not in (select t2.keyword_search from etsy_keywords_alura_keysear t2 where t.date=t2.date ) and t.date='{date}'")
    keyword_search_list=keyword_search['keyword'].to_list()
    for keyword_search in keyword_search_list:
        q.put(keyword_search)


def consumer():
    try:
        while True:
            keyword_search = q.get()
            num=get_keywords_page(keyword_search)
            print(f'任务完成{keyword_search}关键词一共有{num}个关联的关键词')
    except Exception as e:
        print(e)


producer()
pool = ThreadPool(10)
i=0
for _ in range(3):
    i+=1
    pool.apply_async(consumer)
pool.close()
pool.join()
