from selenium import webdriver
import time

driver = webdriver.Chrome('/Users/renxiaogang/Documents/chromedriver')  # 设置chrome浏览器驱动器路径
driver.fullscreen_window()  # 最大化窗口
driver.get('http://www.baidu.com')  # 打开指定网页
driver.find_element_by_name('wd').send_keys('北京在哪里\n')  # 找到输入框，并输入关键字
# driver.find_element_by_id('su').click()  # 找到这个ID然后点击一下
driver.back()  # 返回上一页

time.sleep(3)
driver.refresh()
time.sleep(3)

driver.forward()
# driver.find_element_by_link_text('百度首页').click()  # 点击链接显示的名字
# time.sleep(3)
driver.quit()  # 退出
