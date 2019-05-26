##
## Imprima el valor maximo y minimo por cada letra de la columa 1.
##
## A,9,1
## B,9,1
## C,9,0
## D,7,1
## E,9,1
##
import glob
filenames= glob.glob("data.csv")
data = open("data.csv", "r").readlines()
data = [line[:-1] for line in data]
data = [line.replace("\t",",") for line in data]
data = [line.split(",") for line in data]
data = sorted([[line[0], line[1]] for line in data])
datas = [line[0] for line in data]
datas = set(datas)
fin=[]
for letra in datas:
  h = []
  for m in data:
    if letra == m[0]:
      h = h+[m[1]]
  j = [letra, max(h), min(h)]
  fin=fin+[j]
fin = sorted(fin)
for ya in fin:
  resp= ya[0]+","+str(ya[1])+","+str(ya[2])
  print(resp)
