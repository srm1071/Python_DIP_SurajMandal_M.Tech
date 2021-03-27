# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 21:26:37 2021

@author: suraj
"""
import numpy as np
import cv2
from matplotlib import pyplot as plt
import math  

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
    im=open("images\camera_sobel.pgm","w")
    im.write("%s"%t1)
    im.write("%s"%t2)
    im.write("%s"%t3)
    im.write("%s"%t4)
    h=img.shape[0]
    w=img.shape[1]
    
    for i in range(h):
        for j in range(w):
            im.write("%d\n"%img[i,j])
    return(img)
    im.close()

img,p1,p2,t1,p3=readfile("images\camera.pgm")
#img=cv2.imread('images\camera.jpg',0)
# img=cv2.resize(img,(230,230))

dimension=img.shape
print(dimension)
height=img.shape[0]
width=img.shape[1]
mask=np.zeros((3,3), dtype=np.uint8)

mask1=np.array([[-1,0,1],
      [-2,0,2],
      [-1,0,1]])

mask2=np.array([[-1,-2,-1],
      [0,0,0],
      [1,2,1]])

imag=np.zeros((height,width), dtype=np.uint8)


for i in range(0,height-1,1):
    for j in range(0,width-1,1):
        t1=(img[i-1, j-1]*mask1[0, 0]+img[i-1, j]*mask1[0, 1]+img[i-1, j + 1]*mask1[0, 2]+img[i, j-1]*mask1[1, 0]+ img[i, j]*mask1[1, 1]+img[i, j + 1]*mask1[1, 2]+img[i + 1, j-1]*mask1[2, 0]+img[i + 1, j]*mask1[2, 1]+img[i + 1, j + 1]*mask1[2, 2])
        t2=(img[i-1, j-1]*mask2[0, 0]+img[i-1, j]*mask2[0, 1]+img[i-1, j + 1]*mask2[0, 2]+img[i, j-1]*mask2[1, 0]+ img[i, j]*mask2[1, 1]+img[i, j + 1]*mask2[1, 2]+img[i + 1, j-1]*mask2[2, 0]+img[i + 1, j]*mask2[2, 1]+img[i + 1, j + 1]*mask2[2, 2])
        imag[i,j]=abs(math.sqrt((t1**2)+(t2**2)))



imag1=writefile(imag,p1,p2,t1,p3)
img3 = cv2.hconcat([img,imag1])
cv2.imshow('image',img3)