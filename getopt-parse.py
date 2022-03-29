#!/usr/bin/python3

"""
Parse Input.
"""

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-u", "--usage",  action="store_true",
                    help="Een korte gebruikssamenvatting tonen")
parser.add_argument("-g", "--gui",  action="store_true",
                    help="Start in grafische modus")
args = parser.parse_args()

if args.usage:
    print("Gebruik: kzpwgen [-g|--gui] [-h|--help] [-u|--usage]")
elif args.gui:
    cont = input("Druk op de Enter-toets om verder te gaan [Enter]: ")
