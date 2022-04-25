"""
Distances
"""

#import temperature             #error als niet __main__
from . import temperature       #altijd goed

def mile2km(dist):
    return dist * 1.609344

def km2mile(dist):
    return dist * 0.621371


def pound2kg(weight):
    return weight * 0.453592

def kg2pound(weight):
    return weight * 2.204623


if __name__ == "__main__":
    print(mile2km(1))
    #print(temperature.cels2fahr(30))

