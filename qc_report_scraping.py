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
from datetime import datetime

#for web scraping
import requests
from bs4 import BeautifulSoup

#for contral excel
from openpyxl import Workbook

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
URL="http://wiki.chipsnmedia.com:8080/pages/viewpage.action?pageId=147763151"
LOGIN_DATA = {
    'os_username': 'ian.park',
    'os_password': '@yangjaemin2'
}

class Web_scraping:
    def __init__(self):
        print("Web scraping class")


def GetLogInfoFromhtml_th(html_data, header_cnt) :
    idx=0
    th_data = []
    b_soup = BeautifulSoup(html_data, 'html.parser')
    for tag in b_soup.select('th[class="confluenceTh"]') : 
        th_data.append(tag.p.text.strip())
        idx+=1
        if (header_cnt == idx):
            break

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
        #print('index : ', idx, 'th_data : ', th_data[idx])
        td_dic[th_data[idx]] =tag.p.text.strip()        
        if ('Plain Short Full' == tag.p.text.strip()):
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

def WriteFileFromTxt(text, fpath, fmode, fencoding='utf-8') :
    with open(fpath, mode=fmode, encoding=fencoding) as f :
        f.write(text)

def ReadFileLines(fpath, fmode, fencoding='utf-8'):
    with open(fpath, mode=fmode, encoding=fencoding) as f :
        text = f.readlines()
        return text
#text_data = GetDataFromFile('test_log_20200308.txt')
#extracted_data, fail_cnt = ParseLogData(text_data)
#for log in extracted_data :
#    print(log, end='')
        
def MakeLogFile(idx, text) :
    file_name = 'test_log_' + str(idx)
    with open(file_name, mode='w', encoding='utf-8') as f :
        f.write(text)
        
def ReadLogFile(idx) :
    file_name = 'test_log_' + str(idx)
    with open(file_name, mode='r', encoding='utf-8') as f :
        text = f.readlines()
    return text

def MakeExcelData(workbook, sheet_name, data) :
    work_sheet= workbook.create_sheet(sheet_name)
    for line_log in data :
        work_sheet.append([line_log])
    

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

    #print(req_html)
    
    th_data = GetLogInfoFromhtml_th(req_html, 13)
    td_data = GetLogInfoFromhtml_td(req_html, th_data)
    print('len :',len(td_data))
    
    log_url = []
    for data in td_data :
        print(data['STREAMS'], ': ', data['JENKINS'])
        log_url.append(data['JENKINS'])

    print('log url : ', log_url[0].replace(' ',''))
    
    idx = 0
    print('len :',len(log_url))
    for url in log_url :
        print("log url :" , url, " idx : ", idx)
        res = s.get(url.replace(' ',''))
        MakeLogFile(idx, res.text)
        idx+=1
    
    #res=s.get(log_url[6].replace(' ',''))
    #res=s.get('http://ci.chipsnmedia.com/job/WAVE517_DEC_qc/26006/consoleText')
    #print(res.text)
    
    #f_log = OpenFile('test.log', 'w')
    #f_log.write(res.text)
    #f_log= open('test.log', 'w')
    #f_log.write(res.text)
    #f_log.close()
    
    #f_log = open('test.log', 'r')
    #text = f_log.readlines()
    
    workbook = Workbook() # excel file
    #datetime.today().strftime("%Y_%m_%d_%H_%M%S")
    time_data = datetime.today().strftime("%Y_%m_%d_%H_%M")
    excel_file_name="test" + time_data + ".xlsx"
    
    idx=0
    for data in td_data :
        text = ReadLogFile(idx)
        fail_data, fail_cnt = ParseLogData(text)
        MakeExcelData(workbook, data['STREAMS'], fail_data)
        idx+=1
    
    workbook.save(excel_file_name)
#    fail_data, fail_cnt = ParseLogData(text)
#    print('fail cnt : ', fail_cnt)
#    for f_data in fail_data :
#        print(f_data, end='')
        
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
