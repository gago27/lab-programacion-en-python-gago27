##
## Imprima una tabla en formato CSV que contenga por cada clave 
## de la columna 5, la correspondiente cantidad de registros 
## asociados (filas en el archivo)
##
## aaa,13
## bbb,16
## ccc,23
## ddd,23
## eee,15
## fff,20
## ggg,13
## hhh,16
## iii,18
## jjj,18
##
##
import glob
import csv 
filenames = glob.glob("data.csv")
data = open("data.csv", "r").readlines()
data = [line[:-1] for line in data]
data = [line.replace("\t",",") for line in data]
data = [line.split(",") for line in data]
data = [line[5:] for line in data]
data = [[row for row in line if len(row)==5] for line in data]
data = [[row[0:3] for row in line] for line in data]
datas = []
for line in data:
  for row in line:
    datas.append(row)
datas = sorted(datas)
datas0 = set(datas)
datas0 = [line for line in datas0]
datas0 = sorted(datas0)
tabla=[]
for a in datas0:
  b = datas.count(a)
  fila=[a,b]
  tabla= tabla+[fila]

file2 = glob.glob("data1.csv*")
data1 = open("data1.csv", "w")
x = csv.writer(data1, delimiter=",",quoting=csv.QUOTE_NONNUMERIC)
for i in range(len(tabla)):
  x.writerow(tabla[i])
print(open("data1.csv","r").read())
