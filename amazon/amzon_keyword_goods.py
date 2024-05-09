import pandas as pd
import requests

import requests
from bs4 import  BeautifulSoup
import datetime
cookies = {
    'csm-sid': '483-9647847-3382955',
    'x-amz-captcha-1': '1715074200072037',
    'x-amz-captcha-2': 'J/1YU32m1kJq7aEVWxcR+Q==',
    'session-id': '133-5291239-3745228',
    'i18n-prefs': 'USD',
    'skin': 'noskin',
    'ubid-main': '134-7955364-9734702',
    'lc-main': 'en_US',
    'at-main': 'Atza|IwEBII8C9G_Rxo7i4dVkKiVyDJFd2onI4h5G_e-UVYgMHOFsnP1cOAxM7EnkNvNncRQc3eoaI44r-pBXFVcpohHIsGharXO1ub7MMP5Tp9ILIM2jLbuKNhDgwzUIousuqRXy0ZTbGW8wd8CKWH6g5nfEhQlfwfitIfs3-xNuOzo4kZemSpJRmKYEmz_s3pA-BmDhcX7-aiPky6cjSs1ShfkTTgUhf7Ta3NM7fQVR1kPZ00NSZQ',
    'sess-at-main': '"iP8cSMmeUDfeMfPiv0C8qPB8Y4/kPUmBvzGj307dGyY="',
    'sst-main': 'Sst1|PQEjpvLo30Pv9tBWVeZn5RASCU-W_MVor5_TvvPDS8DkZjYC9UUm4sEafm7KcQePbRk37VSnxyh2wbWVZB0VWKEDFlIuacWOOH4KwgQfC-gDDBx5u4AyfXPAmNIhIdbKQYDNfhIza3egzWKBlVxI4guPlH54PmSDlI4XB9D2YiHJLhkzJjaqqdUe3JfpQXAh8EvF98CBPwQdCC4WrSm-C4ClYkT8Aq1ZwO0CcGWrDivtY7T_v5vPW4poMKOQPpQM2gKo81oA6qHOnfxvMztmjz9-r2I6mH2MF9Hu5pxbYLX_XOw',
    'x-main': '"I8hcd@lJUt41RRkC?PD2unCn?1DhiShaEG10DqrJqkJmGj69evVdoYe1Rtgywgvs"',
    'session-id-time': '2082787201l',
    'session-token': 'BLorgFylGa8qN86DH/XfvNBPMbltRyIUrhdC+CeHuvKbtz4ZKcQdLi19reQ1Ocrnyovf6OqUxk8NijSi9RYeTALI6MfRDRM815NUksHQx5fiTBrryUV94zc5KfHv7exW6FhTN8k5Omf+hC8FgGDE6EigqmQ/ppUv00yUwdPXA188OQOViqV9TJttzqTb6KSMTfyphdptKrFb4Seneb7iSSpphfClrCCh6hRkGfUC/ZFr+JbkM2I6tSQGMw68nVD5v59cmDD5W52h8Ft1LYpqLnaAoQ2AgxXQsAs9G9CNUWN6kcpeTY50lU9dLbUN4fp7WmLcFd3C7VJInpeWJBvGbDfvBU8Qjtqwf4zLwc3570HK77D1GvxRpIltwnqQCGUU',
    'JSESSIONID': 'FC5C537F3D69D30E0DCFFED0B17D28F0',
    'csm-hit': 'tb:9TBA50N71B5GPAVWK2TN+s-3DEFPSPZ5NJVT1DX9WCX|1715074865198&t:1715074865198&adb:adblk_no',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'max-age=0',
    # 'cookie': 'csm-sid=483-9647847-3382955; x-amz-captcha-1=1715074200072037; x-amz-captcha-2=J/1YU32m1kJq7aEVWxcR+Q==; session-id=133-5291239-3745228; i18n-prefs=USD; skin=noskin; ubid-main=134-7955364-9734702; lc-main=en_US; at-main=Atza|IwEBII8C9G_Rxo7i4dVkKiVyDJFd2onI4h5G_e-UVYgMHOFsnP1cOAxM7EnkNvNncRQc3eoaI44r-pBXFVcpohHIsGharXO1ub7MMP5Tp9ILIM2jLbuKNhDgwzUIousuqRXy0ZTbGW8wd8CKWH6g5nfEhQlfwfitIfs3-xNuOzo4kZemSpJRmKYEmz_s3pA-BmDhcX7-aiPky6cjSs1ShfkTTgUhf7Ta3NM7fQVR1kPZ00NSZQ; sess-at-main="iP8cSMmeUDfeMfPiv0C8qPB8Y4/kPUmBvzGj307dGyY="; sst-main=Sst1|PQEjpvLo30Pv9tBWVeZn5RASCU-W_MVor5_TvvPDS8DkZjYC9UUm4sEafm7KcQePbRk37VSnxyh2wbWVZB0VWKEDFlIuacWOOH4KwgQfC-gDDBx5u4AyfXPAmNIhIdbKQYDNfhIza3egzWKBlVxI4guPlH54PmSDlI4XB9D2YiHJLhkzJjaqqdUe3JfpQXAh8EvF98CBPwQdCC4WrSm-C4ClYkT8Aq1ZwO0CcGWrDivtY7T_v5vPW4poMKOQPpQM2gKo81oA6qHOnfxvMztmjz9-r2I6mH2MF9Hu5pxbYLX_XOw; x-main="I8hcd@lJUt41RRkC?PD2unCn?1DhiShaEG10DqrJqkJmGj69evVdoYe1Rtgywgvs"; session-id-time=2082787201l; session-token=BLorgFylGa8qN86DH/XfvNBPMbltRyIUrhdC+CeHuvKbtz4ZKcQdLi19reQ1Ocrnyovf6OqUxk8NijSi9RYeTALI6MfRDRM815NUksHQx5fiTBrryUV94zc5KfHv7exW6FhTN8k5Omf+hC8FgGDE6EigqmQ/ppUv00yUwdPXA188OQOViqV9TJttzqTb6KSMTfyphdptKrFb4Seneb7iSSpphfClrCCh6hRkGfUC/ZFr+JbkM2I6tSQGMw68nVD5v59cmDD5W52h8Ft1LYpqLnaAoQ2AgxXQsAs9G9CNUWN6kcpeTY50lU9dLbUN4fp7WmLcFd3C7VJInpeWJBvGbDfvBU8Qjtqwf4zLwc3570HK77D1GvxRpIltwnqQCGUU; JSESSIONID=FC5C537F3D69D30E0DCFFED0B17D28F0; csm-hit=tb:9TBA50N71B5GPAVWK2TN+s-3DEFPSPZ5NJVT1DX9WCX|1715074865198&t:1715074865198&adb:adblk_no',
    'device-memory': '8',
    'downlink': '1.5',
    'dpr': '0.9',
    'ect': '3g',
    'priority': 'u=0, i',
    'rtt': '350',
    'sec-ch-device-memory': '8',
    'sec-ch-dpr': '0.9',
    'sec-ch-ua': '"Chromium";v="124", "Microsoft Edge";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-ch-viewport-width': '506',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0',
    'viewport-width': '506',
}

