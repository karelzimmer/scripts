import re

mlist = re.finditer(r"ba+","Schaap zegt 'baaaaah' tot Ali Baba.")
for m in mlist:
    print( "{} is found at {}.".format(m.group(), m.start()))