import requests
from lxml import etree
import urllib3
import time
import threading, threadpool
# from queue import Queue
from Daily_Test.pachong.Dingdian_spider.query_answer import get_proxies

urllib3.disable_warnings()

lock = threading.Lock()


class DingDianSpider:
    def __init__(self):
        s = requests.session()  # 建立爬虫的回话,相当于浏览器的一个页面,在回话里共享header和cookie等数据
        s.verify = False
        s.trust_env = False
        s.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Ch'
                          'rome/64.0.3282.186 Safari/537.36'}
        self.s = s
        self.proxies = {}
        self.base_url = 'https://www.23us.so/'
        self.count = 0  # 统计变更代理服务器次数计数

    def visit_dingdian(self):
        # 这个方法只是用来测试是否能成功访问页面用
        response = self.__spider(self.base_url)
        if response.status_code == 200:
            print('成功访问顶点首页')

    def __spider(self, url):
        """
        爬虫正体,下面用 while 1,主要是防止ip被封,其实顶点网没必要做这一步
        怎么爬都不会封IP,但现在大多数网站都会封IP
        有时候遇到网络拥堵,也可以改变代理IP
        :param url: 只要传入爬取的url,就能给与相应
        :return: response url返回HTML
        """
        while 1:
            try:
                response = self.s.get(url, proxies=self.proxies, timeout=2)
                if response.status_code == 200:
                    break
            except Exception as e:
                print(e)
                self.count += 1
                # get_proxies在上一篇文章获取ip代理池中的一个方法,那里有详细说明和源码
                # 可以直接拿来用,这里不再赘述,感兴趣的小伙伴可以子看看
                self.proxies = get_proxies()  # 如果出问题就改变代理ip
                print(f'第{self.count}次变更代理ip')
                continue
        return response

    def parse_data(self, arg):
        urls = 'https://www.23us.so/list/{}_{}.html'
        pages_url = urls.format(arg, 1)  # 首先访问每类小说的第一页,抓取最大页码数 max_page
        text = self.__spider(pages_url).text
        tree = etree.HTML(text)
        max_page = int(tree.xpath('//div[@id="pagelink"]/a[@class="last"]/text()')[0])
        for page in range(1, max_page + 1):  # 访问同类型小说的不同页面
            url = urls.format(arg, page)
            items_text = self.__spider(url).text  # 对页面进行访问
            items_tree = etree.HTML(items_text)
            noval_list_num = len(items_tree.xpath('//dl[@id="content"]/dd/table/tr[@bgcolor="#FFFFFF"]'))
            print(f'正在爬取{url}')
            for index in range(1, noval_list_num + 1):  # 访问同类型小说同一页面的不同条目
                # 对数据解析很简单,用xpath,规则性很强
                noval_name = items_tree.xpath(f'//tr[@bgcolor="#FFFFFF"][{index}]/td[1]/a/text()')[0]

                # 最新章节注释了,有时会出现[IndexError]错误,debug到错误章节没问题,返回的页面也没问题,
                # 笔者废了九牛二虎之力愣是没找到原因,先注释了吧,哪位大神要是找到原因,请不吝赐教
                # last_chapter=items_tree.xpath(f'//tr[@bgcolor="#FFFFFF"][{index}]/td[2]/a/text()')[0]
                noval_auth = items_tree.xpath(f'//tr[@bgcolor="#FFFFFF"][{index}]/td[3]/text()')[0]
                words = items_tree.xpath(f'//tr[@bgcolor="#FFFFFF"][{index}]/td[4]/text()')[0]
                updata_date = items_tree.xpath(f'//tr[@bgcolor="#FFFFFF"][{index}]/td[5]/text()')[0]
                state = items_tree.xpath(f'//tr[@bgcolor="#FFFFFF"][{index}]/td[6]/text()')[0]
                lock.acquire()  # 这地方加锁很重要,多线程抢资源很容易导致写下的内容混乱.一个线程写的时候,如果其他线程也开始写,就让他们先等着
                with open('noval.txt', 'a+', encoding='utf-8') as f:
                    f.writelines(','.join([noval_name, noval_auth, updata_date, state, words]) + '\n')
                lock.release()
        print('-' * 50, f'第{arg}类小说抓取完毕!')


if __name__ == '__main__':
    t1 = time.time()

    o = DingDianSpider()
    o.visit_dingdian()

    pool = threadpool.ThreadPool(9)  # 设置最大9个线程
    li = [i for i in range(1, 10)]
    tasks = threadpool.makeRequests(o.parse_data, li)  # 先设置任务列表,才能向线程池申请线程
    [pool.putRequest(task) for task in tasks]  # 向线程池申请线程
    pool.wait()  # wait直到所有的线程都执行完毕,主线程才停止

    t2 = time.time()
    print('时间:', t2 - t1)