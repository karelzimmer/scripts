class Voertuig:
    def __init__( self ):
        self.startpunt = []
        self.eindpunten = []
        self.werkwoord = ""
        self.naam = ""
    def __str__( self ):
        return self.naam
    def isStartpunt( self, p ):
        return NotImplemented
    def isEindpunt( self, p ):
        return NotImplemented
    def snelheid( self, p1, p2 ):
        return NotImplemented
    def reisWerkwoord( self ):
        return NotImplemented