import datetime

def plusDagen( jaar, maand, dag, increment ):
    startdatum = datetime.datetime( jaar, maand, dag )
    einddatum = startdatum + datetime.timedelta( days=increment )
    return einddatum.year, einddatum.month, einddatum.day

y, m, d = plusDagen( 2015, 11, 13, 55 )
print( "{}/{}/{}".format( y, m, d ) )