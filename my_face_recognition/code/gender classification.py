

import logging

# 设置日志级别为ERROR
logging.basicConfig(level=logging.ERROR)

from PIL import Image
import cv2
import numpy as np
from transformers import pipeline

def cv_imread(filePath):
    cv_img=cv2.imdecode(np.fromfile(filePath,dtype=np.uint8),-1)
    ## imdecode读取的是rgb，如果后续需要opencv处理的话，需要转换成bgr，转换后图片颜色会变化
    ##cv_img=cv2.cvtColor(cv_img,cv2.COLOR_RGB2BGR)
    return cv_img
img=cv_imread(r'C:\Users\PC\Desktop\测试\崔岩\f23w237\f23w237-2.jpg')
# image=Image.open(r'C:\Users\PC\Downloads\OIP-C (1).jpg')
mask=cv_imread(r'C:\Users\PC\Desktop\测试\崔岩\f23w237\f23w237-2-mask1.png')
img_face = cv2.add(img, cv2.resize(mask,(img.shape[1],img.shape[0])))

img_face = cv2.resize(img_face,(1800,2400))
image=Image.fromarray(cv2.cvtColor(img_face,cv2.COLOR_BGR2RGB))
# pipe = pipeline("image-classification", model="huggingface/rizvandwiki/gender-classification-2")
# print(pipe(image))
image.save('2.jpg')
image.show()




# import warnings

# warnings.filterwarnings("ignore")
# from modelscope.pipelines import pipeline
# from modelscope.utils.constant import Tasks
#
# fair_face_attribute_func = pipeline(Tasks.face_attribute_recognition, 'damo/cv_resnet34_face-attribute-recognition_fairface')
# src_img_path = r'C:\Users\PC\Desktop\1.jpg'
# raw_result = fair_face_attribute_func(src_img_path)
# print('face attribute output: {}.'.format(raw_result))

#
# from modelscope.pipelines import pipeline
# from modelscope.utils.constant import Tasks
#
# model_id = 'damo/cv_resnet50_pedestrian-attribute-recognition_image'
# pedestrian_attribute_recognition = pipeline(Tasks.pedestrian_attribute_recognition, model=model_id)
# output = pedestrian_attribute_recognition(r'C:\Users\PC\Desktop\1.jpg')
# print(output)