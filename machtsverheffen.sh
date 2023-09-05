#!/usr/bin/bash 

# NOVI: Datastructuren en Algoritmen: Dynamic Programming en Recursion
# Machtsverheffen, bereken 5^4 zonder machtsverheffen te gebruiken.

# Dit is geen recursie, maar iteratie :-( !

grondtal=5
exponent=4
result=1

macht () 
{
    result=$((result * grondtal))
}

for i in $(seq 1 $exponent); do
# for (( i=0; i<$exponent; i++ )); do
    echo "5^$i"
    macht
done 

echo "$result"
exit 0
