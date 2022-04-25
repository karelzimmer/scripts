# Gegevens uit Macbeth.xml lezen met Python ElementTree en xpath

import xml.etree.ElementTree as ET

tree = ET.parse("Macbeth.xml")
root = tree.getroot()       #is niet de root /, maar documentelement <PLAY>
print("root.tag:", root.tag)        #PLAY
print()

#xpath = ".//PERSONA"
#xpath = "PERSONAE/PERSONA"
#xpath = "PERSONAE/PGROUP/PERSONA"
#xpath = "PERSONAE/PGROUP[1]/PERSONA"
#xpath = "ACT/TITLE"
#xpath = "ACT[TITLE='ACT I']/SCENE/TITLE"
#xpath = ".//SPEECH[SPEAKER='Old Man']/LINE"
#xpath = "ACT/SCENE/SPEECH[SPEAKER='Old Man']/LINE"
#xpath = "ACT/SCENE/SPEECH[SPEAKER='DUNCAN']/LINE"
xpath = "ACT[5]/SCENE[5]/SPEECH[SPEAKER='MACBETH']/LINE"
#xpath = 


lst = root.findall(xpath)       #->lst met elems
for elem in lst:
    print(elem.text)
    #print(ET.dump(elem))

