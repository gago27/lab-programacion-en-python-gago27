##
## Imprima una tabla en formato CSV que contenga por registro,
## la cantidad de elementos de las columnas 4 y 5
## (filas en el archivo)
##
## E,3,5
## A,3,4
## B,4,4
## ...
## C,4,3
## E,2,3
## E,3,3
##
import glob
import csv
filenames= glob.glob("data.csv")
data= open("data.csv", "r").readlines()
data= [line[:-1] for line in data]
data = [line.replace("\t", ",") for line in data]
data= [line.split(",") for line in data]
datas2= [line[0] for line in data]
datas= [line[3:] for line in data]
datas1= [[row for row in line if len(row)==1] for line in datas]
datas3= [[row for row in line if len(row)==5] for line in datas]
datas4= [[datas2[i],len(datas1[i]),len(datas3[i])] for i in range(len(datas))]

file= glob.glob("respuesta.csv")
files= open("respuesta.csv", "w")
x = csv.writer(files, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
for i in range(len(datas4)):
  x.writerow(datas4[i])
print(open("respuesta.csv","r").read())
