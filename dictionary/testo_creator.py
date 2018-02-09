# -*- coding: utf-8 -*-


##
##Just for fun
##

"""
...
"""

import os
import io


def list_creator():
    listo = []
    for file_name in os.listdir('./txt_sources/'):
        with io.open('./txt_sources/%s' % file_name, 'r', encoding='utf-8', errors='ignore') as fi:
            for line in fi:
                listo.append(line)
    return listo

def main():
    listo = list_creator()
    file = open('testo.py', 'a')
    file.write('listo = ' + str(listo))
    file.close()


if __name__ == '__main__':
    main()

