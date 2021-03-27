import numpy as np
import cv2
from matplotlib import pyplot as plt


def readfile(image):
    img1=open(image,"r")
    p1=img1.readline()
    p2=img1.readline()
    t1=img1.readline()
    p3=img1.readline()
    width,height=[int(i) for i in t1.split()]
    imag=np.zeros((height,width), dtype=np.uint8)
    for i in range(height):
        for j in range(width):
            imag[i,j]=img1.readline()
            
    return(imag,p1,p2,t1,p3)

def writefile(img,t1,t2,t3,t4):
    im=open("images\lenaneg.pgm","w")
    im.write("%s"%t1)
    im.write("%s"%t2)
    im.write("%s"%t3)
    im.write("%s"%t4)
    h=img.shape[0]
    w=img.shape[1]
    
    for i in range(h):
        for j in range(w):
            im.write("%d\n"%img[i,j])

    im.close()
    
img,p1,p2,t1,p3=readfile('images\lena.pgm')
im1=np.array(img)

dimension=im1.shape
print(dimension)
height=im1.shape[0]
width=im1.shape[1]
maximum=np.amax(im1)

imag=np.zeros((height,width), dtype=np.uint8)

for i in range(0,height):
    for j in range(0,width):
            imag[i][j]=maximum-im1[i][j]
        

imag1=writefile(imag,p1,p2,t1,p3)

