import random
import turtle
turtle.speed(10)
def main(): #função principal (main)
  while True:
    vezes = int(input('Quantas vezes quer fazer?'))
    for i in range(vezes):
      figura = random.randint(0,1)
      if figura == 0:
        retangulo()
      elif figura == 1:
        circulo()
def retangulo(): #retangulo
  turtle.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
  l = random.randint(20,50)
  a = random.randint(20,50)
  turtle.penup()
  turtle.goto(random.randint(-200, 200),random.randint(-200, 200))
  turtle.pendown()
  turtle.forward(l)
  turtle.right(90)
  turtle.forward(a)
  turtle.right(90)
  turtle.forward(l)
  turtle.right(90)
  turtle.forward(a)
  turtle.penup()
def circulo(): #circulo
  r = random.randint(20,50)
  g = random.randint(0,360)
  turtle.penup()
  turtle.goto(random.randint(-200, 200),random.randint(-200, 200))
  turtle.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
  turtle.pendown()
  turtle.circle(r,g)
  turtle.penup()
  
main()