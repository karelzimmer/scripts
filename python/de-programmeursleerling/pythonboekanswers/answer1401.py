alles = { "Socrates", "Plato", "Eratosthenes", "Zeus", "Hera", 
    "Athene", "Acropolis", "Kat", "Hond" }
mensen = { "Socrates", "Plato", "Eratosthenes" }
sterfelijken = { "Socrates", "Plato", "Eratosthenes", "Kat", 
    "Hond" }

print( mensen.issubset( sterfelijken ) ) # (a)
print( "Socrates" in mensen ) # (b)
print( "Socrates" in sterfelijken ) # (c)
print( len( sterfelijken.difference( mensen ) ) > 0 ) # (d)
print( len( alles.difference( sterfelijken ) ) > 0 ) # (e)