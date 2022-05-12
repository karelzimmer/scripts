from csv import writer

fp = open( "pc_writetest.csv", "w", newline='' )
csvwriter = writer( fp )
csvwriter.writerow( ["FILM", "SCORE"] )
csvwriter.writerow( ["Monty Python and the Holy Grail", 8] )
csvwriter.writerow( ["Monty Python's Life of Brian", 8.5] )
csvwriter.writerow( ["Monty Python's Meaning of Life", 7] )
fp.close()