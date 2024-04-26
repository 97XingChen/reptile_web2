import requests

cookies = {
    'email': '',
    '__gads': 'ID=6cf972babc429860:T=1702869357:RT=1702869357:S=ALNI_ManPuniC1mg8rugpxYpdqBDZzjuCw',
    '__gpi': 'UID=00000cb349d5642a:T=1702869357:RT=1702869357:S=ALNI_MYzvHJBGTURLytfEDX9MopTMyvHog',
    'AliexpressSession': 'nF5dJqBrp9iOYPfschDNpiR1tdwWh6Vvpykxcink',
    '_ga_LWDZ3KY9Q1': 'GS1.1.1703053937.7.0.1703053937.0.0.0',
    'user_mouse': '20231220143217_a0wv96sq1',
    'language': 'zh',
    '_gid': 'GA1.2.1433720311.1703053938',
    'favtedProductIds': '',
    'favtedShopIds': '',
    'is_w_tip': '1',
    'login_session': 'oVKrQS57pFl9281wd1uNG31t2MMBpz26VCXhBpJY',
    'ext_url': '',
    'user_id': '82162',
    'level': 'undefined',
    'ad_login_token': 'ff10223d3bd1722642838b06e341cda7',
    '_fbp': 'fb.1.1703054432281.894388540',
    'blackShopList': '',
    'sidebarStatus': '0',
    '_gat_gtag_UA_161819767_1': '1',
    '_ga_49HDCB1VE6': 'GS1.1.1703053938.5.1.1703055211.0.0.0',
    '_ga': 'GA1.1.1748720882.1702292147',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    # 'Cookie': 'email=; __gads=ID=6cf972babc429860:T=1702869357:RT=1702869357:S=ALNI_ManPuniC1mg8rugpxYpdqBDZzjuCw; __gpi=UID=00000cb349d5642a:T=1702869357:RT=1702869357:S=ALNI_MYzvHJBGTURLytfEDX9MopTMyvHog; AliexpressSession=nF5dJqBrp9iOYPfschDNpiR1tdwWh6Vvpykxcink; _ga_LWDZ3KY9Q1=GS1.1.1703053937.7.0.1703053937.0.0.0; user_mouse=20231220143217_a0wv96sq1; language=zh; _gid=GA1.2.1433720311.1703053938; favtedProductIds=; favtedShopIds=; is_w_tip=1; login_session=oVKrQS57pFl9281wd1uNG31t2MMBpz26VCXhBpJY; ext_url=; user_id=82162; level=undefined; ad_login_token=ff10223d3bd1722642838b06e341cda7; _fbp=fb.1.1703054432281.894388540; blackShopList=; sidebarStatus=0; _gat_gtag_UA_161819767_1=1; _ga_49HDCB1VE6=GS1.1.1703053938.5.1.1703055211.0.0.0; _ga=GA1.1.1748720882.1702292147',
    'Origin': 'https://ixspy.com',
    'Referer': 'https://ixspy.com/data',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
    'currpagePath': '/shopify-store/search',
    'page': 'shopify_store_search',
    'prevpagePath': '/upgrade',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'siteId': '7',
}

json_data = {
    'rank_type': 'search',
    'page': 1,
    'size': 2000,
    'orderBy': 'sw_rank',
    'orderType': 'desc',
    'domain': '',
    'category_id': '12552',
    'category_nodes': [],
    'sales_7_count_start': 0,
    'sales_7_count_end': 0,
    'sales_30_count_start': 0,
    'sales_30_count_end': 0,
    'ads_7_count_start': 0,
    'ads_7_count_end': 0,
    'ads_30_count_start': 0,
    'ads_30_count_end': 0,
    'title': '',
    'country_code': '',
    'products_total_start': 0,
    'products_total_end': 0,
    'launch_time': '',
    'dayType': '',
}

response = requests.post('https://ixspy.com/shopify-store-rank', cookies=cookies, headers=headers, json=json_data)


down_jsonl = 'tt_author.jsonl'
print(response.json())
