import xml.etree.ElementTree as ET
tree = ET.parse('dat.xml')
root = tree.getroot()

print(type(tree))
for elem in root:
   for subelem in elem:
      print(subelem.text)
