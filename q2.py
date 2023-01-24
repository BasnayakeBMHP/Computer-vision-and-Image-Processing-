import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import data

image = data.camera()

f, axarr = plt.subplots(1, 3)
axarr[0].imshow(cv2.blur(image,(3,3)))
axarr[0].set_title('3x3 kernel')

axarr[1].imshow(cv2.blur(image,(10,10)))
axarr[1].set_title('10x10 kernel')

axarr[2].imshow(cv2.blur(image,(20,20)))
axarr[2].set_title('20x20 kernel');