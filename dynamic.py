# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 09:51:06 2021

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
    im=open("images\moon_log.pgm","w")
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
    
img,p1,p2,t1,p3=readfile('images\moon.pgm')
arr1=[]
arr2=[]
arr3=[] 
#img=cv2.resize(img1,(256,256))
img=np.array(img)
maxi=np.amax(img)

height=img.shape[0]
width=img.shape[1]
imag1=np.zeros((height,width), dtype=np.uint8)
imag2=np.zeros((height,width), dtype=np.uint8)

c= 255/(np.log(1+maxi))

for i in range(0,height,1):
    for j in range(0,width,1):
#        for k in range(0,channel,1):
            imag1[i][j]=c*(np.log(1+img[i][j]))

cv2.imshow('image',imag1)
writefile(imag1,p1,p2,t1,p3)
