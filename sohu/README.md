由于打开搜狐网页是播放元素 点赞 踩 需要渲染
并且如果想要抓取年份等信息元素时需要模拟js点击事件
所以需要使用selenium PHANTOMJS
# selenium 安装使用pip install selenium
# phantomjs 安装使用 
mv phantomjs-2.1.1-linux-x86_64.tar.bz2 /usr/local   
cd /usr/local && tar -jxvf phantomjs-2.1.1-linux-x86_64.tar.bz2
ln -sf /usr/local/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/bin
phantomjs --version
#相关代码
```
from selenium import webdriver
cap = webdriver.DesiredCapabilities.PHANTOMJS
driver = webdriver.PhantomJS(desired_capabilities=cap)
#打开渲染
self.driver.get(response.url)
#点击展开信息按钮
self.driver.find_element_by_class_name("info-arrT").click()
items['name'] = self.driver.find_element_by_xpath('//div[@class="crumbs"]/a[last()]').text
```
参考博客
http://www.jianshu.com/p/3d84afc43d42
http://blog.csdn.net/u013378306/article/details/51841784
