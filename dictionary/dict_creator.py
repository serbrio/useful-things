# -*- coding: utf-8 -*-


##
##Just for fun
##

"""
...
"""

import re
#import io
#import sys
import os
import testo


def d_creator():
    listo = testo.listo
    #listo = []
    #for file_name in os.listdir('./txt_sources/'):
    #    with io.open('./txt_sources/%s' % file_name, 'r', encoding='utf-8', errors='ignore') as fi:
    #        for line in fi:
    #            listo.append(line)

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
        n = [0]
        # "n" is a list (mutable type), because there is no support of nonlocal statement in python 2,
        # but we need to change the value in a function deeper

        def comforter(k, l):
            ke = k.encode('utf-8', 'ignore')
            va = dictio[k].encode('utf-8', 'ignore')
            l.append((ke, va))
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
            #if first word ('word ') fully matches key (the request),
            #put it in the top of the search_result list
        if final_result:
            return final_result, n[0]
        else:
            return [(('Nothing found in dictionary for "' + key + '".'), '')], n[0]




#if __name__ == '__main__':
#    d_creator()
