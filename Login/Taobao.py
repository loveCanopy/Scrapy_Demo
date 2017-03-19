#- * - coding: utf8 -*-
from selenium import webdriver
cap = webdriver.DesiredCapabilities.PHANTOMJS
driver = webdriver.PhantomJS(desired_capabilities=cap)
# driver = webdriver.Firefox()
driver.get("https://login.taobao.com/member/login.jhtml")
driver.find_element_by_xpath('//a[@class="forget-pwd J_Quick2Static"]').click()
driver.find_element_by_id("TPL_username_1").clear()
driver.find_element_by_id("TPL_password_1").clear()
driver.find_element_by_id("TPL_username_1").send_keys("xxxxx")
driver.find_element_by_id("TPL_password_1").send_keys("xxxx")
driver.find_element_by_id("J_SubmitStatic").click()
for item in driver.get_cookies():
	print item
# driver.get_cookies()取得cookie
# cookie = "; ".join([item["name"] + "=" + item["value"] + "\n" for item in driver.get_cookies()])
# print cookie
# 然后带上cookie登录后的页面去请求页面
driver.get("https://buyertrade.taobao.com/trade/itemlist/list_bought_items.htm")
