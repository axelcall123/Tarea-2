import csv

with open('names.csv') as file:
    datos = csv.reader(file)
    for reg in datos:
        print(reg)
#https://python-para-impacientes.blogspot.com/2015/05/operaciones-con-archivos-csv.html
