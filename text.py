import json
import requests
import io
import base64
from PIL import Image
from io  import BytesIO
import numpy as np
url = "http://127.0.0.1:7860"
from PIL import Image, PngImagePlugin
import cv2
from base64 import b64encode
def myimg2img(image_Load,
              mask_Load,
              inpainting_fill=1,
              inpaint_full_res=0,
              inpainting_mask_invert=1,
              prompt="puppy dog",
              negative_prompt="(deformed iris, deformed pupils, semi-realistic, cgi, 3d, render, sketch, cartoon, drawing, anime, mutated hands and fingers:1.4), (deformed, distorted, disfigured:1.3), poorly drawn, bad anatomy, wrong anatomy, extra limb, missing limb, floating limbs, disconnected limbs, mutation, mutated, ugly, disgusting, amputation, white background, bad-hands-5",
              force_task_id="",
              steps=20,
              width=512,
              height=512,
              seed=-1,
              denoising_strength=0.75,
              cfg_scale=7,
              batch_size=1,
              n_iter=1,
              sampler="DPM++ 2M Karras",
              sd_model_checkpoint="epicphotogasm_v4One4All.safetensors [797dab5e63]",

              ):
    payload = {
        "init_images":image_Load,
        "mask":mask_Load,
        "prompt": prompt,
        "negative_prompt":negative_prompt,
        "force_task_id":force_task_id,
        "steps": steps,
        "height":height,
        "width":width,
        "n_iter":n_iter,
        "batch_size":batch_size,
        "seed":seed,
        "cfg_scale": cfg_scale,
        "inpainting_mask_invert": inpainting_mask_invert,
        "denoising_strength": denoising_strength,
        "inpainting_fill": inpainting_fill,
        "inpaint_full_res": inpaint_full_res,
        "sampler_name":sampler,
        "override_settings": {"sd_model_checkpoint": sd_model_checkpoint},
        "alwayson_scripts": {
            "ControlNet":{
                        "args":[{ "input_image": image_Load,
                                  "module": "seg_ofcoco",
                                  "model": "control_v11p_sd15_seg [e1f51eb9]",
                                  "weight": 0.3,
                                }]
            }
        }
    }
    response = requests.post(url=f'{url}/sdapi/v1/img2img', json=payload)
    r = response.json()

    return r


def cv_imread(filePath):
    cv_img=cv2.imdecode(np.fromfile(filePath,dtype=np.uint8),-1)
    ## imdecode读取的是rgb，如果后续需要opencv处理的话，需要转换成bgr，转换后图片颜色会变化
    ##cv_img=cv2.cvtColor(cv_img,cv2.COLOR_RGB2BGR)
    return cv_img

def readImage(path):
    img =cv_imread(path)
    retval, buffer = cv2.imencode('.jpg', img)
    b64img = b64encode(buffer).decode("utf-8")
    return b64img




def im_2_b642(image):
    img = cv_imread(image)
    retval, bytes = cv2.imencode('.png', img)

    encoded_image = base64.b64encode(bytes).decode('utf-8')
    return encoded_image

def people(force_task_id, image_path, mask_path, prompt):

    image_Load=readImage(image_path)
    mask_Load=readImage(mask_path)

    result_images=myimg2img(
                image_Load=image_Load
                ,mask_Load=mask_Load
                ,prompt=prompt
                , width=1000
                , height=800
   )

    return result_images

task_id='11011010'
image_path=r"C:\Users\PC\Desktop\florm_陈\艳丽\bd18055bd0051\bd18055bd0051-1-f012.jpg"
mask_path=r"C:\Users\PC\Desktop\florm_陈\艳丽\bd18055bd0051\bd18055bd0051-1-f012_bmask.png"
prompt="girl，garden，smile，high quality, ultra-realistic"

people(task_id,image_path,mask_path,prompt)









