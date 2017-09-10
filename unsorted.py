
##URL parse######
## python3

from urllib.parse import parse_qs
my_vals = parse_qs('red=5&blue=0&green=&black=zerospace+and+ampersand+%26+the%3A+end,5', keep_blank_values=True)
print(my_vals)

#  python2

from urlparse import parse_qs
my_vals = parse_qs('red=5&blue=0&green=&black=zerospace+and+ampersand+%26+the%3A+end,5', keep_blank_values=True)
