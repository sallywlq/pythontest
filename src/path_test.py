#coding=utf-8
'''
Created on 2016年2月25日

@author: wlq
'''
import os
currentPathName=os.getcwd() #当前路径
parentPathName =os.path.abspath(os.path.join(currentPathName, os.pardir+'/html/')) #上一级路径
print currentPathName
print os.pardir+'/html/'
print parentPathName
print parentPathName+'/html/'
