import xml.etree.ElementTree as ET
xml = ET.parse('dat.xml')
root = xml.getroot()

print(type(xml))
for elem in root:
   for subelem in elem:
      print(subelem.text)

print("tipo: ", type(root))


import json
with open('dat.json','r') as miarchivo:
    datos=miarchivo.read()
objeto=json.loads(datos)
#for i in objeto['nombre']:
for i in objeto:
    for a in objeto[i]:
        print(a)
    #print(i)
print("tipo: ", type(objeto))


import csv
with open('names.csv') as file:
    csvss = csv.reader(file)
    for reg in csvss:
        print(reg[0], reg[1], reg[2], reg[3])
print("tipo: ", type(csvss))
