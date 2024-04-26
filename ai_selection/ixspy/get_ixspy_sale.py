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
    '_ga_49HDCB1VE6': 'GS1.1.1713495405.15.1.1713495413.0.0.0',
    '_ga': 'GA1.1.1748720882.1702292147',
    'is_w_tip': '1',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    # 'Cookie': '__gads=ID=6cf972babc429860:T=1702869357:RT=1702869357:S=ALNI_ManPuniC1mg8rugpxYpdqBDZzjuCw; __gpi=UID=00000cb349d5642a:T=1702869357:RT=1702869357:S=ALNI_MYzvHJBGTURLytfEDX9MopTMyvHog; _ga_LWDZ3KY9Q1=GS1.1.1703053937.7.0.1703053937.0.0.0; user_mouse=20231220143217_a0wv96sq1; AliexpressSession=o5GmLuKXrPCHRxjD8BfxYJnGOBene3GuLFvvC6gK; email=; user_id=82162; level=undefined; ad_login_token=f3b1ede7ba934220351eec0871e1f6eb; language=zh; sidebarStatus=0; _gid=GA1.2.1366079758.1713433396; _ga_49HDCB1VE6=GS1.1.1713495405.15.1.1713495413.0.0.0; _ga=GA1.1.1748720882.1702292147; is_w_tip=1',
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

response = requests.get(
    'https://ixspy.com/etsy-goods-search-chart?ids[]=1518307138&ids[]=1413455244&ids[]=1554919480&ids[]=1684273429&ids[]=1023099765&ids[]=1514410368&ids[]=1678173188&ids[]=1308248418&ids[]=1538520418&ids[]=1678829677&ids[]=1321181024&ids[]=1661820574&ids[]=1324634507&ids[]=1661356121&ids[]=1010384443&ids[]=1532612369&ids[]=1559697371&ids[]=1698298540&ids[]=743753701&ids[]=1682177063',
    cookies=cookies,
    headers=headers,
)
print(response.json())