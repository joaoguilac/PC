import turtle
import math
t = turtle.Turtle()

def distancia(x0, y0, indice): #Define a distância mínima entre dois pontos
  global dbase
  for j in range(pontos):
    if indice != j:
      d = math.sqrt((x0 - listaX[j])**2 + (y0 - listaY[j])**2)
      if d < dbase:
        dbase = d

def pontosmaisproximos(x1, y1, indice2): #Define os pontos mais próximos
  for l in range(pontos):
    if indice2 != l:
      teste = math.sqrt((x1 - listaX[l])**2 + (y1 - listaY[l])**2)
      if teste == dbase:
        print('Pontos mais próximos:'),
        print(x1, y1),
        print(listaX[l], listaY[l])
        return True
        break

pontos = int(input("Quantos pontos?"))
print("Digite os " + str(pontos) + " pontos:")
listaX = []
listaY = []
for i in range(pontos):
  x, y = input().split() 
  x = int(x) 
  y = int(y)
  listaX.append(x)
  listaY.append(y)

dbase = math.sqrt((listaX[0] - listaX[1])**2 + (listaY[0] - listaY[1])**2)
for i in range(pontos):
  distancia(listaX[i], listaY[i], i)

for id in range(pontos): 
  retorno = pontosmaisproximos(listaX[id], listaY[id], id)
  if retorno == True:
    break

condicao = False
for m in range(pontos):  
  for k in range(pontos):
    teste = math.sqrt((listaX[m] - listaX[k])**2 + (listaY[m] - listaY[k])**2)
    if teste == dbase:
      a = listaX[m]
      b = listaY[m]
      c = listaX[k]
      d = listaY[k]
      condicao = True
      break
  if condicao == True:
    break

#Desenho dos pontos
for e in range(pontos):
  t.color("black")
  if listaX[e] == a and listaY[e] == b:
    t.color("red")
  elif listaX[e] == c and listaY[e] == d:
    t.color("red")
  t.penup()
  t.goto(listaX[e],listaY[e])
  t.pendown()
  t.dot(10)
t.hideturtle()