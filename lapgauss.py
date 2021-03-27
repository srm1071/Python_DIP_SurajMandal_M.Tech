# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 07:58:11 2021

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
    im=open("images\lena4.pgm","w")
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
mask=np.zeros((3,3), dtype=np.uint8)

mask=np.array([[-1,-1,-1],
      [0,0,0],
      [1,1,1]])
mask1=np.array([[-1,0,1],
      [-1,0,1],
      [-1,0,1]])

mask3=np.array([[0,-1,0],
      [-1,4,-1],
      [0,-1,0]])

mask4=np.zeros((3,3), dtype=np.float)
imag=np.zeros((height,width), dtype=np.uint8)
imag1=np.zeros((height,width), dtype=np.uint8)
sgsq=0.5

for i in range(1,height-1,1):
    for j in range(1,width-2,1):
        imag[i,j]=(img[i-1, j-1]*mask3[0, 0]+img[i-1, j]*mask3[0, 1]+img[i-1, j + 1]*mask3[0, 2]+img[i, j-1]*mask3[1, 0]+ img[i, j]*mask3[1, 1]+img[i, j + 1]*mask3[1, 2]+img[i + 1, j-1]*mask3[2, 0]+img[i + 1, j]*mask3[2, 1]+img[i + 1, j + 1]*mask3[2, 2])


for i in range(3):
    for j in range(3):
        #t1=((mask[i,j]**2)+(mask1[i,j]**2)-(2*sgsq))/(sgsq**2)
        t1=1/(2*3.14*sgsq)
        t2=(math.exp((-(mask[i,j]**2)+(mask1[i,j]**2))/(2*sgsq)))
        t3=(t1*t2)
        print(t3)
        mask4[i,j]=t3
        
print(mask4)
        
for i in range(1,height-1,1):
    for j in range(1,width-2,1):
        imag1[i,j]=abs(imag[i-1, j-1]*mask4[0, 0]+imag[i-1, j]*mask4[0, 1]+imag[i-1, j + 1]*mask4[0, 2]+imag[i, j-1]*mask4[1, 0]+ imag[i, j]*mask4[1, 1]+imag[i, j + 1]*mask4[1, 2]+imag[i + 1, j-1]*mask4[2, 0]+imag[i + 1, j]*mask3[2, 1]+imag[i + 1, j + 1]*mask3[2, 2])

        


imag1=writefile(imag1,p1,p2,t1,p3)
print(imag1)
#img3 = cv2.hconcat([img,imag1])
cv2.imshow('image',imag1)