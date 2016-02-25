# -*- coding: utf-8 -*-'
'''
Created on 2016年2月25日

@author: wlq
'''

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import os

dr = webdriver.Chrome()
#file_path =  'file:///' + os.path.abspath('test.html')
file_path =  'file:///' + os.path.abspath(os.path.abspath(os.path.join(os.getcwd(), os.pardir+'/html/test.html')))
dr.get(file_path)
time.sleep(2)
dr.refresh()
time.sleep(2)
dr.refresh()
#点击Link1链接（弹出下拉列表）
dr.find_element_by_link_text('Link1').click()
time.sleep(5)
#找到id 为dropdown1的父元素
WebDriverWait(dr, 30).until(lambda the_driver: the_driver.find_element_by_id('dropdown1').is_displayed())
#在父亲元件下找到link为Action的子元素
menu = dr.find_element_by_id('dropdown1').find_element_by_link_text('Action')

#鼠标定位到子元素上
webdriver.ActionChains(dr).move_to_element(menu).perform()

time.sleep(2)
print "okk"

dr.quit()