import sys
import logging

debugLogger = logging.getLogger("user_debug")

#you can use both double quotes and single quotes for string 
#like "string" and 'string'



if __name__ == "__main__":
    single_quotes_string = 'single quotes string'
    double_quotes_string = "double quotes string"

    print(single_quotes_string)
    print(double_quotes_string)

    tab_string = "\t" # tab string
    print("length of tab_string:", len(tab_string))

    not_tab_string = r"\t" # '\' and 't' string
    print("length of not_tab_string:", len(not_tab_string))
    
    multi_line_string = """This is the first line.
    and this is the second line
    and this is the third line"""
    print(multi_line_string)

    



