import turtle
turtle.speed(1)

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
ponto = input("Ponto a ser testado:").split()
coordenadaPonto = []
for t in ponto:
  coordenadaPonto.append(int(t))

listaX.append(listaX[0])
listaY.append(listaY[0])
tamanholista = len(listaX)

for i in range(tamanholista):
  if i == 0:
    turtle.penup()
    turtle.goto(listaX[i], listaY[i])
    turtle.pendown()
  else:
    turtle.goto(listaX[i], listaY[i])

listaX.pop(tamanholista-1)
listaY.pop(tamanholista-1)

tamanhosomatorio = len(listaX)
for pi in range(1, tamanhosomatorio):
  if pi == tamanhosomatorio-1:
    xvi = listaX[tamanhosomatorio-1] - coordenadaPonto[0]
    yvi = listaY[tamanhosomatorio-1] - coordenadaPonto[1]   
    xvimais1 = listaX[0] - listaX[tamanhosomatorio-1]
    yvimais1 = listaY[0] - listaY[tamanhosomatorio-1]
    teste = componente_z(xvi, yvi, xvimais1, yvimais1)
  elif pi <= tamanhosomatorio-1:
    xvi = listaX[pi-1] - coordenadaPonto[0]
    yvi = listaY[pi-1] - coordenadaPonto[1]
    xvimais1 = listaX[pi] - listaX[pi-1]
    yvimais1 = listaY[pi] - listaY[pi-1]
    teste = componente_z(xvi, yvi, xvimais1, yvimais1)
  if teste == True:
    a = "vermelho"
    print('Ponto se encontra FORA do polígono')
    break
  if teste == False and pi != tamanhosomatorio-1:
    continue
  if pi == tamanhosomatorio-1:
    a = "verde"
    print('Ponto se encontra DENTRO do polígono')
    
turtle.penup()
turtle.goto(coordenadaPonto[0], coordenadaPonto[1])
turtle.pendown()
if a == "vermelho":
  turtle.color("red")
elif a == "verde":
  turtle.color("green")
turtle.dot(6)
turtle.hideturtle()

#(Outro polígono desenhado de forma anti-horária e convexo)
#Foi da questão da lista passada
#Valores em x: -10  10  15 20 17 10 -20
#Valores em y: -20 -20 -10  5 17 30  10

#(Outro polígono desenhado de forma anti-horária e convexo)
#Também foi da questão da lista passada
#Valores em x: 0 50 50
#Valores em y: 0 0 50

#(Outro polígono desenhado de forma anti-horária e convexo)
#Valores em x: 0 40 40 30 0
#Valores em y: 0 0 20 30 30

#(Seu polígono desenhado de forma anti-horária)
#x = -40 0 20 -20 -50 
#y = -30 -10 20 40 10

#(Seu polígono desenhado de forma horária [Foi a forma que vc desenhou])
#x = -50 -20 20 0 -40 y = 10 40 20 -10 -30
#[0,0], [0,7], [0,-7]