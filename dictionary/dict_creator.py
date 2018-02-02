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
    listo = []
    with io.open('NL-RU-A.txt', 'r', encoding='utf-8', errors='ignore') as fi:
        for line in fi:
            listo.append(line)
    #(!)need to load all dict txt files. 

    dictio = {}
    pattern = re.compile(" - ")

    for x in listo:
        val = x.strip()
        match = pattern.split(val, maxsplit=1)
        if len(match) == 2:
            dictio[unicode(match[0])] = unicode(match[1])
            #(!)add check, if the dict[unicode(match[0])] is already used,
            #if so -> add new key to dict
    return dictio


def d_searcher(entry, dictio):
    key = entry.strip()
    if key == '':
        return [('', '')], ''
    else:
        n = 0
        search_result_full_match = []
        search_result = []
        final_result = []
        for k in dictio:
            if key.lower() == k.lower():
                ke = k.encode('utf-8', 'ignore')
                va = dictio[k].encode('utf-8', 'ignore')
                search_result_full_match.append((ke, va))
                n += 1
            elif key.lower() == k.lower().split()[0]:
                ke = k.encode('utf-8', 'ignore')
                va = dictio[k].encode('utf-8', 'ignore')
                search_result_full_match.append((ke, va))
                n += 1
            elif key.lower() in k.lower():
                ke = k.encode('utf-8', 'ignore')
                va = dictio[k].encode('utf-8', 'ignore')
                search_result.append((ke, va))
                n += 1
        if search_result_full_match:
            for i in sorted(search_result_full_match):
                if len(final_result) > 10:
                    break
                final_result.append(i)
        if search_result:
            for i in sorted(search_result):
                if len(final_result) >= 10:
                    break
                final_result.append(i)
            #if first word ('word ') fully matches key (the request),
            #put it in the top of the search_result list
        if final_result:
            return final_result, n
        else:
            return [(('Nothing found in dictionary for "' + key + '".'), '')], n




#if __name__ == '__main__':
#    d_creator()
