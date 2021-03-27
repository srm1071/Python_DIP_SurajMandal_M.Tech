# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 21:46:19 2021

@author: suraj
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt


def readfile(image):
    img1=open(image,"r")
    img1.readline()
    img1.readline()
    t1=img1.readline()
    img1.readline()
    width,height=[int(i) for i in t1.split()]
    imag=np.zeros((height,width), dtype=np.uint8)
    for i in range(height):
        for j in range(width):
            imag[i,j]=img1.readline()
            
    return(imag)

    
def write_hist_text(arr):
    cnt=0
    t=open("images\histo_text.txt","w")
    for cnt in range(256):
        pix=arr[cnt]
        pix=np.sqrt(pix)
        for i in range(int(pix)):
                t.write("*")
        
        if(pix!=0):
            t.write("\n")
            cnt=cnt+1


arr1=[]
hist=[]
img=readfile("images\camera.pgm")

dimension=img.shape
print(dimension)
height=img.shape[0]
width=img.shape[1]
#channel=img.shape[2]


for k in range(0,256):
    hist.append(k)
    count1=0
    for i in range(0,height,1):
        for j in range(0,width,1):
            if (img[i,j]==k):
                count1=count1+1
    arr1.append(count1)


write_hist_text(arr1)

