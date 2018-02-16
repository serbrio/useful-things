# -*- coding: utf-8 -*-


##
##Just for fun
##

"""
...
"""

import os
import io
import base64

def list_creator():
    listo = []
    for file_name in os.listdir('./txt_sources/'):
        with io.open('./txt_sources/%s' % file_name, 'r', encoding='utf-8', errors='ignore') as fi:
            for line in fi:
                listo.append(line)
    return listo

def icon_b64_creator():
    with io.open('./images/raw_icon.gif', 'rb') as fi:
        icon_b64 = base64.b64encode(fi.read())
    return icon_b64


def main():
    listo = list_creator()
    #icon_b64 = icon_b64_creator()
    file = open('testo.py', 'w')
    file.write('listo = ' + str(listo))
    #file.write('\nicon_b64 = ' + '"""' + icon_b64 + '"""')
    file.close()


if __name__ == '__main__':
    main()

