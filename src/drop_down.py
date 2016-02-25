#-*-coding=utf-8

from selenium import webdriver

import os,time
from duplicity.globals import select
from selenium.selenium import selenium

driver= webdriver.Chrome()

#file_path =  'file:///' + os.path.abspath('drop_down.html')
file_path = 'file:///' + os.path.abspath((os.pardir+'/html/drop_down.html'))
print file_path
driver.get(file_path)

time.sleep(2)

m=driver.find_element_by_id("ShippingMethod")

m.find_element_by_xpath("//option[@value='10.69']").click()

time.sleep(3)
print m.text




driver.quit()