import math

for i in range(10000):
  x = int(math.sqrt(i+100))
  y = int(math.sqrt(i+368))

  if((pow(x,2) == i+100) and (pow(y,2) == i+268)):
    print(i)

