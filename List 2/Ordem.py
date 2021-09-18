import turtle
t = turtle.Turtle()
v1 = int(input('Valor 1:'))
v2 = int(input('Valor 2:'))
v3 = int(input('Valor 3:'))
if v1 > v2 and v1 > v3:
  maior_valor = v1
elif v1 < v2 and v1 < v3:
  menor_valor = v1
else:
  meio = v1

if v2 > v1 and v2 > v3:
  maior_valor = v2
elif v2 < v1 and v2 < v3:
  menor_valor = v2
else:
  meio = v2

if v3 > v1 and v3 > v1:
  maior_valor = v3
elif v3 < v1 and v3 < v2:
  menor_valor = v3
else:
  meio = v3

print('Em ordem: ' + str(menor_valor) + ' ' + str(meio) + ' ' + str(maior_valor))

#Linhas
t.pensize(10)
t.forward(menor_valor)
t.pensize(10)
t.penup()
t.goto(0,10)
t.pendown()
t.forward(meio)
t.pensize(10)
t.penup()
t.goto(0,20)
t.pendown()
t.forward(maior_valor)