# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 23:06:53 2019

@author: Jay Park
"""

import sys

if __name__ == "__main__":
    try:
        print (0/0)
    except ZeroDivisionError:
        print("Can not devide by zero")