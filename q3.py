import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import data


image = data.camera()


rows,cols = image.shape
M = cv2.getRotationMatrix2D((cols/2,rows/2),45,1)
dst_45 = cv2.warpAffine(image,M,(cols,rows))

M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
dst_90 = cv2.warpAffine(image,M,(cols,rows))

f, axarr = plt.subplots(1, 2)
axarr[0].imshow(dst_45)
axarr[0].set_title('45 deg rotation')

axarr[1].imshow(dst_90)
axarr[1].set_title('90 deg rotation');