# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 01:39:23 2019

@author: Anshit Vishwakarma
"""

import cv2
import os
path = 'C:/Users/Anshit Vishwakarma/Desktop/DogCentric Activity dataset/Train' #It should be changed to "Test" or "Validation" 
folder = os.fsencode(path)
for file in os.listdir(folder):
    filename=os.fsdecode(file)
#    print(filename)
    subfolder = os.fsencode(path+"/"+filename)
    for subfile in os.listdir(subfolder):
        subfilename = os.fsdecode(subfile)
        if subfilename.endswith('.avi'): # whatever file types you're using...
#            print(subfilename)
            vidcap = cv2.VideoCapture(path+"/"+filename+"/"+subfilename)
            success,image = vidcap.read()
            count = 0
            success = True
            while success:
                cv2.imwrite("C:/Users/Anshit Vishwakarma/Desktop/DogCentric Activity dataset (Images)/Train/"+filename+"/"+subfilename+"_"+"frame%d.jpg" % count, image)     # save frame as JPEG file
                success,image = vidcap.read()
                print ('Read a new frame: ', success)
                count += 1
                continue


path = 'C:/Users/Anshit Vishwakarma/Desktop/DogCentric Activity dataset/Test' #It should be changed to "Test" or "Validation" 
folder = os.fsencode(path)
for file in os.listdir(folder):
    filename=os.fsdecode(file)
#    print(filename)
    subfolder = os.fsencode(path+"/"+filename)
    for subfile in os.listdir(subfolder):
        subfilename = os.fsdecode(subfile)
        if subfilename.endswith('.avi'): # whatever file types you're using...
#            print(subfilename)
            vidcap = cv2.VideoCapture(path+"/"+filename+"/"+subfilename)
            success,image = vidcap.read()
            count = 0
            success = True
            while success:
                cv2.imwrite("C:/Users/Anshit Vishwakarma/Desktop/DogCentric Activity dataset (Images)/Test/"+filename+"/"+subfilename+"_"+"frame%d.jpg" % count, image)     # save frame as JPEG file
                success,image = vidcap.read()
                print ('Read a new frame: ', success)
                count += 1
                continue
            

path = 'C:/Users/Anshit Vishwakarma/Desktop/DogCentric Activity dataset/Validation' #It should be changed to "Test" or "Validation" 
folder = os.fsencode(path)
for file in os.listdir(folder):
    filename=os.fsdecode(file)
#    print(filename)
    subfolder = os.fsencode(path+"/"+filename)
    for subfile in os.listdir(subfolder):
        subfilename = os.fsdecode(subfile)
        if subfilename.endswith('.avi'): # whatever file types you're using...
#            print(subfilename)
            vidcap = cv2.VideoCapture(path+"/"+filename+"/"+subfilename)
            success,image = vidcap.read()
            count = 0
            success = True
            while success:
                cv2.imwrite("C:/Users/Anshit Vishwakarma/Desktop/DogCentric Activity dataset (Images)/Validation/"+filename+"/"+subfilename+"_"+"frame%d.jpg" % count, image)     # save frame as JPEG file
                success,image = vidcap.read()
                print ('Read a new frame: ', success)
                count += 1
                continue