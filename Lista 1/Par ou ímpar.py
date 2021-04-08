import turtle
t = turtle.Turtle()
numero = int(input("Qual o número?"))
if numero % 2 == 0:
  print('par')
  turtle.color("red")
else:
  print('ímpar')
  turtle.color("green")

turtle.begin_fill()
turtle.circle(30)
turtle.end_fill()