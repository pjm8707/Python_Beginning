# -*- coding: utf-8 -*-
#!/usr/bin/python3
"""
Created on Wed Nov 24 11:09:01 2021

@author: ian
"""

#rule
"""
* naming rule
 - dictionary/list/tuple
global constant : DIC_/LIST_/TUP_
local variable : dic_/li_/tup_
"""

# mysql, pip install PyMySQL
import pymysql

# panda sql , pip install -U pandasql
from pandasql import sqldf

import os, sys, re

#function
def test_func() :
    test_func.idx += 1
    return test_func.idx

test_func.idx = 0

#string formating python v3.~
test_str = 'Hi, {}'.format('Ian')
print(test_str)
test_str = 'Name : {0}, Num : {1}'.format('Ian', '2006')
print(test_str)

#list
integer_list = [1,2,3,4,5]
heterogeneous_list = ["string", 3, 0.1, True]
list_of_list = [integer_list, heterogeneous_list, []]
legthOfList = len(integer_list)

range_x = range(10)
print("type:", type(range_x))
print("length :", len(range_x))

for val in range_x:
    print("val:", val)

#dictionary
empty_dict1 = {}
empty_dict2 = dict()
list_grades = {80, 95}
grades = {"Joel" : 80, "Tim" : 95}

print(grades['Joel'])

tweet = {
        "user" : "jay",
        "text" : "I am a nice guy",
        "retweet_count" : 100,
        "hashtags" : ["#excercise", "#crossfit", "#yolo", "#500F"],
        "list_grade" : list_grades
        }

tweet_keys = tweet.keys() # key list
tweet_valus = tweet.values() # value list
tweet_items = tweet.items() # key + value list

for val in tweet['list_grade']:
    print("val : {}".format(val))


xxx_8b_list=[
    "test_xxx_list_1",
    "test_xxx_list_2",
    "test_xxx_list_3",
]

DIC_STREAM_LIST = {
    "xxx"    : [ "xxx_list", xxx_8b_list],
}

#os (import os)
cmd="pwd"
os.system(cmd)

#file open/close
rfile_path = r'D:\199_TEMP\temp_file_20190703\r_test_doc.txt'
wfile_path = r'D:\199_TEMP\temp_file_20190703\w_test_doc.txt'
rfile_path.replace('\\', '/')
wfile_path.replace('\\', '/')

#mode = 'r+b'
with open(rfile_path , mode = 'rt+', encoding = 'utf-8') as file :
    for line in file:
        print(line)

with (open(rfile_path, mode = 'rt+', encoding = 'utf-8')) as rFile :
    with (open(wfile_path, mode = 'wt+', encoding = 'utf-8')) as wFile:
        for line in rFile:
            wFile.write(line)

#re
pattern='picture_num : [0-9]+'
res = re.search(pattern, line)
last_display_res_group = res.group()

#my sql
HOST_DB_ADDR='52.2.12.152'
HOST_DB_ID='qc_000'
HOST_DB_PW='123qwe'
DB_NAME='BITSTREAM'

user=HOST_DB_ID
passwd=HOST_DB_PW
host=HOST_DB_ADDR
db_name=DB_NAME

stream_db = pymysql.connect (
        user=user,
        passwd=passwd,
        host=host,
        db=db_name,
        charset='utf8',
        port=3306
        )

cursor = stream_db.cursor(pymysql.cursors.DictCursor)

sql='select * from AV1_8B where name = \'PATAGONIA_7680x4320_03647_03759.ivf\''

cursor.execute(sql)

li_result = cursor.fetchall() # fetch all data
print(li_result)
print(len(li_result))
print(li_result[0]['name'])
#result = cursor.fetchone() # fetch a row
#result = cursor.fetchmany(n) # fetch n rows




