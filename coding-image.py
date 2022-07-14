import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

FILE_PATH = "data"
for collection in os.listdir(FILE_PATH):
    for image in os.listdir(os.path.join(FILE_PATH, collection)):
        img = cv2.imread(os.path.join(FILE_PATH, collection, image))
        img_code = image.split(".")[0]
        cv2.putText(
            img=img,
            text=str(img_code),
            org=(50, 140),
            fontFace=cv2.FONT_HERSHEY_TRIPLEX,
            fontScale=5,
            color=(0, 0, 0),
            thickness=3,
        )
        cv2.imwrite(os.path.join(FILE_PATH, collection, image), img)
