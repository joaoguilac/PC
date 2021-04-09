import turtle
t = turtle.Turtle()
t.speed(5)
def quadrado(p):
  t.penup()
  t.goto(-200,0)
  t.pendown()
  t.color('blue')
  t.begin_fill()
  for i in range(4):
    t.forward(10*p + 15)
    t.right(90)
  t.end_fill()

print('Digite dois números inteiros n1 e n2, em que n1 < n2 e n1 >= 0.')
n1 = int(input('n1='))
n2 = int(input('n2='))

F0 = 0
F1 = 1
if n1 == 0:
  print(F0)
  quadrado(F0)
  print(F1)
  quadrado(F1)
n = F0 + F1
F0 = F1
F1 = n
if n1+2 == 2 and n2 >= 2:
  printf(n)
  quadrado(F1)

if n1 == 0:
  for n in range(n1+3,n2+1):
    n = F0 + F1
    F0 = F1
    F1 = n
    printf(n)
    quadrado(n)
elif n1 > 2:
  while n < 3:
    n = F0 + F1
    F0 = F1
    F1 = n
  for n in range(n1,n2+1): 
    n = F0 + F1
    F0 = F1
    F1 = n
    print(n)
    quadrado(n)