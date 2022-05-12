from random import choice

antwoord = [ "Dat is zeker", "Het is zeker zo", "Zonder twijfel", 
"Ja, zeker", "Je kunt erop vertrouwen", "Zoals ik het zie, ja", 
"Waarschijnlijk", "Ziet er goed uit", "Ja", "Lijkt van wel", 
"Vaag, probeer het nog eens", "Vraag later nog eens", "Kan ik \
beter niet zeggen", "Kan ik nu niet voorspellen", "Concentreer \
je en vraag nog eens", "Reken er maar niet op", "Ik zeg van \
niet", "Mijn bronnen zeggen van niet", "Lijkt er niet op", 
"Zeer twijfelachtig" ]

input( "Stel je vraag aan de magische bol: " )
print( "De magische bol zegt:", choice( antwoord ) )