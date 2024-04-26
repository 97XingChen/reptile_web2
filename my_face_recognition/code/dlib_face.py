import face_recognition
import cv2 as cv
import matplotlib.pyplot as plt

plt.switch_backend('TkAgg')
def face_detect_demo(img):
    # image = my_face_recognition.load_image_file(img,mode='RGB')
    face_locations = face_recognition.face_locations(img)

    for i in face_locations:
      img1_detect = cv.rectangle(img, (i[1], i[0]), (i[3], i[2]),  (255,0,0),5)
    print(face_locations)
    #输出效果图像
    cv.imshow('result', img)
    return face_locations

cap=cv.VideoCapture(r'E:\new_port\download\n001_00005.mp4')
fps = int(cap.get(cv.CAP_PROP_FPS))
i=0
# face_locations_list=[]

#播放进行读取（一帧一帧的走）
while True:
    s = i / fps
    #flag表示是否在播放（布尔类型）
    flag,frame=cap.read()
    #判断是否在播放
    if not flag:
        break
    # rgb_frame = frame[:, :, ::-1]
    face_locations=face_detect_demo(frame)
    #输入q的时候进行关闭
    if ord('q') == cv.waitKey(10):
        break
    # face_locations_list.append()




    i=i+1
