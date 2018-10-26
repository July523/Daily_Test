# coding=utf-8

import urllib.request

from bs4 import BeautifulSoup


def __fetch_content(self):
    print(url)
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
    }
    # 网站反爬虫，构造合理的http要求
    request = urllib.request.Request(url, headers=header)

    # 爬取网站内容
    r = urllib.request.urlopen(request).read()
    soup = BeautifulSoup(r)

    # 找到主播的房间号

    name = soup.findAll("span", attrs={"class": 'tag ellipsis'})
    link = soup.findAll("a", attrs={"class": 'play-list-link'})

    for i in range(0, 50):

        print(name[i].string)
        print("http://www.douyu.com" + link[i].get("href"))
        print("-----------------")

        # 保存文本
        with open('D:\\douyu.txt', mode='a', encoding='utf-8')as jb:
            jb.write(name[i].string)
            jb.write("\n")
            jb.write("https://www.douyu.com" + link[i].get("href"))
            jb.write("\n")
            jb.write("\n")


if __name__ == "__main__":
    url = "https://www.douyu.com/g_wzry"
    __fetch_content(url)