


from selenium import webdriver




class Lagou:

    def __init__(self):
        
        # 准备全局变量
        self.data = list()
        self.isEnd = False

        # 启动浏览器，初始化浏览器
        opt = webdriver.chrome.options.Options()        
        opt.set_headless()

        self.driver = webdriver.Chrome(chrome_options=opt)
        # self.wait = WebDriverWait(self.driver, 10)

        # 打开起始 URL
        self.position = input("请输入职位：")
        # self.driver.get('https://www.lagou.com/jobs/list_' + urllib.parse.quote(self.position) + '?labelWords=&fromSearch=true&suginput=')

        # 设置cookie
        cookie = input('请输入cookie: ')
        for item in cookie.split(";"):
            k, v = item.strip().split('=')
            print('k: ', k, 'v: ', v)
            self.driver.add_cookie({'name':k, 'value': v})


        pass

    def parse_page(self):
        """爬取网页数据"""
        pass

    def turn_page(self):
        """进行翻页操作"""
        pass

    def crawl(self):
        """爬取数据，调用parse_page 和 turn_page"""
        pass

    def save(self):
        """保存数据, 将数据保存到文件中"""
        pass

    def draw(self):
        """数据可视化"""
        pass

if __name__ == "__main__":
    
    pass