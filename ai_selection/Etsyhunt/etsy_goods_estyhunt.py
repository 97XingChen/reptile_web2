import requests
import queue
q=queue.Queue()
from multiprocessing.pool import ThreadPool
import requests

cookies = {
    'sbox-l': 'cn',
    'sbox-guid': 'MTcxMzE3NzM2OHwzNDV8OTYxODk1MDEx',
    '_uab_collina': '171317737042970566538713',
    '_trackUserId': 'G-1713177425000',
    '_clck': '1ow8zgy%7C2%7Cfky%7C0%7C1566',
    '__stripe_mid': '33c9954a-970b-4a14-b6db-0ae3787b25abd517ac',
    '_csrf': '939cce0ef1c224c18181d0a053af551ce96a21afbf7909f6c2cb856ad79a1647a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22waAws6Hz4cN5yVYq9mGQWTy-bcr-n33h%22%3B%7D',
    'first_visit_path': '%2Fecommerce%2Fcommon%2Fv1_0%2Fnew-user',
    'anonymous_user_id': '8228ab2946e1516ea4eecf430f6db700',
    'is_first_visit': 'false',
    '_gid': 'GA1.2.1066000858.1714111260',
    'g_state': '{"i_l":0}',
    'ZFSESSID': '70tfcb1ls40682sg00pg97g6k4',
    '_identity': '61926c8a5e062338cc69d1bb737178c0a1856f85caff9ab7ac6d07aa7d8ecf20a%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A21%3A%22%5B7846853%2Cnull%2C259200%5D%22%3B%7D',
    'last_login': 'efa616f9f9a24d3fbe46ab449e38cc587411edd5fbbe1ea9ffdd7dfb187dbecea%3A2%3A%7Bi%3A0%3Bs%3A10%3A%22last_login%22%3Bi%3A1%3Bi%3A3%3B%7D',
    'crisp-client%2Fsession%2Fee0c1497-4d30-45d2-ae24-8157e37e83d4': 'session_48073b8f-ec61-4038-a214-59a9344d1429',
    '__stripe_sid': '9697f110-3e01-421e-b27b-e8da2cfcdf6830b821',
    '_ga_M97JW26PVF': 'GS1.1.1714121193.4.1.1714122408.59.0.0',
    '_ga': 'GA1.2.1200815540.1713177371',
    '_gat_gtag_UA_140648082_9': '1',
    'SERVERID': 'b0398419351ae18d9b70be5d5b8153cf|1714122413|1714111240',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsYW4iOiJjbiIsInZlciI6InNtYiIsInRpbWVzdGFtcCI6MTcxNDEyMjQwNywiZXhwaXJlIjoxNzE0MzgxNjA3LCJ1c2VyX2lkIjoiVFY1clExRlJiQT09IiwiYXBwbmFtZSI6IkV0c3lIdW50Iiwic3Vic2NyaXB0aW9uIjp7ImlkIjoiMzA0MjQ2IiwicGxhbl9pZCI6IjI1MSIsInBsYW5fcHJpY2VfaWQiOiIzMDAiLCJ1c2VyX2lkIjoiNzg0Njg1MyIsImNoYW5uZWwiOiIxIiwiY2hhbm5lbF9jdXN0X2lkIjoiY3VzX1B6a0FOeTJaQmNIUmtCIiwiY2hhbm5lbF9zdWJzY3JpcHRpb25fb3Jfb3JkZXJfaWQiOiJzdWJfMVA5a2hmSmMxSWFobTJFOVZZbTY2cWoxIiwiY2hhbm5lbF9zdGF0dXMiOiJ0cmlhbGluZyIsImNoYW5uZWxfbGFzdF9wYXltZW50X2RhdGUiOiIwIiwiY2hhbm5lbF9sYXN0X3BheW1lbnRfYW1vdW50IjoiMCIsImNoYW5uZWxfc3RhcnRfYXQiOiIxNzE0MTIyMjYzIiwiY2hhbm5lbF9jYW5jZWxlZF9hdCI6IjAiLCJjaGFubmVsX2VuZF9hdCI6IjAiLCJwZXJpb2Rfc3RhcnQiOiIxNzE0MTIyMjYzIiwicGVyaW9kX2VuZCI6IjE3MTQzODE0NjMiLCJwZXJpb2RfZGVsYXkiOiIwIiwiaXNfdHJpYWwiOiIxIiwic2NhbGEiOm51bGwsImxhc3Rfc3luYyI6IjAiLCJjcmVhdGVkX2F0IjoiMjAyNC0wNC0yNiAwMjowNDoyNyIsImxhc3RfbW9kaWZpZWQiOiIyMDI0LTA0LTI2IDAyOjA0OjMzIiwiY2FuY2VsZWRfYXQiOiIwMDAwLTAwLTAwIDAwOjAwOjAwIiwiZW5kZWRfYXQiOiIwMDAwLTAwLTAwIDAwOjAwOjAwIiwic3RhdHVzIjoiMSIsImNvdW50cnlfY29kZSI6IjAiLCJwYXlfdHlwZSI6IjAiLCJwcmVfc3Vic2NyaXB0aW9uX2lkIjoiMCIsImNvZGUiOiJldHN5X3BsYW5fM19tb250aF8xOV85OSIsInBsYW5fbmFtZSI6IkV0c3lIdW50IFBybyIsImlzX3JlY3VybHkiOiIxIiwicHJpY2UiOiIxMjkuOTAiLCJkZWZhdWx0X3BsYW4iOiJldHN5X3BsYW5fMF9tb250aF8wIiwicGxhbl90eXBlIjoiUHJvIiwicGxhbl9wcmljZSI6eyJpZCI6IjI2OSIsInBsYW5faWQiOiIyNTEiLCJuYW1lIjoiRVRTWS1Qcm8tMTkuOTlVU0QtTW9udGgiLCJ0aXRsZSI6IiIsImNvZGUiOiJldHN5X3BsYW5fM19tb250aF8xOV85OSIsInByaWNlIjoiMTkuOTkiLCJjdXJyZW5jeV90eXBlIjoiMCIsImludGVydmFsIjoiMiIsImludGVydmFsX2NvdW50IjoiMSIsInN0YXR1cyI6IjEiLCJwYXJlbnRfaWQiOiIwIiwiaXNfcmVjdXJseSI6IjEiLCJ0aGVtZV9pbmZvIjoie1widHJpYWxfZGF5c1wiOlwiM1wiLFwidHJpYWxfYW1vdW50XCI6XCIxXCIsXCJjbnlfdHJpYWxfYW1vdW50XCI6XCI2LjVcIixcImJ0bl9ldmVudF90eXBlXCI6XCIxXCIsXCJjb250ZW50X2xpc3RfY29sb3JcIjpcIiM0MjY3QjJcIixcInByaWNlX3RleHRcIjpcIjE5Ljk5XCIsXCJwcmljZV90ZXh0XzFcIjpcIjE5Ljk5XCIsXCJ0aW1lX3RleHRcIjpcIlxcdTY3MDhcIixcInRpbWVfdGV4dF8xXCI6XCJtb1wiLFwiZGVmYXVsdF9pY29uXCI6XCJlbC1pY29uLXN1Y2Nlc3NcIixcImNvbnRlbnRfbGlzdFwiOlwiXFx1NWUyZFxcdTRmNGRcXHU2NTcwXFx1ZmYxYTFcXHU0ZWJhXFxuXFx1OTAwOVxcdTU0YzFcXHU2NDFjXFx1N2QyMlxcdWZmMWFcXHU0ZTBkXFx1OTY1MFxcblxcdTU1NDZcXHU1NGMxXFxcL1xcdTVlOTdcXHU5NGZhXFx1Njk5Y1xcdTUzNTVcXHVmZjFhXFx1NWM1NVxcdTc5M2EyMDAwXFx1Njc2MVxcblxcdTVlOTdcXHU5NGZhXFx1NjQxY1xcdTdkMjJcXHVmZjFhXFx1NGUwZFxcdTk2NTBcXG5cXHU1MTczXFx1OTUyZVxcdThiY2RcXHU1MjA2XFx1Njc5MFxcdWZmMWEyMDBcXHU2YjIxXFxcL1xcdTY1ZTVcXG5cXHU2NTM2XFx1ODVjZlxcdTUyOWZcXHU4MGZkXFx1ZmYxYTI1MDBcXHU0ZTJhXFxuRXRzeUdQVFxcdWZmMWFcXHU0ZTBkXFx1OTY1MFxcblxcdTUyMjBcXHU5NjY0XFx1ODBjY1xcdTY2NmZcXHVmZjFhMTAwXFx1NWYyMFxcXC9cXHU1NDY4XFxuQUlcXHU2MzYyXFx1ODBjY1xcdTY2NmZcXHVmZjFhMzVcXHU1ZjIwXFxcL1xcdTU0NjhcXG5cXHU1ZTk3XFx1OTRmYVxcdTUyMDZcXHU2NzkwXFx1ZmYxYVxcdTRlMGRcXHU5NjUwXFxuXFx1NjI3OVxcdTkxY2ZcXHU1MTczXFx1OTUyZVxcdThiY2RcXHU1MjA2XFx1Njc5MFxcdWZmMWE1MFxcdTZiMjFcXFwvXFx1NjVlNVxcblxcdTVlOTdcXHU5NGZhXFx1N2VkMVxcdTViOWFcXHVmZjFhMTBcXHU0ZTJhXFxuTGlzdGluZ1xcdTRmMThcXHU1MzE2XFx1ZmYxYTEwMFxcdTZiMjFcXFwvXFx1NjVlNVxcblxcdTdkMjJcXHU4YmM0XFx1NTI5ZlxcdTgwZmRcXHVmZjFhNTAwXFx1NmIyMVxcXC9cXHU2NWU1XFxuXFx1NGU5YVxcdTlhNmNcXHU5MDBhXFx1NjI0YlxcdTVkZTVcXHU1NGMxXFx1ZmYxYVxcdTRlMGRcXHU5NjUwXFxuXFx1NGUwYlxcdTY3YjZcXHU1NTQ2XFx1NTRjMVxcdTYzMTZcXHU2Mzk4XFx1ZmYxYVxcdTRlMGRcXHU5NjUwXFxuXFx1NGUwYlxcdTY3YjZcXHU1ZTk3XFx1OTRmYVxcdTYzMTZcXHU2Mzk4XFx1ZmYxYVxcdTRlMGRcXHU5NjUwXFxuXFx1NjU3MFxcdTYzNmVcXHU3NmQxXFx1NjNhN1xcdWZmMWFcXHU2NTJmXFx1NjMwMVxcbjxmb250IHN0eWxlPSdjb2xvcjojRjE3MDNGJz4zXFx1NTkyOVxcdThiZDVcXHU3NTI4XFx1NGVjNSQxXFxuXFx1OGJkNVxcdTc1MjhcXHU2NzFmXFx1OTVmNFxcdTUzZWZcXHU5NjhmXFx1NjVmNlxcdTUzZDZcXHU2ZDg4PFxcXC9mb250PlwiLFwiY29udGVudF9saXN0XzFcIjpcIlNlYXQ6IDEgU2VhdFxcblByb2R1Y3QgU2VhcmNoOiBVbmxpbWl0ZWRcXG5Qcm9kdWN0IENoYXJ0OiAyMDAwIGRhdGEgZW50cmllc1xcblNob3AgQ2hhcnQ6IDIwMDAgZGF0YSBlbnRyaWVzXFxuU2hvcCBTZWFyY2g6IFVubGltaXRlZFxcbktleXdvcmQgU2VhcmNoOiAyMDAgRGFpbHlcXG5GYXZvcml0ZXM6IFVwIHRvIDI1MDBcXG5FdHN5R1BUOiBVbmxpbWl0ZWRcXG5SZW1vdmUgQkc6IDEwMCBwaWNcXFwvd2tcXG5BSSBSZXBsYWNlIEJHOiAzNSBwaWNcXFwvd2tcXG5TaG9wIEFuYWx5c2lzOiBVbmxpbWl0ZWRcXG5CYXRjaCBLZXl3b3JkIEFuYWx5c2lzOiA1MCBEYWlseVxcbkNvbm5lY3RlZCBTaG9wczoxMCBzaG9wc1xcbkxpc3RpbmdPcHRpbWl6ZTogMTAwIERhaWx5XFxuRm9sbG93dXBSZW1pbmQ6IDUwMCBEYWlseVxcbkFtYXpvbiBIYW5kbWFkZTogVW5saW1pdGVkXFxuSW5hY3RpdmUgUHJvZHVjdHM6IFVubGltaXRlZFxcbkluYWN0aXZlIFNob3BzOiBVbmxpbWl0ZWRcXG5EYXRhIFRyYWNraW5nOiBTdXBwb3J0XFxuPGZvbnQgc3R5bGU9J2NvbG9yOiNGMTcwM0YnPjMtZGF5IFRyaWFsIGZvciBqdXN0ICQxXFxuQ2FuY2VsIGF0IGFueSB0aW1lPFxcXC9mb250PlwiLFwicGxhbl9jdXN0b21fc3R5bGVcIjp7XCJhY3RpdmVcIjpcInRydWVcIixcIm5vcm1hbF9idG5fdGV4dF9jb2xvclwiOlwiI0ZGRlwiLFwibm9ybWFsX2J0bl9iZ19jb2xvclwiOlwiIzQyNjdCMlwiLFwibm9ybWFsX2JvcmRlcl9jb2xvclwiOlwiIzQyNjdCMlwiLFwiaG92ZXJfYnRuX3RleHRfY29sb3JcIjpcIiNGRkZcIixcImhvdmVyX2J0bl9iZ19jb2xvclwiOlwiIzQyNjdCMlwiLFwiaG92ZXJfYm9yZGVyX2NvbG9yXCI6XCIjNDI2N0IyXCIsXCJob3Zlcl9zY2FsZVwiOlwiMTBcIixcInVzaW5nX2J0bl90ZXh0X2NvbG9yXCI6XCIjRkZGXCIsXCJ1c2luZ19idG5fYmdfY29sb3JcIjpcIiM0MjY3QjJcIixcInVzaW5nX2JvcmRlcl9jb2xvclwiOlwiIzQyNjdCMlwifSxcInRoZW1lX3N0eWxlXCI6XCIxXCIsXCJjb250ZW50X2xpc3Rfc3R5bGVcIjpcIjJcIixcImRlZmF1bHRfaWNvbl9jb2xvclwiOlwiI2YxNzAzZlwiLFwieWVhcl9zYXZlX3ByaWNlXCI6XCJcIixcImlzX3RyaWFsXCI6MSxcInRpdGxlXzFcIjpcIlByb1wiLFwicHJpY2VcIjpcIjE5Ljk5XCIsXCJzdWJfdGl0bGVfMVwiOlwiQWR2YW5jZWQgc2VsZWN0aW9uXFxuSGVscGluZyBtdWx0aS1zdG9yZSBzZWxsZXJcXG5cIixcInN1Yl90aXRsZVwiOlwiXFx1NTkxYVxcdTVlOTdcXHU5NGZhXFxcL1xcdTk0ZmFcXHU4ZDI3XFx1NTM1NlxcdTViYjZcXHU1ZmM1XFx1OTAwOVxcblxcdTlhZDhcXHU5NjM2XFx1OTAwOVxcdTU0YzFcXHU1MjlmXFx1ODBmZFxcdTUyYTlcXHU2MGE4XFx1NTkyN1xcdTUzNTZcIixcInRpdGxlXCI6XCJQcm9cIixcImJ0bl9uYW1lXCI6XCJcXHU3YWNiXFx1NTM3M1xcdThiYTJcXHU5NjA1XCIsXCJidG5fbmFtZV8xXCI6XCJHRVRcIixcInByaWNlX2Rlc1wiOlwiXCIsXCJ0cmlhbF9jdGFfbmFtZVwiOlwiMVxcdTdmOGVcXHU1MTQzXFx1OGJkNVxcdTc1MjhcIixcInRyaWFsX2N0YV9kZXNjcmliZVwiOlwiMVxcdTdmOGVcXHU1MTQzXFx1OGJkNVxcdTc1MjgzXFx1NTkyOSAtIFxcdTk2OGZcXHU2NWY2XFx1NTNlZlxcdTkwMDBcIixcInRyaWFsX2N0YV9uYW1lXzFcIjpcIlRyeSBmb3IgJDFcIixcInRyaWFsX2N0YV9kZXNjcmliZV8xXCI6XCIzIGRheXMgZm9yICQxIC0gQ2FuY2VsIGF0IGFueSB0aW1lXCIsXCJpc19vcGVuX2N1cnJlbmN5XCI6XCIwXCJ9IiwibGV2ZWwiOiIwIiwiaXNfZGVmYXVsdF9wbGFuIjoiMCIsInR5cGUiOiIwIiwic3RyaXBlX3N5bmNfc3RhdHVzIjoiMCIsImlzX2RlbGV0ZWQiOiIwIiwiY3JlYXRlZF9hdCI6IjIwMjItMDQtMjggMDE6MTc6NTEiLCJ1cGRhdGVkX2F0IjoiMjAyNC0wNC0wNCAyMTozMDowOCJ9fX0.Hwo4fHQ140N-2kqoVw_ha10xtm3Id0Qv4GO1aEwU4NY',
    # 'cookie': 'sbox-l=cn; sbox-guid=MTcxMzE3NzM2OHwzNDV8OTYxODk1MDEx; _uab_collina=171317737042970566538713; _trackUserId=G-1713177425000; _clck=1ow8zgy%7C2%7Cfky%7C0%7C1566; __stripe_mid=33c9954a-970b-4a14-b6db-0ae3787b25abd517ac; _csrf=939cce0ef1c224c18181d0a053af551ce96a21afbf7909f6c2cb856ad79a1647a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22waAws6Hz4cN5yVYq9mGQWTy-bcr-n33h%22%3B%7D; first_visit_path=%2Fecommerce%2Fcommon%2Fv1_0%2Fnew-user; anonymous_user_id=8228ab2946e1516ea4eecf430f6db700; is_first_visit=false; _gid=GA1.2.1066000858.1714111260; g_state={"i_l":0}; ZFSESSID=70tfcb1ls40682sg00pg97g6k4; _identity=61926c8a5e062338cc69d1bb737178c0a1856f85caff9ab7ac6d07aa7d8ecf20a%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A21%3A%22%5B7846853%2Cnull%2C259200%5D%22%3B%7D; last_login=efa616f9f9a24d3fbe46ab449e38cc587411edd5fbbe1ea9ffdd7dfb187dbecea%3A2%3A%7Bi%3A0%3Bs%3A10%3A%22last_login%22%3Bi%3A1%3Bi%3A3%3B%7D; crisp-client%2Fsession%2Fee0c1497-4d30-45d2-ae24-8157e37e83d4=session_48073b8f-ec61-4038-a214-59a9344d1429; __stripe_sid=9697f110-3e01-421e-b27b-e8da2cfcdf6830b821; _ga_M97JW26PVF=GS1.1.1714121193.4.1.1714122408.59.0.0; _ga=GA1.2.1200815540.1713177371; _gat_gtag_UA_140648082_9=1; SERVERID=b0398419351ae18d9b70be5d5b8153cf|1714122413|1714111240',
    'priority': 'u=1, i',
    'referer': 'https://etsyhunt.com/',
    'sec-ch-ua': '"Chromium";v="124", "Microsoft Edge";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0',
}

params = {
    'search_key': '',
    'category': '',
    'price': '',
    'sales_weekly': '',
    'sales': '',
    'favorites': '',
    'favorites_weekly': '',
    'reviews': '',
    'reviews_weekly': '',
    'product_type': '',
    'is_raving': '0',
    'is_pick': '0',
    'is_bestsell': '0',
    'listed_time': '',
    'country': '',
    'is_first': 'false',
    'currency_code': 'USD',
    'is_batch': '0',
    'sort_by': '1',
    'desc': '1',
    'page_num': '5',
    'page_size': '20',
}


def etsy_goods(page):
    params['page_num']=str(page)
    try:
        response = requests.get('https://etsyhunt.com/ecommerce/product/v1_0/list', params=params, headers=headers)

        print(page,'页',len(response.json()['data']),response.json()['data'])
    except Exception as e:
        print(e)

def produce():
    for page in range(1,300):
        q.put(page)


def consumer():
    try:
        while True:
            page = q.get()
            num=etsy_goods(page)
    except Exception as e:
        pass


produce()
pool = ThreadPool(10)
i=0
for _ in range(1):
    pool.apply_async(consumer)
pool.close()
pool.join()
