import turtle
def componente_z(xi, yi, ximais1, yimais1):
  vz = (xi * yimais1) - (yi * ximais1)
  if vz < 0:
    return True
  else:
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

for i in range(tamanholista):
  if i == 0:
    turtle.penup()
    turtle.goto(listaX[i]*2, listaY[i]*2)
    turtle.pendown()
    turtle.begin_fill()
  else:
    turtle.goto(listaX[i]*2, listaY[i]*2)
turtle.end_fill()
turtle.hideturtle()

listaX.append(listaX[0])
listaX.pop(0)
listaY.append(listaY[0])
listaY.pop(0)

tamanhosomatorio = len(listaX) - 1
for pi in range(tamanhosomatorio):
  xvi = listaX[pi] - listaX[pi-1]
  yvi = listaY[pi] - listaY[pi-1]
  xvimais1 = listaX[pi+1] - listaX[pi]
  yvimais1 = listaY[pi+1] - listaY[pi]
  teste = componente_z(xvi, yvi, xvimais1, yvimais1)
  if teste == True:
    print('CÔNCAVO')
    break
  if teste == False and pi != tamanhosomatorio-1:
    continue
  if pi == tamanhosomatorio-1:
    print('CONVEXO')
    
#Valores em x: -30 -10 60  30 -40
#Valores em y: -20  40 10 100  90
#CÔNCAVO