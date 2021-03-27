# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 20:38:54 2021

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
    im=open("images\camera_hist.pgm","w")
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
    

arr1=[]
hist=[]
pmf=[0]*256
cdf=[]
sum=0
img,p1,p2,t1,p3=readfile('images\camera.pgm')

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


for i in range(0,256):
    pmf[i]=arr1[i]/(256*256)
    sum=sum+arr1[i]
    cdf.append(sum)
    
for i in range(0,256):
     cdf[i]=cdf[i]/65536
     cdf[i]=int(cdf[i]*255)


imag=np.zeros((height,width), dtype=np.uint8)

for k in range(0,256):
    for i in range(0,height,1):
        for j in range(0,width,1):
            if (img[i,j]==k):
                imag[i,j]=cdf[k-1]

writefile(imag,p1,p2,t1,p3)
print(imag)
img3 = cv2.hconcat([img,imag])
cv2.imshow('image',img3)
cv2.imwrite('images\camera_hist.jpg',imag)


cv2.waitKey()
cv2.destroyAllWindows()
