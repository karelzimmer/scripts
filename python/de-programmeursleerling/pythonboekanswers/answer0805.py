from pcinput import getInteger

def getNummer( prompt ):
    while True:
        num = getInteger( prompt )
        if num < 0 or num > 1000:
            print( "Geef een getal tussen 1 en 1000" )
            continue
        return num

def main():
    while True:
        x = getNummer( "Geef nummer 1: " )
        if x == 0:
            break
        y = getNummer( "Geef nummer 2: " )
        if y == 0:
            break
        if x%y == 0 or y%x == 0:
            print( "Fout: de nummers mogen geen delers zijn" )
            return
        print( "Vermenigvuldiging van",x,"met",y,"geeft",x*y )
    print( "Tot ziens!" )

if __name__ == '__main__':
    main()