#!/usr/bin/bash

# vervang 2 of meer lege regels door 1 lege regel

cd ~/scripts || exit

for file in *; do
    cat --squeeze-blank "$file" > "/tmp/$file"
    mv "/tmp/$file" "$file"
done
