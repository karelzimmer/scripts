import xml.etree.ElementTree as ET

# Load an XML document and get the root element, i.e. <Company>.
tree = ET.parse("company.xml")
root = tree.getroot()

emp = ET.Element("Employee")
emp.set("EmpNum", "ZZ123")
emp.set("JobTitle", "Rollercoaster designer")
root.append(emp)

firstname = ET.Element("FirstName")
firstname.text = "Zak"
lastname = ET.Element("LastName")
lastname.text = "Thunderbolt"

name = ET.Element("Name")
name.append(firstname)
name.append(lastname)
emp.append(name)

tel = ET.Element("Tel")
tel.text = "222-7777-999"
emp.append(tel)

sal = ET.Element("Salary")
sal.text = "250000"
emp.append(sal)

tree.write("UpdatedCompany.xml")
