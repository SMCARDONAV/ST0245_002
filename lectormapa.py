import csv

archivo = "calles_de_medellin_con_acoso.csv"
with open(archivo, newline= "") as f:
    datos = csv.reader(f)
    calles = list(datos) 

print(calles)