params = {
    'k': '1st mothers day',
    'i': 'fashion-womens-jewelry',
    'rh': 'n:7192394011,p_n_date_first_available_absolute:15196853011',
    'page':1
}


keyword_list=['100th anniversary','1st communion gift','1st mothers day','2024 solar eclipse','acotar','aesthetic jewelry',
              'aka','anatomy','ancient egypt','ankh necklace','aquarius','arabic','armor','ateez']
cate_list=['fashion-mens-jewelry']
goods_dict_list=[]
for keyword in keyword_list:
    for cate  in cate_list:
        goods_num=48
        page=1
        while goods_num>=48:
            params['k']=keyword
            params['i'] = cate
            params['page'] = page
            try:
                response = requests.get('https://www.amazon.com/s', params=params, cookies=cookies, headers=headers)
                bs_1=BeautifulSoup(response.content,'lxml')
                goods_html_list=bs_1.findAll('div',attrs={'class':'a-section a-spacing-base a-text-center'})
                for goods_html in goods_html_list:
                    shop = goods_html.find('span',attrs={'class':'a-size-base-plus a-color-base'}).text
                    title = goods_html.find('span', attrs={'class': 'a-size-base-plus a-color-base a-text-normal'}).text
                    url= 'https://www.amazon.com'+goods_html.find('a', attrs={'class': 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})['href'] \
                        if goods_html.find('a', attrs={'class': 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})else None
                    price = goods_html.find('span', attrs={'class': 'a-offscreen'}).text if goods_html.find('span', attrs={'class': 'a-offscreen'}) else None
                    starts=  goods_html.find('span', attrs={'class': 'a-icon-alt'}).text  if goods_html.find('span', attrs={'class': 'a-icon-alt'}) else None
                    ratings= goods_html.find('span', attrs={'class': 'a-size-base s-underline-text'}).text  if goods_html.find('span', attrs={'class': 'a-size-base s-underline-text'}) else None
                    goods_dict = {'shop':shop,'title':title,'url':url,'price':price,"starts":starts,"ratings":ratings,'New_Arrivals':"Last 90 days",'date':datetime.datetime.now().strftime('%F')}
                    goods_dict =dict(**goods_dict,**params)
                    goods_dict_list.append(goods_dict)
                goods_num=len(goods_html_list)
                page+=1
                print(params, '成功',goods_num)
            except Exception as e:
                goods_num = 48
                print(params,'失败',e)

goods_data=pd.DataFrame(goods_dict_list)
goods_data.to_excel('amzon_keywords_goods.xlsx',index=False)


