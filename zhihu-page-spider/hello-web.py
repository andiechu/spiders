# -*- coding: utf-8 -*-

""" A Hello-World to web spider """

__author__ = 'Andie Chu'

import urllib.request as urllib2
import urllib.parse


def fetch_page():
    resp = urllib2.urlopen('http://www.baidu.com')
    with open('./hello-resp.html', 'w') as f:
        f.write(str(resp.read(), 'utf-8'))

def fetch_with_params():
    url = 'http://www.zhihu.com/login/email'
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4)"
    referer = 'https://www.zhihu.com/question/29372574'
    headers = {
        'User-agent': user_agent,
        'Referer': referer
    }
    data = {
        'email': 'aaa@163.com',
        'password': '123456',
        'remember_me': True
    }
    b_data = bytes(urllib.parse.urlencode(data, encoding = 'utf-8'), 'utf-8')

    req = urllib2.Request(url, b_data, headers = headers, method='POST')
    resp = urllib2.urlopen(req)

    with open('./hello-params.html', 'w') as f:
        f.write(str(resp.read(), 'utf-8'))

if __name__ == '__main__':
    fetch_with_params()