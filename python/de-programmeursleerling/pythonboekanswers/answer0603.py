from pcinput import getString

s = getString( "Geef een string: " )
count = 0
if ("a" in s) or ("A" in s):
    count += 1
if ("e" in s) or ("E" in s):
    count += 1
if ("i" in s) or ("I" in s):
    count += 1
if ("o" in s) or ("O" in s):
    count += 1
if ("u" in s) or ("U" in s):
    count += 1
    
if count == 0:
    print( "Er zitten geen klinkers in de string." )
elif count == 1:
    print( "Er zit maar 1 verschillende klinker in de string." )
else:
    print( "Er zijn", count, "verschillende klinkers." )