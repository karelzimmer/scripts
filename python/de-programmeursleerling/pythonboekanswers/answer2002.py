from datetime import date
from random import random

class Cursus:
    def __init__( self, naam, nummer ):
        self.naam = naam
        self.nummer = nummer
    def __repr__( self ):
        return "{}: {}".format( self.nummer, self.naam )

class Student:
    def __init__( self, achternaam, voornaam, geb_datum, anr):
        self.achternaam = achternaam
        self.voornaam = voornaam
        self.geboortedatum = geb_datum
        self.anr = anr
        self.cursussen = []
    def __str__( self ):
        return self.voornaam+" "+self.achternaam
    def age( self ):
        vandaag = date.today()
        jaren = vandaag.year - self.geboortedatum.year
        if vandaag.month < self.geboortedatum.month or \
            (vandaag.month == self.geboortedatum.month \
            and vandaag.day < self.geboortedatum.day):
            jaren -= 1
        return jaren
    def inschrijven( self, cursus ):
        if cursus not in self.cursussen:
            self.cursussen.append( cursus )
    
studenten = [ 
    Student( "Alikruik", "Adrie", date( 1989, 10, 3 ), 453211 ),
    Student( "Bonzo", "Beatrijs", date( 1991, 12, 29 ), 476239 ),
    Student( "Continuum", "Carola", date( 1992, 3, 7 ), 784322 ),
    Student( "Domoor", "Dirk", date( 1993, 7, 11 ), 995544 ) ]
cursussen =[
    Cursus( "Vinologie", 787656 ),
    Cursus( "Lepelbuigen voor gevorderden", 651121 ),
    Cursus( "Onderzoeksvaardigheden: Babbelen", 433231 )]

for student in studenten:
    for cursus in cursussen:
        if random() > 0.3:
            student.inschrijven( cursus )

for student in studenten:
    print( "{}: {} {} ({})".format( student.anr, 
        student.voornaam, student.achternaam, student.age() ) )
    if len( student.cursussen ) == 0:
        print( "\tNo cursussen" )
    for cursus in student.cursussen:
        print( "\t{}".format( cursus ) )