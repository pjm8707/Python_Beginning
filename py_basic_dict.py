import sys
import logging
from collections import defaultdict


#logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

logging.basicConfig(strem = sys.stderr, level = logging.DEBUG)
debugLogger = logging.getLogger("user_debug")
debugLogger.setLevel(logging.DEBUG)

def DLog(*args):
    for msg in args:
        debugLogger.debug(msg)
    
    debugLogger.debug("\n")

#you can use both double quotes and single quotes for string 
#like "string" and 'string'



if __name__ == "__main__":
    #dict
    empty_dict1 = {}
    empty_dict2 = dict()
    grades = {"Joel" : 80, "Tim" : 95}
    
    joels_grade = grades["Joel"]
    DLog("\njoels_grade:", joels_grade)
    
    try:
        kates_grade = grades["Kate"]
    except KeyError:
        DLog("\n no grade for Kate!!!")

    
    bResult = "Joel" in grades
    DLog("Joel has grade:", "Joel" in grades)
    DLog("Kate has grade:", "kate" in grades)

    #dict.get() method
    joels_grade = grades.get("Joel", 0)
    kates_grade = grades.get("Kate", 0)
    
    DLog("Joel's grade:", joels_grade)
    DLog("kate's grade:", kates_grade)
    
    #assignment - dict
    grades["Tim"] = 99
    grades["Kate"] = 100
    DLog("Num of Students:", len(grades))
    
    #To make typical data simply, mostly dict is used.
    tweet = {
            "user" : "jay",
            "text" : "I am a nice guy",
            "retweet_count" : 100,
            "hashtags" : ["#excercise", "#crossfit", "#yolo", "#500F"]
            }

    tweet_keys = tweet.keys() # key list
    tweet_valus = tweet.values() # value list
    tweet_items = tweet.items() # key + value list
    DLog(type(tweet_keys))
    DLog(tweet_keys)
    DLog(tweet_valus)
    DLog(tweet_items)
    
    
    word_cnt = {}
    document = ["text", "text", "text_2", "text_3", "text_2", "text"]
    
    for word in document:
        if word in word_cnt:
            word_cnt[word] += 1
        else:
            word_cnt[word] = 1
    
    #default dict
    #from collections import defaultdict
    word_cnt_default = defaultdict(int)
    
    for word in document:
        word_cnt_default[word] +=1

    word_cnt_items = word_cnt_default.items()   
    DLog(word_cnt_default.items())
    
    dict_list = defaultdict(list)
    dict_list[2].append(1)
    DLog(dict_list.items())





















