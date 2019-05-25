##
## Imprima la cantidad de registros por letra para la 
## primera columna, ordenados alfabeticamente.
##
## A,8
## B,7
## C,5
## D,6
## E,14
##
import glob
filenames = glob.glob("data.csv")
data = open("data.csv","r").readlines()
data = [line[:-1] for line in data]
data = [line.replace("\t", ",") for line in data]
data = [line.split(",") for line in data]
data = [line[0] for line in data]
datas = set([line[0] for line in data])
b = []
for i in datas:
  a = 0
  for m in data:
    if i == m:
      a = a+1
  b.append((i,a))
b = sorted(b)
for h in b:
  resp= h[0]+","+str(h[1])
  print(resp)
