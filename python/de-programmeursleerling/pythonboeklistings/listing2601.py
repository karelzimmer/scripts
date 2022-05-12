from csv import reader

fp = open( "pc_inventory.csv", newline='' )
csvreader = reader( fp )
for regel in csvreader:
    print( regel )
fp.close()