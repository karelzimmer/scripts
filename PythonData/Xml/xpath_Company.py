#je kan ook lxml importeren; wheel niet nodig(?)
#pip install lxml

#import xml.etree.ElementTree as ET
import lxml.etree as ET

# Load an XML document and get the root element, i.e. <Company>.
tree = ET.parse("company.xml")
root = tree.getroot()

# Find all <Salary> elements.
sals = root.findall("Employee/Salary")
print("All salaries:")
for sal in sals:
    print("  %s" % sal.text)
    
# Find the <Salary> for employee[2].
salEmp2 = root.find("Employee[2]/Salary")
print("\nSalary for employee[2] is %s" % salEmp2.text)

# Find the full names of all salaried employees.
names = root.findall("Employee[Salary]/Name")
print("\nFull names of all salaried employees:")
for name in names:
    print("  %s %s" % (name.find("FirstName").text, name.find("LastName").text))

# Find the <Salary> for all programmers.
sals = root.findall("Employee[@JobTitle='Programmer']/Salary")
print("\nSalary of all programmers:")
for sal in sals:
    print("  %s" % sal.text)

# Find the <Tel> for all employees.
tels = root.findall(".//Tel")       #lxml eist ook .//
print("\nTelephone numbers for all employees:")
for tel in tels:
    print("  %s" % tel.text)
