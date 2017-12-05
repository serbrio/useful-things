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

print('')
print('/////////////////////////////////////////////////////////')
print("///Hi! This is a NL-RU dictionary.///////////////////////")
print("///Search in NL words only available at the moment.//////")
print("///So there is no sense to look for words in Cyrillic.///")
print('///(Input "exit()", if you want to escape.)//////////////')
print('/////////////////////////////////////////////////////////')

while True:
    print('')
    print('')
    print('')
    print("//////////////////////////////////////////////////////////////////////////////////////")
    print("////////Enter the request://///////////////////////")
    try:
        key = raw_input().strip()
        print("//////////////////////////////////////////////////////////////////////////////////////")
        key_u = unicode(key)
        if key_u == 'exit()':
            break
        elif key_u == 'Sashu':
            print('Hi there, Sashustik! ;)')
            print('Smile! )')
            break
        n = 0
        for k in dict:
            if key_u in k:
                print('key: ' + k.encode(sys.stdout.encoding, 'ignore'))
                print('value: ' + dict[k].encode(sys.stdout.encoding, 'ignore'))
                print('=====================')
                n += 1
        print("//////////////////////////////////////////////////////////////////////////////////////")
        print("////////Found " + str(n) + " matches for _" + str(key_u) + "_.")
        print("//////////////////////////////////////////////////////////////////////////////////////")
    except:
        print('////////Nothing found in dictionary for _' + key_u + '_.')
        print(':(')
        print('////////(Input "exit()", if you want to escape.)')
        print("//////////////////////////////////////////////////////////////////////////////////////")

