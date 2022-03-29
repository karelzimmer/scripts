#!/usr/bin/env python

my_secret_key = 5

def decrypt ( secret_string , secret_number ) :

  result = ""

  for x in secret_string :

    result = result+chr( ord ( x ) ^ int (secret_number) )

  return result

print(decrypt("alq%lv%``k%b`m`lh" , my_secret_key ) )

print(decrypt("dit is een geheim" , my_secret_key ) )

