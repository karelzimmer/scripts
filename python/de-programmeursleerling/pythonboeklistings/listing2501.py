import re

pAplus = re.compile( r"a+" )
lAplus = pAplus.findall( "aardvarken" )
print( lAplus )