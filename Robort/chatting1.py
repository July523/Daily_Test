# coding=utf-8 
# @Time :2019/1/25 11:20

import requests as rq
import time
import random
import string
import urllib
import hashlib

APPKEY = 'ABDEFGH'  # 换成你的APPKEY


def get_sign(data):
    lst = [i[0] + '=' + urllib.parse.quote_plus(str(i[1])) for i in data.items()]
    params = '&'.join(sorted(lst))
    s = params + '&app_key=' + APPKEY
    h = hashlib.md5(s.encode('utf8'))
    return h.hexdigest().upper()


def chat(question):
    url_chat = 'https://api.ai.qq.com/fcgi-bin/nlp/nlp_textchat'
    nonce_str = ''.join(random.sample(string.ascii_letters + string.digits, 16))
    data = {
        'app_id': 1234567890,  # 换成你的app_id
        'time_stamp': int(time.time()),
        'nonce_str': nonce_str,
        'session': '10000',
        'question': question,
    }
    data['sign'] = get_sign(data)
    r = rq.post(url_chat, data=data)
    answer = r.json()['data']['answer']
    return answer


print('你好，请问需要什么帮助？')
while True:
    try:
        print(chat(input()))
    except (KeyboardInterrupt, EOFError, SystemExit):
        # CTRL-C/CTRL-D 中断退出
        break
