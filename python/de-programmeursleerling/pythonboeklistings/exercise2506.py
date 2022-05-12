import re

tekst = "<html><head><title>Lijst van personen met ids</title>\
</head><body>\
<p><id>123123123</id><naam>Groucho Marx</naam>\
<p><id>123123124</id><naam>Harpo Marx</naam>\
<p><id>123123125</id><naam>Chico Marx</naam>\
<randomcrap>Etaoin<id>Shrdlu</id>qwerty</naam></randomcrap>\
<nocrap><p><id>123123126</id><naam>Zeppo Marx</naam></nocrap>\
<address>Chicago</address>\
<morerandomcrap><id>999999999</id>geennaamtezien!\
</morerandomcrap>\
<p><id>123123127</id><naam>Gummo Marx</naam>\
<note>Zoek hem op via <a href=\"http://www.google.com\">\
Google.</a></note>\
</body></html>"