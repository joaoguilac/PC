import turtle
def componente_z(xi, yi, ximais1, yimais1):
  vz = (xi * yimais1) - (yi * ximais1)
  return vz
  
def existe(x, y, ponto1, ponto2):
  for i, t in enumerate(x):
    if ponto1 == t:  
      return True
  for i, t in enumerate(y):
    if ponto2 == t:
      return False
  

x = input("Valores em x:")
x = x.split()
listaX = []
for t in x:
  listaX.append(int(t))
y = input("Valores em y:")
y = y.split()
listaY = []
for t in y:
  listaY.append(int(t))

listaX.append(listaX[0])
listaY.append(listaY[0])
tamanholista = len(listaX)

turtle.begin_fill()
for i in range(tamanholista):
  if i == 0:
    turtle.penup()
    turtle.goto(listaX[i]*2, listaY[i]*2)
    turtle.pendown()
  else:
    turtle.goto(listaX[i]*2, listaY[i]*2)
turtle.end_fill()

a = 0
tamanhosomatorio = len(listaX) - 1
contador = 0
while contador > tamanhosomatorio:  
#for i in range(tamanhosomatorio):
  a = a + componente_z(listaX[contador], listaY[contador], listaX[contador+1], listaY[contador+1]) / 2
  contador = contador + 1
print('A área é ' + str(a))