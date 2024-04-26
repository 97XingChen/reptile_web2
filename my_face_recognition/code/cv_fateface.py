import cv2 as cv
def face_detect_demo(img):
    #将图片灰度
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    #加载特征数据
    face_detector = cv.CascadeClassifier('haarcascade/haarcascade_frontalface_alt2.xml')
    #进行检测人脸操作(参数也可以不写)
    faces = face_detector.detectMultiScale(gray,1.1,4)
    print(len(faces),faces,'\n')

    for x,y,w,h in faces:
        #画矩形
        cv.rectangle(img,(x,y),(x+w,y+h),color=(0,0,255),thickness=2)
        #画圆
        cv.circle(img,center=(x+w//2,y+h//2),radius=(w//2),color=(0,255,0),thickness=2)
    # 显示图片(这时的照片会一闪而过)
    cv.imshow('result',img)
#读取视频
cap=cv.VideoCapture(r'E:\new_port\download\n001_00001.mp4')
#播放进行读取（一帧一帧的走）
while True:
    #flag表示是否在播放（布尔类型）
    flag,frame=cap.read()
    #判断是否在播放
    if not flag:
        break
    face_detect_demo(frame)
    #输入q的时候进行关闭
    if ord('q') == cv.waitKey(10):
        break

#释放内存
cv.destroyAllWindows()
#释放视频的空间
cap.release()


