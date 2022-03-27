#!/bin/bash 

# Fibonacci sequence 
# Elk element van de rij is steeds de som van de twee voorgaande elementen,
# beginnend met 0 en 1

MAX=20     # a constant, denoting Number of terms (+1) to generate. 
MIN=2      # another constant. 
           #If index is less than 2, then Fibo(index) = index. 

Fibonacci () 
{ 
  fsn=$1   
  if [ "$fsn" -lt "$MIN" ] 
  then 
    echo "$fsn"  # First two terms are 0 1 ... see above. 
  else 
    (( --fsn ))  # j-1 
    term1=$( Fibonacci $fsn )   #  Fibo(j-1) 

    (( --fsn ))  # j-2 
    term2=$( Fibonacci $fsn )   #  Fibo(j-2) 

    echo $(( term1 + term2 )) 
  fi 
}

for i in $(seq 0 $MAX) 
do  # Calculate $MAX+1 terms. 
  FIBO=$(Fibonacci $i) 
  echo -n "$FIBO " 
done 
# expected output:
#  0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765

echo  " "
exit 0
