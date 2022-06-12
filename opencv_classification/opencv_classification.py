#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 22:59:16 2020

@author: kao
"""

# https://img.ltn.com.tw/Upload/news/600/2018/05/11/phpywwM4U.jpg
# In[1]
import cv2

import os.path

def detect(filename, cascade_file = "BASIC10/cascade.xml"):
    if not os.path.isfile(cascade_file):
        raise RuntimeError("%s: not found" % cascade_file)

    cascade = cv2.CascadeClassifier(cascade_file)
    image = cv2.imread(filename)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)

    faces = cascade.detectMultiScale(gray,
                                     # detector options
                                     scaleFactor = 1.1,
                                     minNeighbors = 5,
                                     minSize = (24, 24))
    i=0
    with open('detection.txt', 'a', newline='') as f:
        for (x, y, w, h) in faces:
            if i > 10:
                break
            i+=1
            temp=image[y:y+h,x:x+w,:]
            #cv2.imwrite('%s_%d.jpg'%(os.path.basename(filename).split('.')[0],i),temp)
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 4)
            temp_sent2 = "tooth 1 {} {} {} {}\n".format(x, y, w, h)
            f.write(temp_sent2)
        cv2.imwrite("out.jpg", image)


# In[2]
detect('test.jpg')