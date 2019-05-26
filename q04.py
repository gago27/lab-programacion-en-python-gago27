##
## Imprima la cantidad de registros por cada mes.
##
## 01,3
## 02,4
## 03,2
## 04,4
## 05,3
## 06,3
## 07,5
## 08,6
## 09,3
## 10,2
## 11,2
## 12,3
##
import glob
filenames = glob.glob("data.csv")
data = open("data.csv","r").readlines()
data = [line[:-1] for line in data]
data = [line.replace("\t",",") for line in data]
data = [line.split(",") for line in data]
datas = [line[2] for line in data]
datas = sorted([dates[5:7] for dates in datas])
datas0 = set(datas)
h = []
for i in datas0:
  j = [i]
  a = 0
  for m in datas:
    if m == i:
      a = a+1
  j= j+[a]
  h = sorted(h+[j])
for q in h:
  resp=str(q[0])+","+str(q[1])
  print(resp)
