# -*- coding: utf-8 -*-


##
##Just for fun
##

"""
...
"""

import re
#import codecs
import io


#file = open('NL-RU-A.txt', 'r')
#list = file.readlines()
#file.close()

#file = codecs.open('NL-RU-A.txt', 'r', 'utf_8_sig')
#list = file.readlines()
#file.close()

list = []
with io.open('NL-RU-A.txt', 'r', encoding='utf-8', errors='ignore') as fi:
    for line in fi:
        list.append(line)

dict = {}
for x in list:
    #key_val = x.strip().split(r' - ')
    # dict[key_val[0]] = key_val[1]
    val = x.strip()
    #print 'val is: ', val
    match = re.search(r'(.*) - (.*)', val, re.U)
    if match:
        dict[match.group(1)] = match.group(2)
    else:
        dict[val] = ''

#print dict

while True:
    print('')
    print('////////////////////////////////////////////////////')
    print("Enter the request:")
    key = raw_input()
    try:
        for k in dict:
            if key in k:
                print('')
                #print k + ': ', dict[k]
                print 'key: ', k
                print 'value: ', dict[k]
                print('=====================')
    except:
        print('Nothing found in dictionary for ' + key)