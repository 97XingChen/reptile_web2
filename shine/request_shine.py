from bs4 import BeautifulSoup
import requests
import tool
import json

def get_url(url,headers,cookies):
    return BeautifulSoup(requests.get(url, headers=headers,cookies=cookies).content, "lxml")


def down_goods(headers,cookies,down_jsonl):
    for i in range(1,33):
        url=f'https://us.shein.com/RecommendSelection/Women-Clothing-sc-017172961.html?page={i}'
        response=get_url(url, headers=headers, cookies=cookies)
        soup=BeautifulSoup(response.content, "lxml")
        good_html=soup.find_all('div',attrs={'class':'product-card__goods-title-container'})
        print(len(good_html))
        [ tool.down_jsonlines(down_jsonl,{"store":"shein","goods_url":'https://us.shein.com'+goods.a.get("href")}      )  for goods in good_html]

def down_picture(headers,cookies,load_jsonl,down_jsonl):

    goods_dict = tool.land_jsonlines(load_jsonl)
    picture_dict = tool.land_jsonlines(down_jsonl)
    href_list = [json.loads(goods)['goods_url'] for goods in goods_dict]
    href_list_end = [json.loads(goods)['href'] for goods in picture_dict]
    href_list=list(set(href_list)-set(href_list_end))
    for href in href_list:
        soup = get_url(href, headers=headers, cookies=cookies)
        picture_url_html=soup.find_all('div', attrs={'class': 'crop-image-container'})
        picture_url =list(set(['http:'+picture.get("data-before-crop-src").split('_thumbnail')[0].replace('http:','')+'.jpg' for picture in picture_url_html]))
        [tool.down_jsonlines(down_jsonl, {"store":"shein","href": href, "picture_url": picture})  for picture in   picture_url ]
        print(href,len(picture_url), 'success')



