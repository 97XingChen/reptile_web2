import jsonlines


def down_jsonlines(path,dict):
    with jsonlines.open(path, mode='a') as writer:
        writer.write(dict)


def land_jsonlines(path: object) -> object:
    with open(path, mode='r', encoding="utf-8") as writer:
        temp = set(writer.readlines())
    return temp

def down_txt(path,str):
    with open(path, mode='a', encoding="utf-8") as f:
        f.write('\n'+str)

def land_txt(path):
    with open(path, mode='r', encoding="utf-8") as f:
        temp=f.read()
    return temp

categoryid={
            '101':'表演',
        '102':'音乐',
        '103':'动物',
        '104':'二次元',
        '105':'户外活动',
        '106':'解压',
        '107':'科学教育',
        '108':'美妆',
        '109':'日常生活',
        '110':'时尚',
        '111':'美食菜谱',
        '112':'运动',
        '113':'健身',
        '114':'旅游',
        '115':'舞蹈',
        '116':'DIY',
        '117':'家庭育儿',
        '118':'游戏',
        '119':'健康',
        '120':'家居园艺',
        '121':'恋爱',
        '122':'流行文化',
        '123':'职业',
        '124':'专业发行人',
        '125':'艺术',
        '126':'车子',
        '127':'名人',
        '128':'搞笑',
        '129':'摄影',
}