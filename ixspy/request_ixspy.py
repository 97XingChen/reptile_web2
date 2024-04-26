import requests
from tt import tool


def get_anchor_message(favorited_total_start,favorited_total_end,coun):

    json_data = {
        'rank_time': 3,
        'rank_type': 'total',
        'page': 1,
        'size': 10000,
        'desc': 'desc',
        'order': 'follower_total',
        'region': coun,
        'category': '0',
        'follower_total_start': 0,
        'follower_total_end': 0,
        'favorited_total_start': str(favorited_total_start),
        'favorited_total_end': str(favorited_total_end),
        'verified_type': '0',
        'social': '',
        'time': 3,
    }

    response = requests.post('https://tik.ixspy.com/author-index',  json=json_data)
    return response

# category_list=[ 101+i   for i in range(29)    ]
# print(category_list)
# for category in category_list:

favorited_total_start=401054
favorited_total_end=494925
while True:

    data_lines=get_anchor_message(favorited_total_start,favorited_total_end,'US').json()['data']
    if data_lines["count"]<10000:
       print(favorited_total_start, favorited_total_end, 'suess')
       with open('log.txt', 'a') as f:
           f.write(str(favorited_total_start) +'  '+  str(favorited_total_end) +'  '+ 'success' + '\n')
       tool.down_jsonlines('ixspy_tt.jsonl', data_lines)
       favorited_total_end = favorited_total_start
       favorited_total_start=int(favorited_total_start/1.5)
    else:
        favorited_total_start = int(favorited_total_start*1.05)
        with open('log.txt', 'a') as f:
               f.write(str(favorited_total_start) +'  '+ str(favorited_total_end) + '\n')





