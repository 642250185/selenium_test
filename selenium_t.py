import time, json
# 从selenium 里面导入webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 创建Chrome对象
driver = webdriver.Chrome()

# 操作这个对象
driver.get("https://www.baidu.com")

# 获取输入框
inputID = driver.find_element_by_id("kw")
inputID.clear()

# 获取title
print("title: ", driver.title)

# 在输入框输入搜索内容
inputID.send_keys(u"自动化测试")

# Ctrl + a 全选输入内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'a')

# Ctrl + x 剪切输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'x')

# 清除输入框内容
driver.find_element_by_id("kw").clear()

# 输入框重新输入内容
driver.find_element_by_id("kw").send_keys("迷人的万茜")

# 单击搜索按钮
driver.find_element_by_id("su").click()

# 生成快照
driver.save_screenshot("baidu_1.png")

# 获取当前url
current_url = driver.current_url
print("current_url: ", current_url)

# 获取当前页面的cookie
cookies = driver.get_cookies()
print("cookies: ", cookies)

time.sleep(2)
driver.quit()














































