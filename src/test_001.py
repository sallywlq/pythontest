#coding=utf-8
'''
Created on 2016年2月22日
@author: wlq
'''
import sys,os
import webbrowser
sys.path.append("libs")
from duplicity.path import Path
from __builtin__ import str
print ("hello wlq")
#获取脚本文件的当前路径
def cur_file_dir():
     #获取脚本路径
     path = sys.path[0]
     #判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是py2exe编译后的文件，则返回的是编译后的文件路径
     if os.path.isdir(path):
         return path
     elif os.path.isfile(path):
         return os.path.dirname(path)
#打印结果
print cur_file_dir()

def cur_path():
    path = os.path.abspath('.')
    print path

#cur_path()
url = 'http://www.baidu.com'
webbrowser.open(url)
print webbrowser.get()

import urllib
open('index.txt','w').write(urllib.urlopen('http://www.baidu.com').read()) 

#str = raw_input("Enter your input: ")
#print str

#str1 = input("Enter your input: ")  #input输入时要使用单引号，否则会出现错误
#print str1+"33333333333"



