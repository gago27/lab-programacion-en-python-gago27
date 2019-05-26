##
## Imprima por cada fila, la columna 1 y la suma de los valores
## de la columna 5
##
## E,22
## A,14
## B,14
## ....
## C,8
## E,11
## E,16
##
import glob
filenames= glob.glob("data.csv")
data = open("data.csv","r").readlines()
data = [line[:-1] for line in data]
data = [line.replace("\t",",") for line in data]
data = [line.split(",") for line in data]
letras = [line[0] for line in data]
columna = [line[5:] for line in data]
columna = [[row for row in line if len(row)==5] for line in columna]
columna = [[int(row[4]) for row in line] for line in columna]
numeros=[]
for row in columna:
  a=0
  for num in row:
    a = a+num
  numeros.append(a)
numeros
for i in range(len(numeros)):
  resp= str(letras[i])+","+str(numeros[i])
  print(resp)
