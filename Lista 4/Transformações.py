import turtle
import math
t = turtle.Turtle()
t.speed(10)

def retanguloR(X, Y, L, A):
  X = X*5
  Y = Y*5
  L = L*5
  A = A*5
  t.color('purple')
  t.penup()
  t.goto(X,Y)
  t.pendown()
  t.goto(X+L,Y)
  t.goto(X+L,Y-A)
  t.goto(X,Y-A)
  t.goto(X,Y)
  t.color('black')
  t.penup()
  t.goto(-190,0)
  t.pendown()
  t.goto(190,0)
  t.write('x')
  t.penup()
  t.goto(0,-190)
  t.pendown()
  t.goto(0,190)
  t.write('y')

def rotacao(X, Y, L, A):
  X = X*5
  Y = Y*5
  L = L*5
  A = A*5
  o = int(input('Ângulo de rotação:'))
  o = math.radians(o)
  seno_o = math.sin(o)
  cos_o = math.cos(o)  
  t.color('blue')
  t.pensize(5)
  Pnx = X*cos_o - Y*seno_o
  Pny = X*seno_o + Y*cos_o
  t.penup()
  t.goto(Pnx,Pny)
  t.pendown()
  Pnx = (X+L)*cos_o - (Y)*seno_o
  Pny = (X+L)*seno_o + (Y)*cos_o
  t.goto(Pnx,Pny)
  Pnx = (X+L)*cos_o - (Y-A)*seno_o
  Pny = (X+L)*seno_o + (Y-A)*cos_o
  t.goto(Pnx,Pny)
  Pnx = (X)*cos_o - (Y-A)*seno_o
  Pny = (X)*seno_o + (Y-A)*cos_o
  t.goto(Pnx,Pny)
  Pnx = (X)*cos_o - (Y)*seno_o
  Pny = (X)*seno_o + (Y)*cos_o
  t.goto(Pnx,Pny)

def translacao(X, Y, L, A):
  X = X*5
  Y = Y*5
  L = L*5
  A = A*5
  xt = int(input('xt:'))
  yt = int(input('yt:'))
  xt = xt*5
  yt = yt*5
  Pnx = X + xt
  Pny = Y + yt
  t.color('blue')
  t.pensize(5)
  t.penup()
  t.goto(Pnx,Pny)
  t.pendown()
  t.goto(Pnx+L,Pny)
  t.goto(Pnx+L,Pny-A)
  t.goto(Pnx,Pny-A)
  t.goto(Pnx,Pny)

def opcao3(X, Y, L, A):
  X = X*5
  Y = Y*5
  L = L*5
  A = A*5
  o = int(input('Ângulo de rotação:'))
  o = math.radians(o)
  seno_o = math.sin(o)
  cos_o = math.cos(o)  
  xt = int(input('xt:'))
  yt = int(input('yt:'))
  xt = xt*5
  yt = yt*5
  t.color('blue')
  t.pensize(5)
  Pnx = X*cos_o - Y*seno_o
  Pny = X*seno_o + Y*cos_o
  Pnx = Pnx + xt
  Pny = Pny + yt
  t.penup()
  t.goto(Pnx,Pny)
  t.pendown()
  Pnx = (X+L)*cos_o - Y*seno_o
  Pny = (X+L)*seno_o + Y*cos_o
  Pnx = Pnx + xt
  Pny = Pny + yt
  t.goto(Pnx,Pny)
  Pnx = (X+L)*cos_o - (Y-A)*seno_o
  Pny = (X+L)*seno_o + (Y-A)*cos_o
  Pnx = Pnx + xt
  Pny = Pny + yt
  t.goto(Pnx,Pny)
  Pnx = (X)*cos_o - (Y-A)*seno_o
  Pny = (X)*seno_o + (Y-A)*cos_o
  Pnx = Pnx + xt
  Pny = Pny + yt
  t.goto(Pnx,Pny)
  Pnx = (X)*cos_o - (Y)*seno_o
  Pny = (X)*seno_o + (Y)*cos_o
  Pnx = Pnx + xt
  Pny = Pny + yt
  t.goto(Pnx,Pny)
  
def opcao4(X, Y, L, A):
  X = X*5
  Y = Y*5
  L = L*5
  A = A*5
  xt = int(input('xt:'))
  yt = int(input('yt:'))
  xt = xt*5
  yt = yt*5
  o = int(input('Ângulo de rotação:'))
  t.left(o)
  o = math.radians(o)
  seno_o = math.sin(o)
  cos_o = math.cos(o)
  Pnx1 = X + xt
  Pny1 = Y + yt
  Pnx = Pnx1*cos_o - Pny1*seno_o
  Pny = Pnx1*seno_o + Pny1*cos_o 
  t.penup()
  t.goto(Pnx,Pny)
  t.pendown()
  t.color('blue')
  t.pensize(5)
  for i in range(2):
    t.forward(L)
    t.right(90)
    t.forward(A)
    t.right(90)


retanguloR(-10, 10, 20, 20)
print('1-Rotação, 2-Translação, 3-rotação > translação, 4-translação > rotação.')
escolha = int(input('Escolha:'))
if escolha == 1:
  rotacao(-10, 10, 20, 20)
elif escolha == 2:
  translacao(-10, 10, 20, 20)
elif escolha == 3:
  opcao3(-10, 10, 20, 20)
elif escolha == 4:
  opcao4(-10, 10, 20, 20)
t.hideturtle()