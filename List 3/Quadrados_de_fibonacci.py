import turtle
t = turtle.Turtle()
t.speed(5)
def quadrado(p):
  t.color('blue')
  t.begin_fill()
  for i in range(4):
    t.forward(10*p + 15)
    t.left(90)
  t.end_fill()

print('Digite dois números inteiros n1 e n2, em que n1 < n2 e n1 >= 0.')
n1 = int(input('n1='))
n2 = int(input('n2='))

F0 = 0
F1 = 1
if n1 == 0:
  print(F0)
  t.penup()
  t.goto(-200,0)
  t.pendown()
  quadrado(F0)
  print(F1)
  posicao1 = -200 + (10*F0 + 15 + 10)
  t.penup()
  t.goto(posicao1,0)
  t.pendown()
  quadrado(F1)

posicao = -200 + (10*F1 + 15 + 10 + 10*F0 + 15 + 10)
if n1 > 1:
  termo = 1
  while termo <= n2 + 1 - n1:
    Fn = F0 + F1
    print(Fn)
    t.penup()
    t.goto(posicao,0)
    t.pendown()
    quadrado(Fn)
    F0 = F1
    F1 = Fn
    posicao = posicao + 10*Fn + 15 + 10
    termo = 1 + termo
elif n1 == 1:
  print(F1)
  posicao1 = -200 + (10*F0 + 15 + 10)
  t.penup()
  t.goto(posicao1,0)
  t.pendown()
  quadrado(F1)
  termo = 2
  while termo <= n2 + 1 - n1:
    Fn = F0 + F1
    print(Fn)
    t.penup()
    t.goto(posicao,0)
    t.pendown()
    quadrado(Fn)
    F0 = F1
    F1 = Fn
    posicao = posicao + 10*Fn + 15 + 10
    termo = 1 + termo
else:
  termo = 3
  while termo <= n2 + 1 - n1:
    Fn = F0 + F1
    print(Fn)
    t.penup()
    t.goto(posicao,0)
    t.pendown()
    quadrado(Fn)
    F0 = F1
    F1 = Fn
    posicao = posicao + 10*Fn + 15 + 10
    termo = 1 + termo