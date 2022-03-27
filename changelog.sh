#!/bin/bash

# Vervang SP tussen vier velden door ':' in CHANGELOG
# Dus van 'veld1 veld2 veld3 veld4' naar 'veld1Lveld2:veld3:veld4'
# Voorbeeld:
# archive 16.04.00 2020-01-25 Gecomprimeerde CHANGELOG
# ->
# archive:16.04.00:2020-01-25:Gecomprimeerde CHANGELOG

cd ~/kzscripts

while read record;do
    part1=$(echo "$record"|awk '{print $1}')
    part2=$(echo "$record"|awk '{print $2}')
    part3=$(echo "$record"|awk '{print $3}')
    # Die '$1=$2=$3=""' om deze velden leeg te maken, daarom weer 'print substr'.
    part4=$(echo "$record"|awk '{$1=$2=$3=""; print substr($0,4)}')
    echo "${part1}:${part2}:${part3}:${part4}" >> CHANGELOG.new
done < CHANGELOG
