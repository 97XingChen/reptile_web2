import os
import tool
import json
import shutil
import pandas as pd
shopify_picture_path='E:\shopify_picture_lable'

picture_label=tool.land_jsonlines(r'picture_label.jsonl')
picture_label_data=pd.DataFrame([ json.loads(lines)  for lines in picture_label ])

def move_none_sku():
    for shop in os.listdir(shopify_picture_path):
        shop_path=os.path.join(shopify_picture_path,shop)
        for sku in os.listdir(shop_path):
            sku_path=os.path.join(shop_path,sku)
            if len(os.listdir(sku_path))<1:
                print(print(sku_path),shutil.rmtree(sku_path))


def get_tile_lable(picture_label_data):
    sku_list=[]
    for shop in os.listdir(shopify_picture_path):
        shop_path=os.path.join(shopify_picture_path,shop)
        sku_list=os.listdir(shop_path)+sku_list
    return picture_label_data[picture_label_data['id'].isin(sku_list)]


def del_false_pictyre():
    fasle_picture_str=tool.land_jsonlines('Fasle.jsonl')
    fasle_picture_json=[json.loads(fasle_picture)   for   fasle_picture in  fasle_picture_str]
    fasle_picture_list=[  fasle_picture['image_path'] for fasle_picture in fasle_picture_json  if 'cannot identify image' in  fasle_picture['Exception'] ]
    for fasle_picture in fasle_picture_list:
        try:
            print( fasle_picture, os.remove(fasle_picture))
        except Exception as e:
            pass
# get_tile_lable(picture_label_data).to_excel('E:\shopify_picture_lable\sku_title.xlsx',index=False)
# move_none_sku()
# del_false_pictyre()







