##
## Por cada clave de la columna 5 (cadena de tres letras), obtenga
## el valor mas pequeño y el valor mas grande asociado a esa clave.
##
## aaa,0,6
## bbb,4,7
## ccc,0,1
## ddd,5,5
## eee,0,0
## fff,4,9
## ggg,3,3
## hhh,6,8
## iii,2,7
## jjj,2,5
##
import glob
filenames=glob.glob("data.csv")
data = open("data.csv", "r").readlines()
data = [line[:-1] for line in data]
data = [line.replace("\t", ",") for line in data]
data = [line.split(",") for line in data]
data = [line[5:] for line in data]
datas=[]
for line in data:
  row = []
  for x in line:
    if len(x)==5:
      row.append(x)
  datas.append(row)
datas0 = []
for i in datas:
  for a in i:
    datas0.append(a)
datas0 = sorted(datas0)
datas1 = []
datas2=[line.replace(":",",") for line in datas0]
datas2=[line.split(",") for line in datas2]
otro = set([line[0]for line in datas2])
nuevo = []
for x in otro:
  let=[x]
  for este in datas2:
    if este[0]==x:
      let.append(este[1])
  nuevo= nuevo+[let]
an= []
for fila in nuevo:
  casi = [fila[0], min(fila), max(fila[1:])]
  an= an + [casi]
an = sorted(an) 
for y in an:
  resp= y[0]+","+y[1]+","+y[2]
  print(resp)
