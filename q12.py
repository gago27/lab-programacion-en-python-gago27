##
## Imprima la suma de la columna 2 por cada letra 
## de la columna 4, ordnados alfabeticamente.
##
## a,114
## b,40
## c,91
## d,65
## e,79
## f,110
## g,35
##
import glob
filenames = glob.glob("data.csv")
data = open("data.csv", "r").readlines()
data = [line[:-1] for line in data]
data = [line.replace("\t",",") for line in data]
data = [line.split(",") for line in data]
datas = [[row for row in line if len(row)==1] for line in data]
datas = [line[1:] for line in datas]
datas1 = [line[2:] for line in datas]
a = []
for i in datas1:
  for m in i:
    a = a+[m]
a= set(a)
a= list(a)
a= sorted(a)
resp=[]
for letra in a:
  inic=[letra]
  count=0
  for row in datas:
    if letra in row:
      count= count+int(row[0])
  inic= inic+[count]
  resp= resp+[inic]
for line in resp:
  soluc= line[0]+","+str(line[1])
  print(soluc)