cookies = {
    '_gid': 'GA1.2.920909466.1703214938',
    '_gcl_au': '1.1.484811386.1703214938',
    'cookieId': '0EA23787_0F03_6494_554D_9AAD81F9BE14',
    '_ga_X55LK525VE': 'GS1.2.1703214938.1.1.1703214962.36.0.0',
    'sessionID_shein': 's%3Aya32kj_ej8weNkE4i-rW42qUWbgqD-ET.ALuV6hnLaIZZJXlQ%2BFmGmKzUPeC6X9N95jl8TlYuAxc',
    'RESOURCE_ADAPT_WEBP': '1',
    'country': 'US',
    'countryId': '226',
    'smidV2': '2023122211175932af8356f772bd276b575d6558d53e44002c749af16352b50',
    '_csrf': 'nB1kMxyTS_xOTxmuunzV3tuH',
    'rskxRunCookie': '0',
    'rCookie': 'bea8x69ux4c5d9l6oke2iwlqg2ady2',
    '_scid': 'a51da2fd-7318-4fc2-99fc-1339ebd2b93a',
    '_pin_unauth': 'dWlkPU1USXdPV1JqTnpZdE5UazBNUzAwTlRnNExUbGpObVF0TTJabFlqYzJObUkzT0RnNQ',
    '_fbp': 'fb.1.1703215093421.2143953563',
    '_aimtellSubscriberID': '983a65fa-bced-28c3-0e0a-59cc4407ab06',
    '_sctr': '1%7C1703174400000',
    '_abck': '9C6CB4EBE10A4BF81B813A8E5EEF86F6~-1~YAAQNPh330ikU2iMAQAAKWZxkAuCrFUo2EA9Ghm240iQ7GFO4hTpM1RPG0E3QGP3LwWZ0XcNNRSURVBk08oikEJ7yp5EBngxv6xtjC0lr1CmcNO67ftY+78GdZ8PHIr0PCoNZ8yXzu9g8uM/eYLEpnIkgarRKNY0/nZ4SKDakY3iQUnOSVBgbcOfPJZHUwN+m5gqMp0jBmDwhfprDQBBYn/6H1PNPfZKTgl7nKwavYBhw3UX8CbcqnhZukVbkVK4y/gf61XTj/2GLCZtcEWX/sEYWCHZkZRx9sAqPOrSv+H5XkD5xo5hHiaHHbmQ9Gq0ZwEZzPYJw6aUIsoPvbSlQVTPTCaOZeNebqrVe0YMzW0kQZGQq/83CUa2VKnj9dmiE5Wd3IG/jgx0bg==~-1~-1~-1',
    'bm_sz': '435D4B5449865A4077CFF8D7DBE19BF7~YAAQNPh330qkU2iMAQAAKWZxkBYpV+4SnxkiaB5C6s/Wo2VILkZUTetaOUUKkXzBww2SUhdV3d5+wLSQkjh9HFglIhUCvM5Qv9OMAdUbu5yT59jIUUv2dzOhwY4H/wx0DQD3BDSxjKQLmVGtY+qJk3YsYl8iVrrlYNDqEWkC0Hn6hpraKrcdWvIMYDo7yljNl28p7EVoTOH9XJ0Fw9lBd69R4MnIzFyQnZUj1Toe43Rcof/LUuQ9vpG/BUB4JeYV17jgQJqo2sigBL8msCScxhuH0EpCG5c5p+vDykqvZ7JWeQ==~3359031~3684409',
    '_cfuvid': 'fpTULRKSCHHHLPJ.RPUPz3dVdigbwds73JGv2pM7rBE-1703231727461-0-604800000',
    'cf_clearance': 'lMnuOqH9e5YCfh7_0xGj7mpAqo4r275xAogKg8.hinE-1703236181-0-2-c79fc64f.fbdfc1ac.909e99af-0.2.1703236181',
    'ftr_blst_1h': '1703236189155',
    'scarab.visitor': '%226D8C9DE997FFB250%22',
    'cto_bundle': 'kXaXZ19mdEYyanZJbmp3N0dUTkVpVnIyQkxOSnpLSlFnZHlmMnoxT3F3V0dmUWRpMFBIVlAlMkZzTEhnbUw4NkliOVpLd0ExY3E1TWtQbktZNElmY0hITjRGWDJtNHJTSVlUbElURVhpOHkwJTJCaSUyRmlQNW11T0tuMExoJTJCQ1gxZVNGREd4T3RtOTZqJTJGcW91MFglMkZkempZQmlsaWFFWXclM0QlM0Q',
    'lastRskxRun': '1703236720983',
    'forterToken': '03b9415f8f83411a864e8dbc554bb554_1703236721870__UDF43-m4_17ck',
    '__cf_bm': 'X6tKdGDOTIlZiIjPl1da9pZ1SQIOUwiA1nKQ3gFGtaI-1703237320-1-AX0d+oW4mKdN/MSZY1b+CVURvF2HPiFJeFrzOKpiqwDBfwNEY8OBhdqRxP5wh+Zqu8YRIZhWEOARsSkFYtgMaNQ=',
    'us_double_lang': 'us',
    'OptanonConsent': 'isIABGlobal=false&datestamp=Fri+Dec+22+2023+17%3A35%3A56+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=6.13.0&hosts=&consentId=8543438b-307d-477c-9ae8-a000d1902e9e&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CSPD_BG%3A1%2CC0002%3A1%2CC0004%3A1&AwaitingReconsent=false',
    '_gat_shein': '1',
    '_uetsid': 'bd1413b0a07811eeb3e4dd210ccdee6c',
    '_uetvid': 'bd143cd0a07811eeb1919b23bd767144',
    '_scid_r': 'a51da2fd-7318-4fc2-99fc-1339ebd2b93a',
    '_ga': 'GA1.1.1318752923.1703214938',
    '_ga_SC3MXK8VH1': 'GS1.1.1703236189.4.1.1703237761.43.0.0',
    'dicbo_id': '%7B%22dicbo_fetch%22%3A1703237762173%7D',
    '_f_c_llbs_': 'K1901_1703237761_Bbq8R1yM56bgpYBC0STypU2uxgB_a4gIkScSZr-1ioZpDPfi33a759LfWa7wZ1tbSgSx78yq8oS17eyvelBwvsgZifjTMiekZS8roesWerF8CxwJ3W4PKSYO1Dxfn3bhpjU2SO3GS1qgQ4iqKxiFeoMLvrSmkR_mjonevTxqVLXUhSdqjH2iIHDYIoJ8VgK1W3M7DjkTceKIx46Ci6uQvhsVSWcEUEs-sszo9GhhHLKIi0KLosSfPQ2sFcw03OVSO2rn7WrMqsy7iGdYvBUbQ3C7UUVs3GGeH33Vo6j59U9pPRPfNGle844Hv7lkdRdqeicCiMPVYKXzqjUdWEf2OA',
}

