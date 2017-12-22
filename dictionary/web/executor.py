#!/bin/env python3

##
##Just for fun
##

import cgi
import time


def logging(fileName, logStr):
    timestamp = time.strftime("%d.%m.%Y  %H:%M:%S")
    s = timestamp + '\n' + logStr + '\n'
    file = open(fileName, 'a')
    file.write(s)
    file.close()
    return


try:
    print("Content-type: text/html\n\n")
    import form
    form.main()

except Exception as e:
    print("""<!DOCTYPE HTML>
          <html>
          <head>
              <meta charset="utf-8">
              <title>NL-RU</title>
          </head>
          <body bgcolor="#CD853F">
          <h1>Something went wrong.</h1>
          </body>
          </html>""")
    logging('logs.txt', str(e))
