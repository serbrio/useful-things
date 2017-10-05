##
##Just for fun
##

"""
...
"""

import re


file = open('example.txt', 'r')
list = file.readlines()
file.close()

dict = {}
for x in list:
    key_val = x.strip().split(r' - ')
    dict[key_val[0]] = key_val[1]


print dict

while True:
    print("Enter the request\n")
    key = raw_input()
    try:
        for k in dict:
            if key in k:
                print(k + ': ', dict[k])
                print('=====================')
    except:
        print('Nothing found in dictionary for ' + key)