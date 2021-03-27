import numpy as np
import cv2
from matplotlib import pyplot as plt

img=cv2.imread('images\lena.pgm')
im=np.array(img)
im1=255-im[:,:]
cv2.imshow('image',im1)
cv2.waitKey()
cv2.destroyAllWindows()
