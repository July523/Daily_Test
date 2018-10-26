# coding=utf-8
import requests
from bs4 import BeautifulSoup
import xlwt
import re

book = xlwt.Workbook()
# 创建表格
sheet = book.add_sheet('sheet1', cell_overwrite_ok=True)


def getHtml():
    url = 'https://www.shixiseng.com/interns?p='
    request = requests.get(url=url)
    respons = request.content  # 得到页面源代码
    soup = BeautifulSoup(respons, 'html.parser')  # 解析源代码
    # 下面是计算岗位列表的页数
    page = soup.select('div#pagebar')[0]
    l = str(page.select('li')[-1].a.attrs['href'])
    x = re.compile(r'\d{3}')
    y = x.search(l)
    lastpage = int(y.group())
    print(lastpage)
    # 调用函数
    saveData(url, lastpage + 1)


def saveData(url, lastpage):
    row = 0  # 必须定义为全局变量
    for i in range(1, lastpage):
        html = requests.get(url='%s%d' % (url, i)).content
        soup = BeautifulSoup(html, 'html.parser')
        infos = soup.select('div.posi-list')[0].select('div.list')
        # 相关的数据信息
        for info in infos:
            po_name = info.select('div.names.cutom_font')[0].a.text
            part = info.find('a', class_='cutom_font').text
            addr = info.find('div', class_='addr').span.text
            xz = info.find('div', class_='xz').span.text

            # 写入excel
            sheet.write(row, 0, po_name)
            sheet.write(row, 1, part)
            sheet.write(row, 2, addr)
            sheet.write(row, 3, xz)
            row += 1


if __name__ == '__main__':
    getHtml()
    book.save('shixiseng.xls')
