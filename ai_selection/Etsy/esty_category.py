import pandas as pd
import requests
import json
cookies = {
    'user_prefs': 'oSG35Zl3BrmW75_Xw9Rl0PpiszFjZACC1Kau-TA6Wik02EVJJ680J0dHKTVPNzRYSUcJRIBFjCAULiKWAQA.',
    'fve': '1703053983.0',
    'ua': '531227642bc86f3b5fd7103a0c0b4fd6',
    '_ga': 'GA1.1.349209306.1703053990',
    '__pdst': 'd7c3087fcef44e4da178dcc5fbc1b090',
    '_pin_unauth': 'dWlkPU9XSXlObVF4TldVdFptWmhaUzAwTkdRNUxUZ3dNemN0TjJZeU1tRXlPVE0yWVdJNA',
    '_tt_enable_cookie': '1',
    '_ttp': 'AkX-63GaJGLt38hi7pZ5ckDDIki',
    'uaid': 'qejak4ZLIxl9Iw-2hIPNGE2ulRpjZACC1Kau-SA6TeHJ7Gql0sTMFCUrpYgqJ9OIfNPgtMKgIMPczIhKrxLdkuSILDfdfFelWgYA',
    '_fbp': 'fb.1.1713431707131.8621907207013255',
    'exp_ebid': 'm=2iqi9lrP9u0R6p4ka8bae486u7d7JZN%2B5HZXaR4dG6I%3D,v=ukeXWPGNbUJurjezCzjQ03hpYReKGm6c',
    'search_history_v2': '0evGvCpCc6w_zitSqCIi4IPsg8xjZACCNIUny2B0tVJxamJRckZqsZJVdLVSYWlqUaWSlVJ6ZlqJko5SSWZuanxxSWJugZKVobmhsYkxkLTQUcpILI4vSi0uzSkBaispKk2tja1lAAA.',
    'gift_session_v2': 'aJc-VMtTagi2HMdvUbnEzROjx1tjZACCNIUny2C0IQMA',
    '_gcl_au': '1.1.1915080365.1713431735',
    'lantern': 'f82c126e-bf35-4979-b58e-29885a3023ff',
    'wedding_session': 'aJK6SLjzqCnhnJAmdJV-q3HVFitjZACCNDWeSjgNAA..',
    '_ga_SY8CXZVMTN': 'GS1.1.1713775017.1.0.1713775017.0.0.0',
    '_ga_3LML020ELY': 'GS1.1.1713774790.2.1.1713775373.0.0.0',
    'hs_listing_views': 'to0w9StCu97d_9_6JIUg_5r7I9JjZACCNNWbE8C0muqSaiVDc0MLS1MDS0NjJStjHSDXwMTC0MTM2EzJyhDKNTKzMAVyjYBcAzMLc0NTQxNzJSuTWgYA',
    'last_browse_page': 'https%3A%2F%2Fwww.etsy.com%2Fshop%2FCloverMinimalist',
    '_uetsid': '69eec440005311efa77241c63aee4f18',
    '_uetvid': 'a4b75b109f0111ee93e3a5883c816c9b',
    'granify.uuid': '0920899d-44bc-411f-b726-60338c31668c',
    'granify.new_user.qivBM': 'false',
    'granify.session.qivBM': '-1',
    'datadome': 'UhWalTYTEQiFeYtw2lQOqtqrrX3Eg8zIHIm8q413b_z_MVRfsvBzTd97AYGIj4e0eEq8KBblnzytXZw18qsMT8Hdsyzj6GfKXnEKzEYfnzHQRXKdYpFSdyNjY0QRmzkD',
    '_ga_KR3J610VYM': 'GS1.1.1713778719.8.1.1713779669.12.0.0',
}

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'user_prefs=oSG35Zl3BrmW75_Xw9Rl0PpiszFjZACC1Kau-TA6Wik02EVJJ680J0dHKTVPNzRYSUcJRIBFjCAULiKWAQA.; fve=1703053983.0; ua=531227642bc86f3b5fd7103a0c0b4fd6; _ga=GA1.1.349209306.1703053990; __pdst=d7c3087fcef44e4da178dcc5fbc1b090; _pin_unauth=dWlkPU9XSXlObVF4TldVdFptWmhaUzAwTkdRNUxUZ3dNemN0TjJZeU1tRXlPVE0yWVdJNA; _tt_enable_cookie=1; _ttp=AkX-63GaJGLt38hi7pZ5ckDDIki; uaid=qejak4ZLIxl9Iw-2hIPNGE2ulRpjZACC1Kau-SA6TeHJ7Gql0sTMFCUrpYgqJ9OIfNPgtMKgIMPczIhKrxLdkuSILDfdfFelWgYA; _fbp=fb.1.1713431707131.8621907207013255; exp_ebid=m=2iqi9lrP9u0R6p4ka8bae486u7d7JZN%2B5HZXaR4dG6I%3D,v=ukeXWPGNbUJurjezCzjQ03hpYReKGm6c; search_history_v2=0evGvCpCc6w_zitSqCIi4IPsg8xjZACCNIUny2B0tVJxamJRckZqsZJVdLVSYWlqUaWSlVJ6ZlqJko5SSWZuanxxSWJugZKVobmhsYkxkLTQUcpILI4vSi0uzSkBaispKk2tja1lAAA.; gift_session_v2=aJc-VMtTagi2HMdvUbnEzROjx1tjZACCNIUny2C0IQMA; _gcl_au=1.1.1915080365.1713431735; lantern=f82c126e-bf35-4979-b58e-29885a3023ff; wedding_session=aJK6SLjzqCnhnJAmdJV-q3HVFitjZACCNDWeSjgNAA..; _ga_SY8CXZVMTN=GS1.1.1713775017.1.0.1713775017.0.0.0; _ga_3LML020ELY=GS1.1.1713774790.2.1.1713775373.0.0.0; hs_listing_views=to0w9StCu97d_9_6JIUg_5r7I9JjZACCNNWbE8C0muqSaiVDc0MLS1MDS0NjJStjHSDXwMTC0MTM2EzJyhDKNTKzMAVyjYBcAzMLc0NTQxNzJSuTWgYA; last_browse_page=https%3A%2F%2Fwww.etsy.com%2Fshop%2FCloverMinimalist; _uetsid=69eec440005311efa77241c63aee4f18; _uetvid=a4b75b109f0111ee93e3a5883c816c9b; granify.uuid=0920899d-44bc-411f-b726-60338c31668c; granify.new_user.qivBM=false; granify.session.qivBM=-1; datadome=UhWalTYTEQiFeYtw2lQOqtqrrX3Eg8zIHIm8q413b_z_MVRfsvBzTd97AYGIj4e0eEq8KBblnzytXZw18qsMT8Hdsyzj6GfKXnEKzEYfnzHQRXKdYpFSdyNjY0QRmzkD; _ga_KR3J610VYM=GS1.1.1713778719.8.1.1713779669.12.0.0',
    'downlink': '1.55',
    'dpr': '1',
    'ect': '3g',
    'origin': 'https://www.etsy.com',
    'priority': 'u=1, i',
    'referer': 'https://www.etsy.com/c/jewelry/brooches-pins-and-clips/clothing-and-shoe-clips/dress-clips?explicit=1&ship_to=US&order=date_desc&category_landing_page=true',
    'rtt': '350',
    'sec-ch-dpr': '1',
    'sec-ch-ua': '"Chromium";v="124", "Microsoft Edge";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version-list': '"Chromium";v="124.0.6367.61", "Microsoft Edge";v="124.0.2478.51", "Not-A.Brand";v="99.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0',
    'x-csrf-token': '3:1713779669:ZKzvFxjDb3cy3FoyeCu9r9uv2QgW:2bdc6e97701463495b789049f29f02bb6582576ea9518320384552561bc22f6b',
    'x-detected-locale': 'USD|en-US|US',
    'x-page-guid': 'f963448aadf.a568002b18cd7174f28d.00',
    'x-requested-with': 'XMLHttpRequest',
}

data = {
    'facet_counts': '{"1179":4502,"1202":4502,"2146":4502,"10840":4502}',
    'node_id': '2146',
    'is_category_page': 'true',
}

response = requests.post(
    'https://www.etsy.com/api/v3/ajax/public/search/view/category-selector',
    cookies=cookies,
    headers=headers,
    data=data,
)
Category_list=response.json()['regions']['nodes']

print(Category_list)
Category_all_list=[]


def iterate_json(Category_list):
    if len(Category_list)>0:
        for Category in   Category_list:
            Category_dict = {"view_name": Category['view_name'],
                             "template":Category['template'],
                             "id":Category['data']['id'],
                             "name": Category['data']['name'],
                             "padding_level": Category['data']['padding_level'],
                             "margin_level": Category['data']['margin_level'],
                             "path": Category['data']['path'],
                             "show_children": Category['data']['show_children'],
                             "is_selected": Category['data']['is_selected'],
                             "show_node": Category['data']['show_node'],
                             }
            Category_all_list.append(Category_dict)
            iterate_json(Category['regions']['nodes'])

iterate_json(Category_list)

Category_all_data=pd.DataFrame(Category_all_list)
Category_all_data.to_excel('Category_all_data.xlsx',index=False)



