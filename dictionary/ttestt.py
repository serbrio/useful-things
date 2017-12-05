# -*- coding: utf-8 -*-


##
##Just for fun
##

"""
...
"""

import re
import io
import sys
#reload(sys)
#import locale
#sys.setdefaultencoding(locale.getpreferredencoding())

list = []
with io.open('NL-RU-A.txt', 'r', encoding='utf-8', errors='ignore') as fi:
    for line in fi:
        list.append(line)

dict = {}
pattern = re.compile(" - ")

for x in list:
    val = x.strip()
    match = pattern.split(val, maxsplit=1)
    if len(match) == 2:
        dict[unicode(match[0])] = unicode(match[1])
    else:
        val_u = unicode(val)
        dict[val_u] = ''

while True:
    print('')
    print('')
    print('')
    print('')
    print("//////////////////////////////////////////////////////////////////////////////////////")
    print("////////Enter the request://///////////////////////")
    key = raw_input().strip()  #Need to add processing of input from Windows OS - there must be some bugs
    print("//////////////////////////////////////////////////////////////////////////////////////")
    key_u = unicode(key)
    n = 0
    #try:
    for k in dict:
            if key_u in k:
                #print('')
                #print k + ': ', dict[k]
                #print('key: ', k.encode('utf-8', 'ignore'))
                #print(dict[k].encode('cp866', 'ignore'))
                print('key: ' + k.encode(sys.stdout.encoding, 'ignore'))
                print('value: ' + dict[k].encode(sys.stdout.encoding, 'ignore'))
                print('=====================')
                n += 1
                #for i in list:
                #    if k in i:
                #        print('from list:')
                #        print(i)
    print("//////////////////////////////////////////////////////////////////////////////////////")
    print("////////Found " + str(n) + " matches for _" + str(key_u) + "_.///////////")
    print("//////////////////////////////////////////////////////////////////////////////////////")
    #except:
    #    print('Nothing found in dictionary for _' + key_u + '_.')
    #    print(':(')
    #    print("//////////////////////////////////////////////////////////////////////////////////////")

