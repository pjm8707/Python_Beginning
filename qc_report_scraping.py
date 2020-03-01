# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 20:35:18 2020

@author: IAN
@brief : QC report scraping
"""



import sys
import os
import logging

#검색할 web page 양이 많으면 파일로 떨구고, 아래 처럼 파일로 넘겨주
#with open("index.html") as fp:
#    soup = BeautifulSoup(fp)

#for web scraping
import requests
from bs4 import BeautifulSoup

formatter = '%(asctime)-15s:%(module)s:%(lineno)d:%(message)s'
logging.basicConfig(stream=sys.stderr, format=formatter, level=logging.DEBUG)
debugLogger = logging.getLogger("user_debug")
debugLogger.setLevel(logging.DEBUG)

def DLOG(*args):
    msg_str=""
    for msg in args:
        msg_str +=str(msg)
    debugLogger.debug(msg_str)

LOG_URL="http://wiki.chipsnmedia.com:8080/"
URL="http://wiki.chipsnmedia.com:8080/display/IRONDOM/2020-01-15_15-13-47_W517_goke_simple_check_X"
LOGIN_DATA = {
    'os_username': 'xxx',
    'os_password': 'xxx'
}

class Web_scraping:
    def __init__(self):
        print("Web scraping class")


def GetLogInfoFromhtml_th(html_data) :
    th_data = []
    b_soup = BeautifulSoup(html_data, 'html.parser')
    for tag in b_soup.select('th[class="confluenceTh tablesorter-header sortableHeader"]') :
        th_data.append(tag.p.text.strip())

    return th_data

def GetLogInfoFromhtml_td(html_data, th_data) :
    idx = 0
    length = len(th_data)
    td_data = []
    b_soup = BeautifulSoup(html_data, 'html.parser')
    for tag in b_soup.select('td[class="confluenceTh confluenceTd"]') :
        #td_data.append(tag.p.text.strip())
        if 0 == idx :
            td_dic = dict()
        print('index : ', idx, 'th_data : ', th_data[idx])
        td_dic[th_data[idx]] =tag.p.text.strip()
        if ('FULL LOG' == tag.p.text.strip()):
            td_dic[th_data[idx]] = tag.p.a.get('href')
        if (length-2 == idx) :
            td_data.append(td_dic)
            idx = 0
        else :
            idx+=1
    return td_data


if __name__ == "__main__":
    try:
        s= requests.Session()
        res = s.post(LOG_URL, data=LOGIN_DATA, verify=False, allow_redirects=False)
    except ConnectionError as e:
        print(e)
        print("connection error")
    finally :
        s.close()

    res.raise_for_status()

    res=s.get(URL)

    req_html= res.text

    print(req_html)
    
    th_data = GetLogInfoFromhtml_th(req_html)
    td_data = GetLogInfoFromhtml_td(req_html, th_data)
