import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import data

image = data.camera()

STRIDE = (3,5,7)
rows,cols = image.shape

f, axarr = plt.subplots(1, len(STRIDE))

for i,S in enumerate(STRIDE):
    im_mod = image.copy()
    P = round(S/2)
    for r in range(P,rows,S):
        for c in range(P,cols,S):
            im_mod[r-P:r+P+1,c-P:c+P+1] = np.average(image[r-P:r+P+1,c-P:c+P+1])
    axarr[i].imshow(im_mod);
    axarr[i].set_title('{}x{} average block'.format(S,S))

