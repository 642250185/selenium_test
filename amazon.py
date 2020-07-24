
import time
import requests
from lxml import etree
from crawlab import save_item

class AmazonClass(object):

    def __init__(self):

        pass

    def get_list(self):

        url = "https://www.amazon.com/s?k=%E6%8A%95%E5%BD%B1%E4%BB%AA&i=deals-intl-ship&__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&ref=nb_sb_noss_2"

        headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
            "cache-control": "max-age=0",
            "cookie": 'session-id=132-0147845-7026244; session-id-time=2082787201l; sp-cdn="L5Z9:HK"; skin=noskin; ubid-main=130-2268314-5653533; x-wl-uid=1BZcM1Xxkjc3RhKfgiIa11jfjof88AhAJYz1T18X8GghTikXD6B3Ls+3gnOduE9zfhaerZwFLcUA=; session-token=1mjBahMcQH2PKdNRs3+kVNDR9Mo3m+o1kAk5lDb3mNDv0UsyIlJswEyo0AQnq6D7krqktVu6td1QY92cLGC0tM0RTk1aHAUUoVsTjJYGTbuioBjFFvnd7HT//xEhZCwHSfhv73QamKe3jljcZ7q3XBefqcBcTkd0bX+/qFGokpaQngCwOFkWptTdKh+3W9xNEAgvK4hrBxX98cq+FVTmfumsAbsRAhLo26gzQZ6lVMmZUE7lIMlZ80adcQQj+wkNkNsE+tWKQpQ=; lc-main=zh_CN; i18n-prefs=USD; csm-hit=tb:3W2R1T4Y9TQCQ8A5R033+s-RFDGE3KCD60HNQ6PXG28|1594636706586&t:1594636706586&adb:adblk_no',
            "downlink": "10",
            "ect": "4g",
            "referer": "https://www.amazon.com/international-sales-offers/b/ref=gbps_fcr_m-9_475e_wht_1064954?currency=USD&language=zh_CN&node=15529609011&gb_f_deals1=dealStates:AVAILABLE%252CWAITLIST%252CWAITLISTFULL%252CEXPIRED%252CSOLDOUT%252CUPCOMING,sortOrder:BY_SCORE,MARKETING_ID:ship_export,enforcedCategories:679255011&pf_rd_p=5d86def2-ec10-4364-9008-8fbccf30475e&pf_rd_s=merchandised-search-9&pf_rd_t=101&pf_rd_i=15529609011&pf_rd_m=ATVPDKIKX0DER&pf_rd_r=0MGJEHJDMNK7AZKN01CR&ie=UTF8",
            "rtt": "150",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "same-origin",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
        }

        try:
            res = requests.get(url=url, headers=headers)
            print("res.status_code: %d" % res.status_code)
            if res.status_code == 200:
                tree = etree.HTML(res.text)
                list_li = tree.xpath('//div[@data-component-type="s-search-result"]')
                print("type: %s, size: %d" % (type(list_li), len(list_li)))
                for item in list_li:
                    # print("item: %s" % item)
                    index = item.xpath("@data-index")[0]
                    asin = item.xpath("@data-asin")[0]
                    uuid = item.xpath("@data-uuid")[0]
                    print("index: %s, asin: %s, uuid: %s" % (index, asin, uuid))

                    # 描述
                    description = item.xpath('./div/span/div/div/div[2]/div[2]/div/div/div/div/div/h2/a/span/text()')[0]
                    print("description: %s" % description)

                    # 星星
                    star = item.xpath('./div/span/div/div/div[2]/div[2]/div/div/div/div/div[2]/div/span/span/a/i/span/text()')[0]
                    print("star: %s" % star)

                    # 总星星
                    sum_star = item.xpath('./div/span/div/div/div[2]/div[2]/div/div/div/div/div[2]/div/span[2]/a/span/text()')[0]
                    print("sum_star: %s" % sum_star)

                    # 现价
                    now_price = ""
                    try:
                        now_price = item.xpath('./div/span/div/div/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div/a/span/span/text()')[0]
                    except Exception as e:
                        now_price = "未报价"

                    print("now_price: %s" % now_price)

                    # 原价
                    org_price = ""
                    try:
                        org_price = item.xpath('./div/span/div/div/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div/a/span[2]/span/text()')[0]
                    except Exception as e:
                        org_price = "没有原价"

                    print("org_price: %s" % org_price)
                    pass

                    print()
                    save_params = {
                        "index": index,
                        "asin": asin,
                        "uuid": uuid,
                        "desc": description,
                        "star": star,
                        "sum_star": sum_star,
                        "now_price": now_price,
                        "org_price": org_price
                    }
                    # 保存数据
                    save_item(save_params)
                pass
            else:
                print("请求失败! status_code: %d" % res.status_code)
        except Exception as e:
            print("error: %s" % e)
        finally:
            pass

        pass

    pass

if __name__ == "__main__":

    amazonclass = AmazonClass()
    amazonclass.get_list()
















