from TikTokApi import TikTokApi
import asyncio
import tool
import json

ms_token=['6jm1b-46dptt04LRXvy8IjJoT8hNqdm-RR2qo2d7ubWfFPty1ORXYgJTij2coGDrWoZwl8gpmLyglsPYUmT0WxKLeZdUZvNz_hOZJgbp7BMhewQrP_h2WGc8u1xnnItpRr6JMrc=',
          'RJFFng5n1s87VlcP7Mbzw65SKwMGqAeoGBuYS-YPCIg-d-C1CB-FDsExedIq_xI9uJcSk2IJ7LMioqQI3BsKjlDgkJLwjhrGxY9DIsOgrwz86Uf_8p0I_7vTdmHLsdpp49Rbw8Xzk2fREw0v',
          'Qo9lrkwCqSuUhm65BLvYbQCA8NS8kIGr2B5xHHwuen_Vp80U86MkfXE2IC3vkLrF9yPe0nJJlFRxaBIYPPhu8lXLjLKv2hOl76K0riapqzZYPxw80jNefA6580DZ6HWPuYAsebEApCoeArZo',
          'ltzbmk_NxCCl_NGpc3WFUhmgoi4rbqK-Rmj_Fd5ibYYVYSUZ6-BHqdDgKhmWbsnEmC2ryzruDD4a2RBBv-ym0vrGPeYQ0hpQDPikI_mjxVbzVpok6uk93XGHzz-XeZSjv0N7GhjsxJWwML-a',
]
async def get_video_example(name1,name2,num,sem,down_jsonl):

    async with sem:
        async with TikTokApi() as api:
            await api.create_sessions(ms_tokens=ms_token, num_sessions=num, sleep_after=2,headless=False)

            user1 = api.user(username=name1)
            user2 = api.user(username=name2)


            print(name1, name2)
            user_data1 = await user1.info()
            user_data2 = await user2.info()

            tool.down_jsonlines(down_jsonl, user_data1)
            tool.down_jsonlines(down_jsonl, user_data2)

            tool.down_txt('user.txt', name1 + '\n' + name2)





if __name__ == "__main__":
    down_jsonl = 'tt_author.jsonl'
    message= tool.land_jsonlines('../ixspy/ixspy_tt.jsonl')

    ##历史已经抓过的数据
    old_message = tool.land_jsonlines(down_jsonl)
    old_author= [ json.loads(author)['userInfo']['user']['uniqueId']   for  author in   old_message]
    old_author2= tool.land_txt('user.txt').split('\n')

    author_all=[]
    sem = asyncio.Semaphore(1)
    for mess in message:
        author_all=author_all+[ author['account']  for author in json.loads(mess)['list']]
    author_all=list(set(author_all)-set(old_author)-set(old_author2))
    print(len(author_all))
    num=2
    author_all_slice=[ author_all[i:i+num]   for i in range(0,len(author_all),num) if len(author_all[i:i+num])==num]
    tasks = [get_video_example(*author_list,num,sem,down_jsonl) for author_list in author_all_slice]
    loop = asyncio.get_event_loop()
    loop.run_until_complete((asyncio.wait(tasks)))
    loop.close()
