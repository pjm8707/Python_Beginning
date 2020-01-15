# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 18:26:24 2020

@author: ian
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


if __name__ == "__main__":
    #DLOG("dir_path %d",1)
    #req_page= requests.get(URL);

    with requests.Session() as s:
        res= s.post(LOG_URL, data=LOGIN_DATA, verify=False, allow_redirects=False);

    res.raise_for_status()
    #redirect_cookie = req.headers['Set-Cookie']
    #redirect_url = req.headers['Location']
    #headers = {"Cookie": redirect_cookie}

    # Location 주소로 Get Request 호출
    res=s.get(URL)

    req_html= res.text

    print(req_html)
    
    b_soup=BeautifulSoup(req_html, 'html.parser')
    
    print('1. ', b_soup.title)
    print('2. ', b_soup.title.name)
    print('3. ', b_soup.title.string)
    print('4. ', b_soup.title.parent.name)
    print('7. ', b_soup.a)
    print('8. ', b_soup.find_all('a'))
    print('9. ', b_soup.find(id="link3"))
