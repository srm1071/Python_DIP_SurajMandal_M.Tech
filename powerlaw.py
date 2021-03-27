# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 17:08:09 2021

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
    im=open("images\camera_power.pgm","w")
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

def plotgraph(a1,a2):
    x=len(a1)
    print(x)
    imag1=np.zeros((256,256), dtype=np.uint8)
    for i in range(x):
            p=a1[i]
            q=a2[i]
            imag1[p][q]=255      
            
    print(imag1)        
    return(imag1)

arr1=[]
arr3=[] 
img,p1,p2,t1,p3=readfile('images\camera.pgm')

dimension=img.shape
height=img.shape[0]
width=img.shape[1]
imag1=np.zeros((height,width), dtype=np.uint8)
imag2=np.zeros((height,width), dtype=np.uint8)

for i in range(0,height,1):
    for j in range(0,width,1):
            imag2[i][j]=(255*(img[i][j]/255)**2.2)
            arr1.append(img[i][j])
            arr3.append(imag2[i][j])
       
cv2.imshow('image',imag2)
imag1=writefile(imag2,p1,p2,t1,p3)
imag3=plotgraph(arr1,arr3)
cv2.imshow('image',imag1)
