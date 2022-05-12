from csv import reader
from json import dump

data = []

fp = open( "pc_inventory.csv", newregel='' )
csvreader = reader( fp )
for regel in csvreader:
    data.append( regel )
fp.close()

fp = open( "pc_writetest.json", "w" )
dump( data, fp )
fp.close()

fp = open( "pc_writetest.json" )
print( fp.read() )
fp.close()