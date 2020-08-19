import json
with open('dat.json','r') as miarchivo:
    datos=miarchivo.read()
objeto=json.loads(datos)
#for i in objeto['nombre']:
for i in objeto:
    for a in objeto[i]:
        print(a)
    #print(i)
print(type(miarchivo))
