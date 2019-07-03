# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 10:37:37 2019

@author: ian
"""
#file.read() 파일 내용의 전체를 다 읽어들인다. 파일 크기가 큰 경우 주

import os
import re

#file_path = 'C:\\Users\\todae\\Desktop\\mydir\\testFile.txt'
#dir_path = os.path.dirname(file_path)
#file_name = os.path.basename(file_path)

#print(os.path.isfile(file_path))
#print(os.path.isdir(dir_path))

#os.getcwd() 현재 디렉토리
#os.chdir("디렉토리 경로") 현재 디렉토리 변경
#os.listdir() 디렉토리에있는 파일 and 디렉토리 목록




# temp_list = r"D:\199_TEMP\temp_file_20190703\test_doc.txt"
# print(temp_list.replace('\\', '/'))

    

if __name__=='__main__':
    file_path = r'D:\199_TEMP\temp_file_20190703\test_doc.txt'
    file_path.replace('\\', '/')
    with  open(file_path , mode = 'r', encoding = 'utf-8') as file :
        for line in file:
            print(line)
