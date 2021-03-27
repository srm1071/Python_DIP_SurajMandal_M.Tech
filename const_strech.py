# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 20:52:45 2021

@author: suraj
"""
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
    im=open("images\moon_contrast.pgm","w")
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

arr1=[]
arr2=[] 
img,p1,p2,t1,p3=readfile('images\moon.pgm')
max=np.amax(img)
min=np.amin(img)

dimension=img.shape
print(dimension)
height=img.shape[0]
width=img.shape[1]
im1=np.zeros((height,width), dtype=np.uint8)

mint=5
maxt=250

for i in range(0,height,1):
    for j in range(0,width,1):
            im1[i][j]=(img[i][j]-min)*((maxt-mint)/(max-min))+mint


imag1=writefile(im1,p1,p2,t1,p3)
cv2.imshow('image',imag1)