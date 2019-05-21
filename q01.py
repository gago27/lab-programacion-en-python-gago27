##
## Imprima la suma de la segunda columna.
##
import glob
filenames = glob.glob("data.csv")
data = open("data.csv","r").readlines()
data = [line[:-1] for line in data]
data = [line.replace("\t", ",") for line in data]
data = [line.split(",") for line in data]
data = [line[1] for line in data]
a = 0
for row in data:
  a= a+ int(row)
print(a)
