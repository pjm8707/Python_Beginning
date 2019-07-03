# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 10:37:37 2019

@author: ian
"""


import os
import re

#file.read() 파일 내용의 전체를 다 읽어들인다. 파일 크기가 큰 경우 주

#file_path = 'C:\\Users\\todae\\Desktop\\mydir\\testFile.txt'
#dir_path = os.path.dirname(file_path)
#file_name = os.path.basename(file_path)

#print(os.path.isfile(file_path))
#print(os.path.isdir(dir_path))

#os.getcwd() 현재 디렉토리
#os.chdir("디렉토리 경로") 현재 디렉토리 변경
#os.listdir() 디렉토리에있는 파일 and 디렉토리 목록

#re
#re.search(d{4})
#re.sub('\d{4}', 'xxxx', '010-1234-5678')



# temp_list = r"D:\199_TEMP\temp_file_20190703\test_doc.txt"
# print(temp_list.replace('\\', '/'))

    

if __name__=='__main__':
    rfile_path = r'D:\199_TEMP\temp_file_20190703\r_test_doc.txt'
    wfile_path = r'D:\199_TEMP\temp_file_20190703\w_test_doc.txt'
    rfile_path.replace('\\', '/')
    wfile_path.replace('\\', '/')

    #mode = 'r+b'
    with open(rfile_path , mode = 'r', encoding = 'utf-8') as file :
        for line in file:
            print(line)

    with (open(rfile_path, mode = 'r', encoding = 'utf-8')) as rFile :
        with (open(wfile_path, mode = 'w', encoding = 'utf-8')) as wFile:
            for line in rFile:
                wFile.write(line)

