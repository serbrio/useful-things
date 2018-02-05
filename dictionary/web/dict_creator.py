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
    path_to_dict_source = os.path.abspath('/data/www/modules/dict/txt_sources/')
    for file_name in os.listdir(path_to_dict_source):
        with io.open(path_to_dict_source + '/' + file_name, 'r', encoding='utf-8', errors='ignore') as fi:
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
        n = [0]

        def comforter(k, l):
            l.append((k, dictio[k]))
            n[0] += 1

        search_result_full_match = []
        search_result_head_match = []
        search_result = []
        final_result = []
        for k in dictio:
            if key.lower() == k.lower():
                comforter(k, search_result_full_match)
            elif key.lower() == k.lower().split()[0]:
                comforter(k, search_result_full_match)
            elif re.match(key.lower(), k.lower()):
                comforter(k, search_result_head_match)
            elif key.lower() in k.lower():
                comforter(k, search_result)
        if search_result_full_match:
            for i in sorted(search_result_full_match):
                if len(final_result) > 10:
                    break
                final_result.append(i)
        if search_result_head_match:
            for i in sorted(search_result_head_match):
                if len(final_result) > 10:
                    break
                final_result.append(i)
        if search_result:
            for i in sorted(search_result):
                if len(final_result) >= 10:
                    break
                final_result.append(i)
                # if first word ('word ') fully matches key (the request),
                # put it in the top of the search_result list
        if final_result:
            return final_result, n[0]
        else:
            return [(('Nothing found in dictionary for "' + key + '".'), '')], n[0]




#if __name__ == '__main__':
#    d_creator()
