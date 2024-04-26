import tool
import json
import pandas as pd
load_jsonl = 'tt_author.jsonl'
down_jsonl = 'tt_author_describe.jsonl'
merge_jsonl = 'ixspy/tt_author_message.jsonl'

old_message = tool.land_jsonlines(load_jsonl)
merge_message=  tool.land_jsonlines(merge_jsonl)
category= tool.categoryid

author_data=pd.DataFrame([{'uniqueId':json.loads(author)['userInfo']['user']['uniqueId'],'nickname': json.loads(author)['userInfo']['user']['nickname'],'signature':json.loads(author)['userInfo']['user']['signature']} for author in old_message])
merge_data=pd.DataFrame(
    [
    {'uniqueId':json.loads(merge)['account'],
     '粉丝':json.loads(merge)['follower_total'],
     '点赞':json.loads(merge)['favorited_total'],
     '视频数':json.loads(merge)['aweme_total'],
     'category_id': [category[str(category_id)] for category_id in   json.loads(merge)['category_id'] if category_id>=100 ]
     }
      for merge in merge_message
    ]
)

author_data=pd.merge(author_data,merge_data,on=['uniqueId'])

print(author_data.to_excel('tt_author_describe.xlsx',index=False))


