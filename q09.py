##
## Genere una lista de tuplas, donde cada tupla contiene en la primera 
## posicion, el valor de la segunda columna; la segunda parte de la 
## tupla es una lista con las letras (ordenadas y sin repetir letra) 
## de la primera  columna que aparecen asociadas a dicho valor de la 
## segunda columna. Esto es:
##
## ('0', ['C'])
## ('1', ['A', 'B', 'D', 'E'])
## ('2', ['A', 'D', 'E'])
## ('3', ['A', 'B', 'D', 'E'])
## ('4', ['B', 'E'])
## ('5', ['B', 'C', 'D', 'E'])
## ('6', ['A', 'B', 'C', 'E'])
## ('7', ['A', 'C', 'D', 'E'])
## ('8', ['A', 'B', 'E'])
## ('9', ['A', 'B', 'C', 'E'])
##
##
import glob
filenames = glob.glob("data.csv")
data= open("data.csv", "r").readlines()
data = [line.replace("\t",",") for line in data]
data = [line.split(",") for line in data]
data = sorted([[line[1], line[0]] for line in data])
datas = set([line[0] for line in data])
uno = []
for num in datas:
  x = [num]
  y = []
  
  for ind in data:
    
    if num == ind[0]:
      y.append(ind[1])
  y = set(y)
  for line in y:
    x = sorted(x+[line])
  uno = uno+[x]
uno = sorted(uno)
for row in uno:
  dos = row[1:]
  tres=(row[0],dos)
  print(tres)
