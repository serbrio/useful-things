#!/bin/env python3

import cgi
import html
import dict_creator
import sys

form = cgi.FieldStorage()
ent = form.getfirst("REQUEST", "")
ent = html.escape(ent)

def Find(s):
  try:
    result, n = dict_creator.d_searcher(s, dict_creator.d_creator())
    print("<h1>Found {} matches:</h1>".format(str(n)))
    for i in result:
      print("<br>")
      print("<p><BIG><b>{}</b></BIG></p>".format(i[0]))
      print("<p>{}</p>".format(i[1]))
      print("<HR>")
  except:
    print("<p>Something went wrong.</p>")


def main():
  print("Content-type: text/html\n")
  print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Search in dictionary</title>
        </head>
        <body bgcolor="#CD853F">""")
  Find(ent)
  print("""</body>
        </html>""")


if __name__ == '__main__':
  main()


