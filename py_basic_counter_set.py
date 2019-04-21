import sys
import logging
from collections import Counter


#logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

logging.basicConfig(strem = sys.stderr, level = logging.DEBUG)
debugLogger = logging.getLogger("user_debug")
debugLogger.setLevel(logging.DEBUG)

def DLog(*args):
    for msg in args:
        debugLogger.debug(msg)
    
    debugLogger.debug("\n")

myDocument = ["test", "test", "test_1", "test_2", "test_3", "test_3"]


if __name__ == "__main__":
    #Counter,most_common()
    myCounter = Counter([0, 1, 2, 3, 0])
    DLog(myCounter);
    
    
    word_counts = Counter(myDocument)
    
    #output 10 most frequent words and their frequency
    for word, count in word_counts.most_common(10):
        DLog(word, count)

    #set - reperesent a set of unique items
    mySet = set()
    mySet.add(1)
    mySet.add(2)
    mySet.add(2)
    DLog("len", len(mySet))
    
    #in works faster on set() than list()
    DLog(1 in mySet)
    DLog(3 in mySet)
    
    #Remove duplcate elements
    item_list =[1,2,3,1,2,3]
    item_set =set(item_list)
    
    DLog(item_list, len(item_list))
    DLog(item_set ,len(item_set))

















