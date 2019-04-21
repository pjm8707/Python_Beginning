# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 23:09:20 2019

@author: Jay Park
"""

import sys

def SumAndMultiproduct(x, y):
    return (x+y), (x*y)

# if this file is a main file, __name__ == "__main__"
if __name__ == "__main__":
    integer_list = [1,2,3,4,5]
    heterogeneous_list = ["string", 3, 0.1, True]
    list_of_list = [integer_list, heterogeneous_list, []]
    
    legthOfList = len(integer_list)
    print("\nlegth of list(integer_list) :",legthOfList)
    
    legthOfList = len(list_of_list)
    print("\nlegth of list(list_of_list) :",legthOfList)
    
    
    #sum of listif you want to know about the function in detail, please refer to the python api document
    print("\nsum of list(integer_list):", sum(integer_list))
    
    #TypeError: unsupported operand type(s) for +: 'int' and 'list'
    #print("\nsum of list(integer_list):", sum(list_of_list))
    
    range_x = range(10)
    print("type:", type(range_x))
    print("length :", len(range_x))
    
    print("\n",range_x[0], range_x[1], range_x[2], range_x[3])
    
    print("\n",range_x[-1], range_x[-2], range_x[-3], range_x[-4])
    
    for val in range_x:
        print("val:", val)
    
    print("\n")    
    
    #if you want to know about range() class in detail, 
    #please refer to the python API document 
    
    for val in reversed(range_x):
        print("val:", val)
        
    list_x = list(range(10))
    
    first_three = list_x[:3]
    three_to_end = list_x[3:]
    one_to_four = list_x[1:5]
    without_first_and_last = list_x[1:-1]
    copy_of_x = list_x[:]
    print("first_three:", first_three)
    print("three_to_end", three_to_end)
    print("one_to_four", one_to_four)
    print("copy_of_x", copy_of_x, "\n")
    
    #operator 'in'
    #if list has a big size, it will take a long time.
    print(1 in list_x)
    print(100 in list_x, "\n")
    
    list_x.extend([10, 11, 12])
    print("list_x:", list_x)
    
    list_y = list_x + [13,14,15]
    print("list_y:", list_y)
    
    list_x.append(13)
    list_x.append(14)
    list_x.append(15)
    print("list_x:", list_x)
    
    #variable excnage
    list_y.reverse()
    list_x, list_y = list_y, list_x
    
    print("\nlist_x:", list_x)
    print("list_y:", list_y)
        
    #tuple
    my_list = [1,2]
    my_tuple = (1, 2)
    other_tuple = 3, 4
    
    print("\ntype:", type(my_list), type(my_tuple), type(other_tuple))
    
    my_list[1] = 3
    
    try:
        my_tuple[1] = 3
    except TypeError:
        print("can not modify a tuple\n")
        
    #multiple return
    product_1 = SumAndMultiproduct(3,3)
    product_2, product_3 = SumAndMultiproduct(9,9)
    
    print("product_1:", type(product_1), product_1)
    print("product_2",type(product_2), type(product_3), product_2, product_3)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
    