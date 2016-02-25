#coding:utf-8
'''
Created on 2016年2月25日

@author: wlq
'''
from selenium import webdriver
import os,time

driver = webdriver.Chrome()

file_path =  'file:///' + os.path.abspath(os.path.join(os.getcwd(), os.pardir+'/html/upload_file.html'))
driver.get(file_path)
print file_path

driver.find_element_by_name("file").send_keys(os.path.abspath('test.html'))

time.sleep(20)
driver.quit()