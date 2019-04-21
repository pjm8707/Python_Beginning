from __future__ import division
import sys

# from __future__ import division
temp_value_1 = 5/2;
temp_value_2 = 5//2;
print("temp_value_1(", type(temp_value_1), "):", temp_value_1)
print("temp_value_2(", type(temp_value_2), "):", temp_value_2)

# function

def Double(x):
    """ ex
    this function is to output two times x.
    """
    return x*2
print ("\ndouble(8):", Double(8))

def ApplyToEight(func):
    """call the function func has input parameter 8 """
    return func(8)

MyDouble = Double
print("apply_to_eight(double):", ApplyToEight(MyDouble))

#lambda function
print("call the lambda function:", ApplyToEight(lambda x: x+5))

#a better way than lambda func
def AnotherDouble(x): return 2*x
print("another_double:", AnotherDouble(7))

#default parameter
def MyPrint(msg="my default message"): 
    return msg

print("\nMyPrint():", MyPrint())
print("MyPrint():", MyPrint("Hello JM!!!"))

def Subtract(a=0, b=0):
    return a-b
print("\nSubTract(10,5):", Subtract(10,5))
print("SubTract(0,5):", Subtract(0,5))
print("SubTract(b=5):", Subtract(b=5))









