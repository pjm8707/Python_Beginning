# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 20:35:18 2020

@author: IAN
@brief : QC report scraping
"""



import sys
import os
import logging
import re

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

def GetDataFromFile(f_path, f_mode='r', f_encoding='utf-8') :
    with open(f_path, mode=f_mode, encoding=f_encoding) as file :
        return file.readlines()

def ParseLogData(text_data) :
    idx=0
    fail_cnt=0
    data=list()
    check_idx=-1
    check_md5=[0,0]
    for line in text_data :
        if re.search('^\[[0-9]+\/[0-9]+\]', line) : #first
            check_idx=idx
            check_md5[0]=0
            check_md5[1]=15
            data.append(line)
            idx+=1
            #print(data[idx-1], end="")

        if check_idx == (idx-1) :
            if re.search('^\[RESULT\] SUCCESS', line) :
                del data[idx-1]
                idx-=1
            elif re.search('^\[RESULT\] FAILURE', line) :
                check_idx+=1
                data[idx-1] = data[idx-1] + line
                fail_cnt+=1
            elif re.search('^Unix   :', line):
                data[idx-1] = data[idx-1] + line
            elif re.search('^\[ERROR\]MISMATCH WITH GOLDEN MD5', line):
                check_md5[0]=1
            elif re.search('^ INSNTANCE #0 INTERRUPT TIMEOUT.', line):
                data[idx-1] = data[idx-1] + line

            if 1 == check_md5[0] and 0 < check_md5[1] :
                data[idx-1] = data[idx-1] + line
                check_md5[1]-=1

    return data, fail_cnt

#text_data = GetDataFromFile('test_log_20200308.txt')
#extracted_data, fail_cnt = ParseLogData(text_data)
#for log in extracted_data :
#    print(log, end='')

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
