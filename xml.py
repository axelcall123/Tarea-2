import xml.etree.ElementTree as ET
xml = ET.parse('dat.xml')
root = xml.getroot()

print(type(xml))
for elem in root:
   for subelem in elem:
      print(subelem.text)

print("tipo: ", type(root))
