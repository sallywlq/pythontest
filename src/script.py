#coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://mail.163.com/")

#给用户名的输入框标红
js="var q=document.getElementById(\"idInput\");q.style.border=\"1px solid red\";"
#调用js
driver.execute_script(js)
time.sleep(3)

driver.find_element_by_id("idInput").send_keys("mmgg0108")
driver.find_element_by_id("pwdInput").send_keys("mmgg123456")
driver.find_element_by_id("loginBtn").click()
time.sleep(3)

driver.quit()