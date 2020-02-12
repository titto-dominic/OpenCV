import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
# %matplotlib inline
DATADIR="/home/titto/Documents/PetImages"
CATEGORIES=["Dog","Cat"]
for category in CATEGORIES:
    path=os.path.join(DATADIR,category)
    for img in os.listdir(path):
        img_array=cv2.imread(os.path.join(path,img),cv2.IMREAD_GRAYSCALE)
        plt.imshow(img_array,cmap="gray")
        plt.show()
        break
    break