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


def d_creator():
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
    return dict

def d_searcher(entry, dict):
    try:
        n = 0
        search_result = []
        key = entry().strip()
        key_u = unicode(key)
        for k in dict:
            if key_u in k:
                key = 'key: ' + k.encode(sys.stdout.encoding, 'ignore')
                value = 'value: ' + dict[k].encode(sys.stdout.encoding, 'ignore')
                #print('=====================')
                search_result.append((key, value))
                n += 1
        #print("//////////////////////////////////////////////////////////////////////////////////////")
        #print("////////Found " + str(n) + " matches for _" + str(key_u) + "_.")
        #print("//////////////////////////////////////////////////////////////////////////////////////")
    except:
        except_message = 'Nothing found in dictionary for _' + key_u + '_.'
        search_result.append(except_message)
    return search_result, n

def main():
    d_creator()


if __name__ == '__main__':
    main()
