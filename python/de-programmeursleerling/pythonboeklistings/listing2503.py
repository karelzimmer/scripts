import re

slist = re.findall( r"b[aeiou]ll", "Bill Gates en Uwe Boll \
dronken Red Bull bij het voetballen in Campbell." )
print( slist )