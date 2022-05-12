from statistics import mean, median, mode, stdev, variance, \
    StatisticsError

data = [ 4, 5, 1, 1, 2, 2, 2, 3, 3, 3 ]

print( "gemiddelde:", mean( data ) )
print( "mediaan:", median( data ) )
try:
    print( "modus:", mode( data ) )
except StatisticsError as e:
    print( e )
print( "st.dev.: {:.3f}".format( stdev( data ) ) )
print( "variantie: {:.3f}".format( variance( data ) ) )