# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 21:46:39 2019

@author: IAN
"""

import sys
import logging
import os
import shutil

formatter = '%(asctime)-15s:%(module)s:%(lineno)d:%(message)s'
logging.basicConfig(stream=sys.stderr, format=formatter, level=logging.DEBUG)
debugLogger = logging.getLogger("user_debug")
debugLogger.setLevel(logging.DEBUG)

#def DLog(*args):
#    for msg in args:
#        debugLogger.debug(msg)

def DLog(*args):
    msg_str=""
    for msg in args:
        msg_str +=str(msg)
    debugLogger.debug(msg_str)

#str.endswith("extension")

#os.getcwd() 현재 작업 디렉토리 반환
#os.chdir(path) 작업 디렉토리 변경
#os.access(path, mode)
#F_OK : 해당 path의 존재 여부 True/False
#R_OK : 해당 path의 읽기 가능 여부 True/False
#W_OK : 해당 path의 쓰기 가능여부 True/False
#X_OK : 해당 path의 실행가능 여부 True/False
#os.listdir(path) 해당경로에 존재하는 파일과 디렉토리를 리스트로 반환
#os.mkdir(path) : 디렉토리생성
#os.rmdir(paht) : 디렉토리 삭제
#os.remove(path) :파일 삭제
    
#try :
#    xxx
#except : 
#    xxx
#except : 
#    xxx
#else : 
#    xxx
#    pass
#finally :
#    xxx
#os.path.isfile(path)
#os.path.exists(path)

def RemoveAllFile(filePath):
    if os.path.exists(filePath):
        for file in os.scandir(filePath):
            os.remove(file.path)
        return True
    else:
        return False

def RemoveExtensionFile(filePath, extension):
    if os.path.exists(filePath):
        for file in os.scandir(filePath):
            if file.name.endswith(extension):
                os.remove(file.path)
        return True
    else :
        return False


if __name__ =="__main__":
    DLog("start of test")
    file_path = "test.txt"
    if file_path.endswith("txt"):
        DLog("text file")


    DLog("current path : ",os.getcwd())
    cur_path = os.getcwd() # current path
    cur_path = cur_path.replace("\\","/")
    DLog(cur_path)

    ch_file_path ="test_folder"
    test_file_name ="test_file.txt"
    try :
        os.chdir(ch_file_path)
    except FileNotFoundError :
        DLog("file not found : ",ch_file_path)

    DLog(os.access(test_file_name, os.F_OK))
    DLog(os.access("test_folder_2", os.F_OK))

    DLog(os.listdir())

    dir_name = "test_folder_3"
    try :
        os.mkdir(dir_name)
    except (FileExistsError , OSError) as e:
        DLog("mkdir error : ", e)

    try :
        os.rmdir(dir_name)
    except (FileNotFoundError , OSError) as e:
        DLog("rmdir error : ", e)
        
    try :
        shutil.rmtree(dir_name)
    except (FileNotFoundError, OSError) as e:
        DLog("rmtree error : ", e)
    else:
        pass

    DLog(os.getcwd())
    for file in os.scandir(os.getcwd()):
        DLog(file.path)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    