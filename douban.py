import time
from lxml import etree
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Douban(object):

    def __init__(self):
        print("selenium 模拟登陆... ... ..")
        pass

    def auto_login(self):
        # 启动浏览器，初始化浏览器
        chrome_options = Options()

        # 加载渠道
        driver = webdriver.Chrome(options=chrome_options, executable_path='./chromedriver.exe')

        # 目标网站
        url = "https://www.douban.com/"

        # 访问首页
        driver.get(url)

        print("page_source: %s" % driver.page_source)
        time.sleep(4)

        try:
            # 用户名
            username = driver.find_element_by_id("username")
            username.clear()  # 清空用户名框
            username.send_keys("nihao642250185@163.com")  # 输入用户名

            # 密码
            password = driver.find_element_by_id("password")
            password.clear()
            password.send_keys("nihao163")

            # 登陆按钮
            driver.find_element_by_xpath("//div[@class='btn btn-account btn-active']").click()

            # 等待2秒
            time.sleep(3)

            # 生成快照
            with open('douban.html', 'w') as file:
                file.write(driver.page_source.encode("UTF-8"))

            # 关闭driver
            driver.quit()
        except Exception as e:
            print("error: %s" % e)
            driver.quit()
        finally:
            pass
        pass

    pass

if __name__ == "__main__":
    douban = Douban()
    douban.auto_login()









