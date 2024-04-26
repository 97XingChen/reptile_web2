from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks
import cv2
import numpy as np
import os
from datetime import date
import time

def get_mutil_head_mask_image(input_location,save_dir,model_id,is_bridesmaid):

    image_name = os.path.basename(input_location)
    mask_path = f'mask/{save_dir}'
    os.makedirs(mask_path, exist_ok=True)
    head_detection = pipeline(Tasks.domain_specific_object_detection, model=model_id)
    result = head_detection(input_location)
    img = cv2.imread(input_location)

    if is_bridesmaid:
        i=0
        for boxes in result['boxes']:
            mask = np.full((img.shape[0], img.shape[1]), 255, dtype=np.uint8)
            mask[int(boxes[1]):int(boxes[3]),int(boxes[0]):int(boxes[2])] = 0
            pt1 = (int(boxes[0]), int(boxes[1]))  # 左边，上边   #数1 ， 数2
            pt2 = (int(boxes[2]), int(boxes[3])) # 右边，下边  #数1+数3，数2+数4
            cv2.rectangle(img, pt1, pt2, (0, 255, 0), 2)
            cv2.imwrite(os.path.join(mask_path, image_name.replace(".jpg", f"-mask{i}.jpg")), mask)
            i += 1
    else:
        mask = np.full((img.shape[0], img.shape[1]), 255, dtype=np.uint8)
        for boxes in result['boxes']:
            mask[int(boxes[1]):int(boxes[3]),int(boxes[0]):int(boxes[2])] = 0
            pt1 = (int(boxes[0]), int(boxes[1]))  # 左边，上边   #数1 ， 数2
            pt2 = (int(boxes[2]), int(boxes[3])) # 右边，下边  #数1+数3，数2+数4
            cv2.rectangle(img, pt1, pt2, (0, 255, 0), 2)
        cv2.imwrite(os.path.join(mask_path, image_name.replace(".jpg", "-mask.jpg")), mask)


if __name__=="__main__":
    model_id = 'damo/cv_tinynas_head-detection_damoyolo'
    image_dir=r"C:\Users\PC\Desktop\lora"
    save_dir=os.path.basename(image_dir)+'_square'

    skuid_list = os.listdir(image_dir)
    for SKUID in skuid_list:
        skuid_path = os.path.join(image_dir, SKUID)
        image_list = os.listdir(skuid_path)
        for image in image_list:
            try:
                if 'b' in image:
                    is_bridesmaid = True
                else:
                    is_bridesmaid = False
                image_path_a = os.path.join(skuid_path, image)

                get_mutil_head_mask_image( image_path_a, save_dir,model_id, is_bridesmaid=is_bridesmaid)
                print(image, 'success')
            except Exception as e:
                with open(r'../no_face.txt', 'a') as f:
                    f.write(str(date.today()) + ' ' + image_path_a + '\n')
                print(image, e)
            time.sleep(0.3)
