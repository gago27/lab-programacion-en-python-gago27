##
## Genere una lista de tuplas, donde cada tupla contiene en la primera 
## posicion, el valor de la segunda columna; la segunda parte de la 
## tupla es una lista con las letras (ordenadas) de la primera 
## columna que aparecen asociadas a dicho valor de la segunda 
## columna. Esto es:
##
## ('0', ['C'])
## ('1', ['A', 'A', 'B', 'D', 'E', 'E'])
## ('2', ['A', 'D', 'E'])
## ('3', ['A', 'B', 'D', 'E', 'E'])
## ('4', ['B', 'E'])
## ('5', ['B', 'C', 'D', 'D', 'E', 'E', 'E'])
## ('6', ['A', 'B', 'C', 'E'])
## ('7', ['A', 'C', 'D', 'E'])
## ('8', ['A', 'B', 'E', 'E'])
## ('9', ['A', 'B', 'C', 'E'])
##
##
import glob
filenames = glob.glob("data.csv")
data = open("data.csv", "r").readlines()
data = [line[:-1] for line in data]
data = [line.replace("\t",",") for line in data]
data = [line.split(",") for line in data]
data = sorted([[line[1], line[0]] for line in data])
datas = set([line[0] for line in data])
uno = []
for num in datas:
  x = [num]
  for ind in data:
    if num == ind[0]:
      x.append(ind[1])
  x = [y for y in x]
  uno = uno+[x]
cuatro = [line[0] for line in uno]
cinco = [line[1:] for line in uno]
dos=[]
for i in range(0, len(uno)):
  tres= (cuatro[i], cinco[i])
  dos = dos+[tres]
dos = sorted(dos)
for line in dos:
  print(line)
