s = "Hello, world!"
mask = (1<<5) | (1<<3) | (1<<1)    # 00101010

codering = ""
for c in s:
    codering += chr(ord(c)^mask)
print( codering )

decodering = ""
for c in codering:
    decodering += chr(ord(c)^mask)
print( decodering )