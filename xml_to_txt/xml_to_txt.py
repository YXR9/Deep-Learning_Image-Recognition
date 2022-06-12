#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 22:59:49 2020

@author: kao
"""


import xml.etree.ElementTree as XET
import csv
tree = XET.parse('test.xml')  # 以XET套件載入XML檔案
root = tree.getroot()         # 取得XML表格 

# In[3]


with open('output.txt', 'a', newline='') as f:
    for member in root.findall('object'):
        for i in member.findall('bndbox'):
            temp_weight = int(i[2].text) - int(i[0].text)
            temp_height = int(i[3].text) - int(i[1].text)
            temp_sent = "tooth {} {} {} {}\n".format(i[0].text, i[1].text, temp_weight, temp_height)
            print("{}, {}, {} , {}".format(i[0].text, i[1].text, temp_weight, temp_height))
            f.write(temp_sent)
    f.close()
