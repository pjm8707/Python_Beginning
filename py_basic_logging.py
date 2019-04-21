# -*- coding: utf-8 -*-
import sys
import logging

formatter = '%(asctime)-15s:%(module)s:%(lineno)d:%(message)s'
logging.basicConfig(stream=sys.stderr, format=formatter, level=logging.DEBUG)
debugLogger = logging.getLogger("user_debug")
debugLogger.setLevel(logging.DEBUG)

def DLog(*args):
    for msg in args:
        debugLogger.debug(msg)
    
    debugLogger.debug("\n")
    
#asctime
#clientip
#message
#lineno
#__name__
#funcName
#levelno
#module
if __name__ == "__main__":
    DLog("LOG TEST")

