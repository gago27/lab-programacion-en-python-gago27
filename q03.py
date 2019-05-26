##
## Imprima la suma de la columna 2 por cada letra de la 
## primera columna, ordneados alfabeticamente.
##
## A,37
## B,36
## C,27
## D,23
## E,67
##
import glob
filenames = glob.glob("data.csv")
data = open("data.csv","r").readlines()
data = [line[:-1] for line in data]
data = [line.replace("\t",",") for line in data]
data = [line.split(",") for line in data]
data = [[line[0], line[1]] for line in data]
data = sorted(data)
datas = set([line[0] for line in data])
datas0 = []
h =[]
for i in datas:
  a = 0
  for m in data:
    if m[0] == i:
      a = a + int(m[1])
  h = h +[[i, a]]
datas0= datas0 + h
datas0 = sorted(datas0)
for q in datas0:
  resp = str(q[0])+","+str(q[1])
  print(resp)
