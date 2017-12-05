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
    try:
        key = raw_input().strip()
        print("//////////////////////////////////////////////////////////////////////////////////////")
        key_u = unicode(key)
        n = 0
        for k in dict:
            if key_u in k:
                print('key: ' + k.encode(sys.stdout.encoding, 'ignore'))
                print('value: ' + dict[k].encode(sys.stdout.encoding, 'ignore'))
                print('=====================')
                n += 1
        print("//////////////////////////////////////////////////////////////////////////////////////")
        print("////////Found " + str(n) + " matches for _" + str(key_u) + "_.///////////")
        print("//////////////////////////////////////////////////////////////////////////////////////")
    except:
        print('Nothing found in dictionary for _' + key_u + '_.')
        print(':(')
        print("//////////////////////////////////////////////////////////////////////////////////////")

