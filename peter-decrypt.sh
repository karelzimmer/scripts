#!/usr/bin/bash

my_secret_key=5

function decrypt {
    result=""
    secret_string=$1
    secret_number=$2
    for (( i=0; i<${#secret_string}; i++ )); do
        # Extract one character from input one by one
        one=${secret_string:$i:1}
        # Convert ASCII/Unicode character to its decimal value
        ord=$(printf '%d' "'$one")
        # XOR between character decimal value and secret number/key
        xor=$(($ord ^ $secret_number ))
        # Convert decimal value to its ASCII/Unicode character representation
        chr=$(printf "\x$(printf %x $xor)\n")
        result=$result$chr
  done
  echo $result
}

decrypt 'alq%lv%``k%b`m`lh' $my_secret_key
# Uitkomst: dit is een geheim

decrypt 'dit is een geheim' $my_secret_key
# Uitkomst: alq%lv%``k%b`m`lh