headers = {
    'authority': 'us.shein.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    # 'cookie': '_gid=GA1.2.920909466.1703214938; _gcl_au=1.1.484811386.1703214938; cookieId=0EA23787_0F03_6494_554D_9AAD81F9BE14; _ga_X55LK525VE=GS1.2.1703214938.1.1.1703214962.36.0.0; sessionID_shein=s%3Aya32kj_ej8weNkE4i-rW42qUWbgqD-ET.ALuV6hnLaIZZJXlQ%2BFmGmKzUPeC6X9N95jl8TlYuAxc; RESOURCE_ADAPT_WEBP=1; country=US; countryId=226; smidV2=2023122211175932af8356f772bd276b575d6558d53e44002c749af16352b50; _csrf=nB1kMxyTS_xOTxmuunzV3tuH; rskxRunCookie=0; rCookie=bea8x69ux4c5d9l6oke2iwlqg2ady2; _scid=a51da2fd-7318-4fc2-99fc-1339ebd2b93a; _pin_unauth=dWlkPU1USXdPV1JqTnpZdE5UazBNUzAwTlRnNExUbGpObVF0TTJabFlqYzJObUkzT0RnNQ; _fbp=fb.1.1703215093421.2143953563; _aimtellSubscriberID=983a65fa-bced-28c3-0e0a-59cc4407ab06; _sctr=1%7C1703174400000; _abck=9C6CB4EBE10A4BF81B813A8E5EEF86F6~-1~YAAQNPh330ikU2iMAQAAKWZxkAuCrFUo2EA9Ghm240iQ7GFO4hTpM1RPG0E3QGP3LwWZ0XcNNRSURVBk08oikEJ7yp5EBngxv6xtjC0lr1CmcNO67ftY+78GdZ8PHIr0PCoNZ8yXzu9g8uM/eYLEpnIkgarRKNY0/nZ4SKDakY3iQUnOSVBgbcOfPJZHUwN+m5gqMp0jBmDwhfprDQBBYn/6H1PNPfZKTgl7nKwavYBhw3UX8CbcqnhZukVbkVK4y/gf61XTj/2GLCZtcEWX/sEYWCHZkZRx9sAqPOrSv+H5XkD5xo5hHiaHHbmQ9Gq0ZwEZzPYJw6aUIsoPvbSlQVTPTCaOZeNebqrVe0YMzW0kQZGQq/83CUa2VKnj9dmiE5Wd3IG/jgx0bg==~-1~-1~-1; ak_bmsc=00D7FB8A984965104ED4BAC752662B53~000000000000000000000000000000~YAAQNPh330mkU2iMAQAAKWZxkBZFSm1rWHetwn37+tv3kt3FroOgXO9VNDKxCFCbckAD7/v4CSxewoqC/FuU5B07G0Waq9e7e0mPrVqMiJid4f+/EOx3jy2Kt0bWrF0PoMvdd/CWCkBn4sG4H6wxxzprMPeo0ByNaNn0mKI8b0PNEfgkxhrjmkfM17Yzso0UnbxKiwkNclKIBqHWj7DOsfRQwifrv6u/R9s56Gcvp2HolWVojgilPCGrqFBBl228cOhoVSUVY0MkimUzGH5fh2sD9Muatp5l8w9uqIDhVYVkwwyNlST+eEfQq7KzC0efZ5FPbuVTpMJcLAfB4j1loCz4gqr8w7xfe/4Bvk97XQvD1V83r173EFcvHDl98IANBWnDlrDLRlA=; bm_sz=435D4B5449865A4077CFF8D7DBE19BF7~YAAQNPh330qkU2iMAQAAKWZxkBYpV+4SnxkiaB5C6s/Wo2VILkZUTetaOUUKkXzBww2SUhdV3d5+wLSQkjh9HFglIhUCvM5Qv9OMAdUbu5yT59jIUUv2dzOhwY4H/wx0DQD3BDSxjKQLmVGtY+qJk3YsYl8iVrrlYNDqEWkC0Hn6hpraKrcdWvIMYDo7yljNl28p7EVoTOH9XJ0Fw9lBd69R4MnIzFyQnZUj1Toe43Rcof/LUuQ9vpG/BUB4JeYV17jgQJqo2sigBL8msCScxhuH0EpCG5c5p+vDykqvZ7JWeQ==~3359031~3684409; bm_sv=1956C6143B473EA74554D03A9A36BF26~YAAQNPh337+qU2iMAQAAlbBxkBYgZcxedLXBPJNSkmSpCRtaEn8STpeLtDwEGw3ZNckN5NS4n5+EdKJMYba/QwRz3L23ZXaMsy3tvqjxEkBVQKTwUs8MBBXliqjkBE8pejUsLJWjlwWMJ0oPBWij6Z0lzrb0z8K2xonvsPdK03OUWhe0uTbfcSZOPh7o2ADDXPPtHxIVnfMqwz2Q1bina8mdeYNhhRP05/KCmIaAAoUa1uPHYtyR9DAffxcRwX4=~1; _cfuvid=fpTULRKSCHHHLPJ.RPUPz3dVdigbwds73JGv2pM7rBE-1703231727461-0-604800000; ftr_blst_1h=1703231736683; cto_bundle=SI6jB19mdEYyanZJbmp3N0dUTkVpVnIyQkxES0M4cmZ3dTBmV1luek45THp0ZWJXS3FLdHFxWTAyV2M3bUgxSmI4ZkxJQTdDeUN4RDElMkJncXFxJTJGZHJNS0hlMXNMVnJ4WTJ1Uno4YXBITjJCakVudTg2MiUyRlhhUm9EVWFxWXdHUk1QNmdXelNhSlgyb2xuJTJGUjA4V0Z3QU52ekN4dyUzRCUzRA; lastRskxRun=1703231840868; forterToken=03b9415f8f83411a864e8dbc554bb554_1703231844367__UDF43-m4_17ck; __cf_bm=EKkJniYVEe5pVeGOCXHjwkOB2ZvIP1XjH6p4PHEzqC4-1703232922-1-AQ0HUxxiOYOEOuKU/cBZDUdkH+CPUzAYtE9y1ytjIaDMuSPmghJHRLErUlRqoZok67pVWhPo98qpm75B55qFR1I=; us_double_lang=us; cf_clearance=nAsm73Dnb3ZEfO2UkLJvSzejDAyzI5fNvcAlO2v4jBo-1703233673-0-2-c79fc64f.fbdfc1ac.909e99af-0.2.1703233673; OptanonConsent=isIABGlobal=false&datestamp=Fri+Dec+22+2023+16%3A27%3A54+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=6.13.0&hosts=&consentId=8543438b-307d-477c-9ae8-a000d1902e9e&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CSPD_BG%3A1%2CC0002%3A1%2CC0004%3A1&AwaitingReconsent=false; _gat_shein=1; _uetsid=bd1413b0a07811eeb3e4dd210ccdee6c; _uetvid=bd143cd0a07811eeb1919b23bd767144; _scid_r=a51da2fd-7318-4fc2-99fc-1339ebd2b93a; _ga_SC3MXK8VH1=GS1.1.1703233671.3.1.1703233679.52.0.0; _ga=GA1.1.1318752923.1703214938; dicbo_id=%7B%22dicbo_fetch%22%3A1703233681200%7D; _f_c_llbs_=K1901_1703233681_cc-hrF-iYMxKo5QXUOMdlhrdl-SF--V8uGcC_WduBPecsnWIsZzOa1rNkmOYVnZXbYp70RedBqf1XuNLKz7Tumou7fgkGY4qPc9oBg0L2VQH_FNgPCTGkj_1WmqR1-Tg4Ig6GiywFuwe84fD1PT02vv-x0d21-iwtkvLpV_7Gdu28k5WHhF9m6fnmLLpd5famnL7xw3yaxiwLnWkiHTGtRfyYxhxHsrxRHP36_V_CyBy-0BUi1LX97CI_4C_6M_lf80-3rb0L78M18BjkwPSuYQCPLmy61rlRKfiCaDj3dc-8ce62EQghUMwGYdqWxVSw4NDYUJ5sQXPkTmsRtSKog',
    'referer': 'https://us.shein.com/risk/challenge?captcha_type=901&cookie_duratio=3600&redirection=%2FRecommendSelection%2FWomen-Clothing-sc-017172961.html',
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


load_jsonl='shein_women_clothes.jsonl'
down_jsonl='shein_women_picture.jsonl'

down_picture(headers,cookies,load_jsonl,down_jsonl)


#获取商品数据
# goods_dict=json.loads(re.findall('var gbProductListSsrData = (.*?)"styles":""}',str(soup))[0][0:-1]+'}')
# print(len(goods_dict['results']['goods']))