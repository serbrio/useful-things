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
    return dict

def d_searcher(entry, dict):
    n = 0
    search_result = []
    key = entry.strip()
    for k in dict:
        if key in k:
            ke = k.encode('utf-8', 'ignore')
            va = dict[k].encode('utf-8', 'ignore')
            search_result.append((ke, va))
            n += 1
    if search_result:
        return search_result, n
    else:
        return [(('Nothing found in dictionary for __' + key + '__.'), '')], n

def main():
    d_creator()


if __name__ == '__main__':
    main()
