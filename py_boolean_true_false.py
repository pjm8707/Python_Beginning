# -*- coding: utf-8 -*-

import sys

if __name__ == "__main__":
    result_1 = 1 < 2
    result_2 = 1 > 2
    result_3 = None
    
    print("result_1 :", result_1)
    print("result_2 :", result_1)
    print("result_3 :", result_1, "\n")
    
    #is operator
    print("result_1 is True :", result_1 is True)
    print("result_2 :", result_2 is True)
    print("result_3 :", result_3 is None)
    
    # and operator
    x = True
    x_data = 100
    temp_val = x and x_data
    
    print("x data:", x and x_data)
    
    x = False
    print("x data:", x and x_data)
    
    #all and any function
    # all() - if all times are ture, return true
    # any() - if any items is ture, return true
    
    test_list = [True, 1, 0, 2]
    
    print("result of all():", all(test_list))
    print("result of any():", any(test_list))
    