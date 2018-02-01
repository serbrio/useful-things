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


def d_creator():
    listo = []
    path_to_dict_source = os.path.abspath('/data/www/modules/dict/NL-RU-A.txt')
    with io.open(path_to_dict_source, 'r', encoding='utf-8', errors='ignore') as fi:
        for line in fi:
            listo.append(line)

    dictio = {}
    pattern = re.compile(" - ")

    for x in listo:
        val = x.strip()
        match = pattern.split(val, maxsplit=1)
        if len(match) == 2:
            dictkey = str(match[0])
            dictval = str(match[1])
            dictio[dictkey] = dictval
            #add check, if the dict[unicode(match[0])] is already used,
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
                ke = k
                va = dictio[k]
                search_result_full_match.append((ke, va))
                n += 1
            elif key.lower() == k.lower().split()[0]:
                ke = k
                va = dictio[k]
                search_result_full_match.append((ke, va))
                n += 1
            elif key.lower() in k.lower():
                ke = k
                va = dictio[k]
                search_result.append((ke, va))
                n += 1
        if search_result_full_match:
            for i in sorted(search_result_full_match):
                final_result.append(i)
        if search_result:
            for i in sorted(search_result):
                final_result.append(i)
                # if first word ('word ') fully matches key (the request),
                # put it in the top of the search_result list
        if final_result:
            return final_result, n
        else:
            return [(('Nothing found in dictionary for "' + key + '".'), '')], n




#if __name__ == '__main__':
#    d_creator()
