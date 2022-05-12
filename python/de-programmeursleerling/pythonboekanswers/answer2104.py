from copy import deepcopy

class Fruitmand:
    
    def __init__( self, stukken={} ):
        self.stukken = stukken
        
    def __repr__( self ):
        s = ""
        sep = "["
        for fruit in self.stukken:
            s += sep+fruit+":"+str( self.stukken[fruit] )
            sep = ", "
        s += "]"
        return s
    
    def __contains__( self, fruit ):
        return fruit in self.stukken
    
    def __add__( self, fruit ):
        fmcopy = deepcopy( self )
        fmcopy.stukken[fruit] = fmcopy.stukken.get( fruit, 0 )+1
        return fmcopy
    
    def __iadd__( self, fruit ):
        self.stukken[fruit] = self.stukken.get( fruit, 0 )+1
        return self
    
    def __sub__( self, fruit ):
        if fruit not in self.stukken:
            return self
        fmcopy = deepcopy( self )
        fmcopy.stukken[fruit] = fmcopy.stukken.get( fruit, 0 )-1
        if fmcopy.stukken[fruit] <= 0:
            del fmcopy.stukken[fruit]
        return fmcopy
    
    def __isub__( self, fruit ):
        self.stukken[fruit] = self.stukken.get( fruit, 0 )-1
        if self.stukken[fruit] <= 0:
            del self.stukken[fruit]
        return self
    
    def __len__( self ):
        return len( self.stukken )
    
    def __getitem__( self, fruit ):
        return self.stukken.get( fruit, 0 )
    
    def __setitem__( self, fruit, n ):
        if n <= 0:
            if fruit in self.stukken:
                del self.stukken[fruit]
        else:
            self.stukken[fruit] = n
    
fm = Fruitmand()
fm += "appel"
fm += "appel"
fm += "banaan"
fm = fm + "kers"
fm["mango"] = 20
print( len( fm ) )
print( fm )
print( "banaan" in fm )
print( "doerian" in fm )
fm -= "appel"
fm -= "banaan"
fm = fm - "kers"
fm -= "doerian"
print( fm )
print( "banaan" in fm )
fm["mango"] = 0
print( fm )