# -*- coding: utf-8 -*-


##
##Just for fun
##

"""
...
"""

import re
import io
import os
#import sys


def d_creator():
    list = []
    with io.open(os.path.abspath('../../modules/dict/NL-RU-A.txt'), 'r', encoding='utf-8', errors='ignore') as fi:
      for line in fi:
          list.append(line)

    dict = {}
    pattern = re.compile(" - ")

    for x in list:
      val = x.strip()
      match = pattern.split(val, maxsplit=1)
      if len(match) == 2:
          dictkey = str(match[0])
          dictval = str(match[1])
          dict[dictkey] = dictval
          #add check, if the dict[unicode(match[0])] is already used,
          #if so -> add new key to dict
    return dict

def d_searcher(entry, dict):
    key = entry.strip()
    if key == '':
      return [('', '')], ''
    else:
      n = 0
      search_result = []
      for k in dict:
        if key.lower() in k.lower():
            #ke = k.encode('utf-8', 'ignore')
            ke = k
            #va = dict[k].encode('utf-8', 'ignore')
            va = dict[k]
            search_result.append((ke, va))
            #search_result.append((str(k, 'utf-8'), str(dict[k], 'utf-8')))
            n += 1
      if search_result:
        #if first word ('word ') fully matches key (the request),
        #put it in the top of the search_result list
        return sorted(search_result), n
      else:
        return [(('Nothing found in dictionary for "' + key + '".'), '')], n




#if __name__ == '__main__':
#    d_creator()
