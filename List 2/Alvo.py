import math
x = int(input('x ='))
y = int(input('y ='))
d = math.sqrt((x**2) + (y**2))
if d >= 0 and d <= 25:
  if d % 2 == 0:
    print('200 pontos')
  else:
    print('100 pontos')
elif d > 25 and d <= 50:
  print('70 pontos')
elif d > 50 and d <= 75:
  print('40 pontos')
elif d > 75 and d <= 100:
  print('10 pontos')
elif d > 100:
  print('0 pontos')

import turtle
t = turtle.Turtle()
t.speed(10)
tela = turtle.Screen()
tela.bgcolor("dark magenta")
#parte preta
t.penup()
t.goto(0,-100)
t.pendown()
t.color('black')
t.begin_fill()
t.circle(100)
t.end_fill()
#parte azul
t.penup()
t.goto(0,-75)
t.pendown()
t.color('blue')
t.begin_fill()
t.circle(75)
t.end_fill()
#parte vermelha
t.color('red')
t.penup()
t.goto(0,-50)
t.pendown()
t.begin_fill()
t.circle(50)
t.end_fill()
#parte amarela
t.color('yellow')
t.penup()
t.goto(0,-25)
t.pendown()
t.begin_fill()
t.circle(25)
t.end_fill()
#ponto
t.penup()
t.goto(x,y)
t.pendown()
t.color('white')
t.dot(10)
t.hideturtle()