import re
import ssl
import time
import json
import urllib3
import requests
import datetime
import urllib.parse
from lxml import etree
ssl._create_default_https_context = ssl._create_unverified_context


class FixednessIpProxy(object):

    def __init__(self):

        # 禁用安全请求警告
        urllib3.disable_warnings()

        # 第三方代理服务商
        self.proxies = self.__proxy_dobel_t3()

        pass

    def download(self, file_name):

        url = "https://api.huishoubao.com/api/product/getProductList?classId=1&brandId=2&pageIndex=1&pageSize=20&pid=1004&token=&platform=5&appkey=&timestamp=1594779597&uuid=C04764BE94504DDE807DA30D0EE4172B&version=1&sign=090fffc3809cf9230108676ef98d77457bf09093"

        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Connection": "closed",
            "Host": "api.huishoubao.com",
            "Origin": "https://mobile.huishoubao.com",
            "Referer": "https://mobile.huishoubao.com/hsbh5/products?pid=1004",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
        }

        try:

            # verify 是否验证服务器的SSL证书
            res = requests.get(url=url, headers=headers, proxies=self.proxies, verify=False)
            print("res.status_code: %d" % res.status_code)
            if res.status_code == 200:

                file_path = "./download/{}".format(file_name)
                print("文件存储路径, file_path: %s" % file_path)
                # 写入文件 encoding="utf-8" 处理中文乱码问题
                with open(file_path, 'w', encoding="utf-8") as fs:
                    # 写入文件
                    fs.write(res.text)
                    # 关闭文件流
                    fs.close()
                    print("文件下载完成, file_name: %s" % file_name)

            else:
                print("请求失败, res.status_code: %d" % res.status_code)
        except Exception as e:
            print("error: %s" % e)
        finally:
            print("end..............")
        pass

    def readfile(self, file_name):

        file_path = "./download/{}".format(file_name)
        fs = open(file_path, 'r')
        try:
            content = fs.read()
            result = json.loads(content)
            return result
        except Exception as e:
            print("readfile error: %s" % e)
            fs.close()
        finally:
            fs.close()

    def __proxy_dobel_t3(self):
        '''
        多贝云代理 套餐三 并发数 10
        无IP限制，每次请求都是随机IP
        :return:
        '''
        dby_proxy_user = 'HSBHSBHEG7M3SR0'
        dby_proxy_pass = 'wkonknYU'
        dby_proxy_host = 'http-proxy-t3.dobel.cn'
        dby_proxy_port = 9180
        proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
            "host": dby_proxy_host,
            "port": dby_proxy_port,
            "user": dby_proxy_user,
            "pass": dby_proxy_pass,
        }
        proxies = {"http": proxyMeta, "https": proxyMeta}
        return proxies

    def verify_ip(self):

        url = "http://ip.webmasterhome.cn/"

        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Cache-Control": "max-age=0",
            "Connection": "closed",
            "Cookie": "ASPSESSIONIDQSCADCTQ=IPJGKPDDJCKJHFOILMFJKLPD; __51cke__=; __gads=ID=92ddde72f374c116:T=1594795140:S=ALNI_MZuaRTyeBivzO36Ci8ITyet2Y0jrA; ipActC=uW4HpsTeY; __tins__212346=%7B%22sid%22%3A%201594795139912%2C%20%22vd%22%3A%204%2C%20%22expires%22%3A%201594797335129%7D; __51laig__=4",
            "Host": "ip.webmasterhome.cn",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
        }

        try:

            # 测试固定IP
            proxies = {'https': '123.139.56.238:9999', 'http': '123.139.56.238:9999'}

            res = requests.get(url=url, headers=headers, proxies=self.proxies, timeout=15)
            print("res.status_code: %d" % res.status_code)

            tree = etree.HTML(res.text)
            ip = tree.xpath(".//span[@id='ipaddr']/a/@title")[0]
            print("IP: %s" % ip)

        except Exception as e:
            print("error: %s" % e)
        finally:
            print("end .............")

        pass

    pass

if __name__ == "__main__":
    # fixednessipproxy = FixednessIpProxy()

    # file_name = "business_1.json"

    # fixednessipproxy.download(file_name)
    # content = fixednessipproxy.readfile(file_name)

    # print("content: %s" % content)

    # language = '<a href="http://www.amazon.ca/gp/product/B078KF8CSX/ref=ag_xx_cont_xx" target="ASINWindow">B078KF8CSX</a>'
    #
    # language = 1
    #
    # flag = language.index(">")
    # print("flag: %d" % flag)
    #
    # start_index = language.index(">")
    # end_index = language.index("</")
    # child_str = language[start_index+1: end_index]
    # print("child_str: %s" % child_str)

    # s = '%E5%B9%BF%E5%B7%9E'
    # s = "%2Fc0%2Fc1%2Fc2%2Fc3%2Fc4%2Fc5%2Fc6%2Fc7%2Fc8%2Fc9%2Fc10%2Fc11%2Fc12%2Fc13%2Fc14%2Fc15%2Fc16"
    # s = urllib.parse.unquote(s)
    # print(s)
    #
    # # ss = '长春'
    # ss = "/c0/c1/c2/c3/c4/c5/c6/c7/c8/c9/c10/c11/c12/c13/c14/c15/c16"
    # ss = urllib.parse.quote(ss)
    # print(ss)

    # t = time.time()
    # timestamp = int(round(t * 1000))
    # print(timestamp)    # 毫秒级时间戳

    # t_str = "04/01/2020"
    # t_str_2 = "2020-04-01"
    # ts = urllib.parse.quote(t_str)
    #
    # time_arr = t_str_2.split("-")
    # print("time_arr: %s" % time_arr)
    #
    # now_time = "{}%2f{}%2f{}".format(time_arr[1], time_arr[2], time_arr[0])
    # print("now_time: %s" % now_time)
    #
    #
    # print("ts: %s" % ts)

    now_time = datetime.datetime.now().strftime('%Y-%m-%d')
    print(now_time)


    today = datetime.datetime.now()
    offset = datetime.timedelta(days=-2)
    re_date = (today + offset).strftime('%Y-%m-%d')
    print("re_date: %s" % re_date)












