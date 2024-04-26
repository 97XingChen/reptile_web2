from modelscope.pipelines import pipeline
from modelscope.utils.constant import  Tasks
import numpy as np

fer = pipeline(Tasks.facial_expression_recognition, 'damo/cv_vgg19_facial-expression-recognition_fer')
img_path = r'C:\Users\PC\Desktop\未提交的\db0007\db0007-1.jpg'
ret = fer(img_path)
label_idx = np.array(ret['scores']).argmax()
label = ret['labels'][label_idx]

print(f'facial expression : {label}.')