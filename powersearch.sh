#!/usr/bin/bash

# Vanaf home directory worden alle directories en files gezocht die ongeldige tekens bevatten

#--------------------------------------------------------------------------#
# Ga naar home directory.                                                  #
#--------------------------------------------------------------------------#
cd ~

#--------------------------------------------------------------------------#
# Zoek naar files met foutieve tekens en rapporteer type, naam, en fout.   #
#--------------------------------------------------------------------------#
while IFS= read -r -d $'\0' file
do
    badname=$(echo $(basename "$file") | \
              tr --delete [:alnum:][:blank:][=\/=][=-=][=_=][=.=][=~=])
    if [ ! -z $badname ]
    then
        echo "$(file --brief "$file") '$file' bevat: $badname"
    fi
done < <(find . -print0)
exit
#EOF
