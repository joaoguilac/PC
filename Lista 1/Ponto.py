#Pertence ou não
x = float(input('x ='))
y = float(input('y ='))
if x >= 0 and y >= 0 and (x ** 2) + (y ** 2) <= 1:
  print('pertence')
else:
  print('não pertence')

#Escala
x2 = x * 60
y2 = y * 60

#Desenho da figura
import turtle
t = turtle.Turtle()
t.begin_fill()
t.forward(60)
t.left(90)
t.color("blue")
t.circle(60, 90)
t.left(90)
t.forward(60)
t.end_fill()

#Plano cartesiano
t.color('gray')
t.penup()
t.goto(-10,0)
t.pendown()
t.left(90)
t.forward(120)
t.penup()
t.goto(0,-10)
t.pendown()
t.left(90)
t.forward(120)
t.penup()
t.goto(90,0)
t.pendown()

#Ponto
t.penup()
t.goto(x2,y2)
t.pendown()
t.color('black')
t.dot(5)
t.hideturtle()