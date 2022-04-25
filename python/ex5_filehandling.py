fnaam = 'supergroep.txt'
# of 'global fnaam = 'supergroep.txt' in schrijf_text()


def schrijf_tekst():

    fh = open(fnaam, 'w')

    fh.write("Crosby\n")
    fh.write("Stills\n")
    fh.write("Nash\n")
    fh.write("and Young, who always comes lately.")

    fh.close()

    print("\nKlaar met schrijven")


def lees_tekst():

    fh = open(fnaam)

#    print(fh.read())
    for regel in fh:
#        print(regel)    # Lege regels
        print(regel, end='')    # Lege regels

    fh.close()

    print("\nKlaar met lezen")


def lees_tekst_try():

    fnaam = 'super.txt'
    fh = None
    #fh = open(fnaam)
    #FileNotFoundError: [Errno 2] No such file or directory: 'super.txt'

    try:
        fh = open(fnaam)
        print(fh.read())
    except FileNotFoundError as ex:
        print(ex)
        #[Errno 2] No such file or directory: 'super.txt'
    except OSError as ex:
        print(ex)
    finally:
        if fh is not None:
            fh.close()
    print("\nKlaar met lezen")


def lees_tekst_with():

    fnaam = 'supergroep.txt'
    try:
        with open(fnaam) as fh:
                  print(fh.read())
    except OSError as ex:
        print(ex)
        #[Errno 2] No such file or directory: 'supergrep.txt'

    print("\nKlaar met lezen")


def lees_csv():
    import csv
    fnaam='Koffie_recensies.csv'
    fh = open(fnaam)
    rd =  csv.reader(fh)
##    fh = open(fnaam)
##    for regel in fh:
##        # <_io.TextIOWrapper name='Koffie_recensies.csv' mode='r' encoding='UTF-8'>
##        print(fh)
    for rij in rd:
##        print(rij)
        print(rij[0], rij[1])
    fh.close()

def lees_csv_dict():
    import csv
    fnaam='Koffie_recensies.csv'
    fh = open(fnaam)
    rd =  csv.DictReader(fh)
    print('%-12s %s  %s' % ('Vestiging', 'Schoon', 'Service'))
    for rij in rd:
#        print(rij)
        print('%-12s %6s  %7s' % (rij['Vestiging'], rij['Schoon'], rij['Service']))
    fh.close()

def schrijf_csv():
    import csv
    data = [
        ['Jitske', 7.0, 6.3, 8.5, 6.9],
        ['Jitse', 5.8, 5.4, 6.3, 9.8],
        ['Oetse', 5.9, 5.5, 6.4, 9.7],
        ['Tjerk', 8.5, 8.5, 8.5, 8.6]
    ]
    print(data)

    fnaam = "Cijfers.csv"
    fh = open(fnaam, 'w', newline='')

    wr = csv.writer(fh, quoting=csv.QUOTE_NONNUMERIC)
    wr.writerow(['Naam','Nederlands','Frans','Duits','Engels'])
    wr.writerows(data)
    #for row in data:
    #    wr.writerow(row)

    fh.close()
    print("\n*** Klaar met schrijven van: %s ***" % fnaam)

# --- script ---

#schrijf_tekst()

#lees_tekst()

#lees_tekst_try()

#lees_tekst_with()

#lees_csv()

#lees_csv_dict()

schrijf_csv()
