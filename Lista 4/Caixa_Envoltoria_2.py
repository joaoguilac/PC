import turtle
t = turtle.Turtle()
t.speed(10)
 
def pontos(): #Desenho da figura 
  global menor_x
  global maior_x
  global menor_y
  global maior_y
  global N 
  for i in range(N-1):
    X,Y = input("Digite as coordenadas dos pontos:").split()
    X = float(X)
    Y = float(Y)
    X, Y = X*20, Y*20
    t.goto(X,Y)
    t.color('red')
    t.dot(7)
    t.color('blue')
    if X < menor_x:
      menor_x = X
    elif X > maior_x:
      maior_x = X
    if Y < menor_y:
      menor_y = Y
    elif Y > maior_y:
      maior_y = Y
def caixa(): #Caixa envoltória do desenho
  t.penup()
  t.goto(menor_x,maior_y)
  t.pendown()
  t.goto(maior_x,maior_y)
  t.goto(maior_x,menor_y)
  t.goto(menor_x,menor_y)
  t.goto(menor_x,maior_y)
  t.color('red')
  t.dot(7)
  t.write('x1,y1')
      
t.hideturtle()
N = int(input('Digite o número N de pontos do polígono')) 
X,Y = input("Digite as coordenadas dos pontos:").split()
X = float(X)
Y = float(Y)
X, Y = X*20, Y*20
menor_x = X
maior_x = X
menor_y = Y
maior_y = Y
t.color('blue')
t.penup()
t.goto(X,Y)
t.pendown()
t.color('red')
t.dot(7)
t.color('blue')
pontos()
t.goto(X,Y)
caixa()
A = maior_y/20 - menor_y/20
L = maior_x/20 - menor_x/20
X1 = menor_x/20
Y1 = maior_y/20
print('Caixa: X1,Y1= ' + str(X1) + ',' + str(Y1) + '; A=' + str(A) + ', L=' + str(L) + ';')