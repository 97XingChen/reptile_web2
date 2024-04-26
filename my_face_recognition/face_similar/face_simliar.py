import os
import shutil

import face_recognition
import numpy as np
import sys
import cv2

def display(img):#查看图片
    cv2.imshow("img",img)
    cv2.waitKey()
    cv2.destroyAllWindows()
def getFaceEncoding(src):
    image = face_recognition.load_image_file(src)
    face_locations = face_recognition.face_locations(image)
    img_  = image[face_locations[0][0]:face_locations[0][2],face_locations[0][3]:face_locations[0][1]]
    img_ = cv2.cvtColor(img_, cv2.COLOR_BGR2RGB)
    #display(img_)
    face_encoding = face_recognition.face_encodings(image, face_locations)[0]
    return face_encoding
def simcos(A,B):
    A=np.array(A)
    B=np.array(B)
    dist = np.linalg.norm(A - B) # 二范数
    sim = 1.0 / (1.0 + dist) #
    return sim

def theSamePerson(one_pic,two_pic):
    '''
    给定两张图片，判断是否是同一个人
    '''
    chenglong = face_recognition.load_image_file(one_pic)
    unknown_image = face_recognition.load_image_file(two_pic)
    biden_encoding = face_recognition.face_encodings(chenglong)[0]
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
    results = face_recognition.compare_faces([biden_encoding], unknown_encoding,tolerance=0.35)
    print('results: ',results)
    return results[0]

def main():
    Ori_path=r'C:\Users\PC\Desktop\20231027all_task\glamlora自拍款ai处理(整理好)'
    des_path=r'C:\Users\PC\Desktop\glamlora自拍款ai处理(整理好)\model21'
    skulist=os.listdir(Ori_path)
    src1 = r'C:\Users\PC\Desktop\20231027all_task\glamlora自拍款ai处理(整理好)\td16055td0002\td16055td0002-5.jpg'
    xl1 = getFaceEncoding(src1)
    for skuid in skulist:
        skuid_path=os.path.join(Ori_path,skuid)
        picture_list=os.listdir(skuid_path)
        for picture in picture_list:
            src2=os.path.join(skuid_path,picture)
            try:
                xl2 = getFaceEncoding(src2)
                # face_distances = face_recognition.face_distance([xl1], xl2)
                # theSamePerson(src1,src2)
                value = simcos(xl1, xl2)
                if value > 0.68:
                    shutil.move(skuid_path,os.path.join(des_path,skuid))
                    print(skuid,picture,value)
                    break
                else:
                    # print(skuid,picture,value)
                    pass
            except Exception as e:
                print(skuid,picture,Exception)

# main()