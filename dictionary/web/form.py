# -*- coding: utf-8 -*-

##
##Just for fun
##

import cgi
import html
import dict_creator


def main():
    form = cgi.FieldStorage()
    ent = form.getfirst("REQUEST", "")
    ent = html.escape(ent)
    contents = processInput(ent)
    print(contents)

def processInput(s):
    ResultStr, nStr = Find(s)
    return fileToStr('Template.html').format(**locals())

def fileToStr(fileName):
    f = open(fileName)
    contents = f.read()
    f.close()
    return contents

def Find(s):
    result, n = dict_creator.d_searcher(s, dict_creator.d_creator())
    ResultStr = ""
    for i in result:
      ResultStr = ResultStr + """\n<br>
      \n<p><BIG><b>%s</b></BIG></p>
      \n<p>%s</p>
      \n<HR>""" % (i[0], i[1])
    return ResultStr, str(n)


if __name__ == '__main__':
  main()
