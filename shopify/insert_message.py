import pandas as pd
import tool
import json
import re
import os
import shutil
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks
import cv2
import numpy as np
import os
from datetime import date
import time
import json

def get_data():
    shopify_picture=tool.land_jsonlines('shopify.jsonl')
    shopify_data = pd.DataFrame([ json.loads(sku)   for sku in shopify_picture ])
    return shopify_data

def getkey():
    keyword_data=pd.read_excel('女装网站整理.xlsx',sheet_name="Sheet2")
    keyword_list=keyword_data['keys'][keyword_data['标签']==1].to_list()
    keywords='|'.join(keyword_list)
    return keywords


def land_model(model_id):
    head_detection = pipeline(Tasks.domain_specific_object_detection, model=model_id,num_workers=2)
    return head_detection


def Match_the_words(word_to_match,text):
    pattern = r"\b(" + word_to_match + r")\b"
    matches = re.findall(pattern, text, re.IGNORECASE)
    return matches

def picture_label():
    shopify_picture_path = r'E:\shopify_picture'
    picture_path_list=tool.land_jsonlines('picture_label.jsonl')
    picture_path=[   json.loads(picture)   for  picture   in  picture_path_list]
    sku_list=[ os.path.join(shopify_picture_path,picture['Store'],picture['id']) for  picture   in  picture_path ]
    return sku_list


def copy_picture():
    sku_list = list(set(picture_label()))
    i = 0
    for sku in sku_list:
        Store = sku.split("\\")[-2]
        skuid = sku.split("\\")[-1]

        try:
            shutil.copytree(sku, os.path.join(shopify_picture_tan, Store, skuid))
        except Exception as e:
            pass
        i += 1
        print(i)


num=1
shopify_picture_tan=r'E:\shopify_picture_lable'
model_id = 'damo/cv_tinynas_head-detection_damoyolo'
#
# # shopify_data=get_data()
head_detection=land_model(model_id)
start_time=time.time()




# for sku in sku_list:
for root, dirs, files in os.walk(shopify_picture_tan):
    for files in files:
        image_path = os.path.join(root, files)
        try:
            result = head_detection(image_path)
            if num%1000==0:
                print(f"一共处理了{num},总共耗时：",time.time()-start_time)
            if len(result['labels'])!=1:
                print(image_path, os.remove(image_path))
            num += 1
        except Exception as e:
            tool.down_jsonlines("Fasle.jsonl", {"image_path": image_path, "Exception": str(e)})





#     try:
#         for image in os.listdir(sku):
#             picture_path=os.path.join(sku,image)
#             result = head_detection(picture_path)
#             if len(result['labels'])!=1:
#                print(picture_path, os.remove(picture_path))
#             if num % 1000 == 0:
#                 print(f"一共处理了{num},总共耗时：", time.time() - start_time,picture_path)
#             num += 1
#     except Exception as e:
#         tool.down_jsonlines("Fasle.jsonl",{"image_path":picture_path,"Exception":str(e)})
#
# print(num)





# def re_get_keywords():
#     for i in range(0,len(shopify_data)):
#         word_to_match=getkey()
#         found=Match_the_words(word_to_match,shopify_data.loc[i,'title'])
#         if len(found)>0:
#             try:
#                 picture_path=os.path.join(os.path.join(shopify_picture_path,shopify_data.loc[i,'Store']),str(shopify_data.loc[i,'id']))
#                 for image in os.listdir(picture_path):
#                     image_path=os.path.join(picture_path,image)
#                     result=head_detection(image_path)
#                     if num%1000==0:
#                         print(f"一共处理了{num},总共耗时：",time.time()-start_time)
#                     if len(result['labels'])!=1:
#                        print(image_path, os.remove(image_path))
#                     num += 1
#             except Exception as e:
#                 tool.down_jsonlines("Fasle.jsonl",{"image_path":image_path,"Exception":str(e)})

            # print(shopify_data.loc[i,'title'],found)
            # tool.down_jsonlines('picture_label.jsonl',{'Store':shopify_data.loc[i,'Store'],'id':str(shopify_data.loc[i,'id']),'title':shopify_data.loc[i,'title'],'lable':found})
#
# print(num)


