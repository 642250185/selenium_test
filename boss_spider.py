

import time
from lxml import etree
from crawlab import save_item
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class BossSpider(object):

    # 加载驱动
    # driver_path = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        # Windows版
        # self.driver = webdriver.Chrome(options=chrome_options, executable_path='./chromedriver.exe')
        # Linux版
        self.driver = webdriver.Chrome(options=chrome_options, executable_path='./chromedriver')

        self.url = "https://www.zhipin.com/job_detail/?query=%E4%BC%9A%E8%AE%A1&city=101010100&industry=&position="
        pass

    def parse_list_page(self, source):
        # 每个职位的链接
        tree = etree.HTML(source)
        list_li = tree.xpath('//*[@id="main"]/div/div[2]/ul/li')
        print("type: %s, size: %d" % (type(list_li), len(list_li)))
        for li in list_li:
            # 职位
            post = li.xpath("./div/div/div/div/div/span/a/text()")
            # 薪酬
            salary = li.xpath("./div/div/div/div/div[2]/span/text()")
            # 条件
            condition = li.xpath("./div/div/div/div/div[2]/p/text()")
            # 工龄
            working_age = condition[0]
            # 教育
            education = condition[1]
            # company 公司
            company = li.xpath("./div/div/div[2]/div/h3/a/text()")
            print("post: %s, salary: %s, working_age: %s, education: %s, company:%s " % (post[0], salary[0], working_age, education, company[0]))

            boss_item = {
                "post": post,
                "salary": salary,
                "condition": condition,
                "working_age": working_age,
                "education": education,
                "company": company
            }
            save_item(boss_item)
            pass

        pass

    def run(self):
        # 访问首页
        self.driver.get(self.url)

        # 获取页面信息
        # page_source可以获取页面的所有数据,包括每个职位的链接
        source = self.driver.page_source
        self.parse_list_page(source)
        pass

if __name__ == '__main__':
    spider = BossSpider()
    spider.run()













