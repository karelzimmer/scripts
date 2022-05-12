curses = {
    '880254': 
    { "naam":"Onderzoeksvaardigheden Data Processing", "ects":3, 
        "studenten":{'u123456':8, 'u383213':7.5, 'u234178':6} }, 
    '822177': 
    { "naam":"Logica", "ects":6,
        "studenten":{'u123456':5, 'u223416':7, 'u234178':9} }, 
    '822164': 
    { "naam":"Computer Games", "ects":6,
        "studenten":{'u123456':7.5, 'u223416':9 } } }

for c in curses:
    print( "{}: {} ({})".format( c, curses[c]["naam"], 
        curses[c]["ects"] ) )
    for s in curses[c]["studenten"]:
        print( "{}: {}".format( s, curses[c]["studenten"][s] ) )
    print()