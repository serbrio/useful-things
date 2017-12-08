# -*- coding: utf-8 -*-


##
##Just for fun
##

"""
...
"""

import re
import io
#import sys


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
          #add check, if the dict[unicode(match[0])] is already used, 
          #if so -> add new key to dict
    return dict

def d_searcher(entry, dict):
    n = 0
    search_result = []
    key = entry.strip()
    #ignore uppercase
    for k in dict:
        if key in k: 
            ke = k.encode('utf-8', 'ignore')
            va = dict[k].encode('utf-8', 'ignore')
            search_result.append((ke, va))
            n += 1
    if search_result:
        #if first word ('word ') fully matches key (the request), 
        #put it in the top of the search_result list
        return sorted(search_result), n
    else:
        return [(('Nothing found in dictionary for "' + key + '".'), '')], n




#if __name__ == '__main__':
#    d_creator()
