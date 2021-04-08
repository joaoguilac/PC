degraus_decrescente = int(input('Degraus da escada decrescente:'))
degraus_crescente = int(input('Degraus da escada crescente:'))

import turtle
t = turtle.Turtle()
t.speed(10)
def degrau(d,c): #Escada inteira
  for i in range(d): #Escada decrescente
    x = i*15
    y = -i*10
    t.penup()
    t.goto(-175+x,y)
    t.pendown()
    t.color('royal blue')
    t.begin_fill()
    for j in range(2): #Desenho de cada degrau 
      t.forward(30)
      t.right(90)
      t.forward(10)
      t.right(90)
    t.end_fill() 
  for k in range(c): #Escada crescente
    d2 = d-1
    x2 = (d2*15) + 30 + (k*15)
    y2 = (-d2*10) + (k*10) 
    t.penup()
    t.goto(-175+x2,y2)
    t.pendown()
    t.color('red')
    t.begin_fill()
    for j in range(2): #Desenho de cada degrau 
      t.forward(30)
      t.right(90)
      t.forward(10)
      t.right(90)
    t.end_fill() 

degrau(degraus_decrescente, degraus_crescente)