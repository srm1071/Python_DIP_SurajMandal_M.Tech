# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 20:53:58 2021

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
            
    print(p1)
    print(p2)
    print(t1)
    print(p3)
    return(imag,p1,p2,t1,p3)
    
def writefile(img,t1,t2,t3,t4):
    im=open("images\lenabit.pgm","w")
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



img,p1,p2,t1,p3=readfile("images\lena.pgm")
#img=cv2.imread('images\camera.jpg',0)
# img=cv2.resize(img,(230,230))

dimension=img.shape
print(dimension)
height=img.shape[0]
width=img.shape[1]

     
b1=np.zeros((height,width),np.int) 
b2=np.zeros((height,width),np.int)
b3=np.zeros((height,width),np.int)
b4=np.zeros((height,width),np.int)
b5=np.zeros((height,width),np.int)
b6=np.zeros((height,width),np.int)
b7=np.zeros((height,width),np.int)   
b8=np.zeros((height,width),np.int) 

imag=0
for i in range(height):
    for j in range(width):
        b9=np.zeros((9),np.int)
        bin=0     
        imag=img[i,j]
        while(bin<8):
            b9[bin]=imag%2
            imag=imag/2
            bin=bin+1
            
            
        b1[i][j]=b9[0]
        b2[i][j]=2*b9[1]
        b3[i][j]=4*b9[2]
        b4[i][j]=8*b9[3]
        b5[i][j]=16*b9[4]
        b6[i][j]=32*b9[5]
        b7[i][j]=64*b9[6]
        b8[i][j]=128*b9[7]


imag1=writefile(b5,p1,p2,t1,p3)


