import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import data

image = data.camera()
levels = int(input("Enter the desired number of intensity levels: "))
dev = 255/(levels-1)
newIm = np.round(image/dev)*dev
fig,arr = plt.subplots(1,2)
arr[0].imshow(image)
arr[1].imshow(newIm)
newIm

