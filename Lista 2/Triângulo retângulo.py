import math
import turtle
t = turtle.Turtle()
lado1 = int(input('lado 1:'))
lado2 = int(input('lado 2:'))
lado3 = int(input('lado 3:'))

#Hipotenusa
if lado1 > lado2 and lado1 > lado3:
  h = lado1
elif lado2 > lado1 and lado2 > lado3:
  h = lado2
else:
  h = lado3
#Catetos  
if h == lado1:
  ca = 0
else:
  ca = lado1
if h == lado2:
  cb = 0
else:
  cb = lado2
if h == lado3:
  cc = 0
else:
  cc = lado3
#Pitágoras
if h**2 == ca**2 + cb**2 + cc**2:
  print('Forma um triângulo retângulo')
  if ca > cb and ca > cc:
    cateto_o = ca
  elif cb > ca and cb > cc:
    cateto_o = cb
  elif cc > ca and cc > cb:
    cateto_o = cc
  if ca != 0 and ca != cateto_o:
    cateto_a = ca
  elif cb != 0 and cb != cateto_o:
    cateto_a = cb
  elif cc != 0 and cc != cateto_o:
    cateto_a = cc
  alpha = math.asin(cateto_o/h)
  t.right(90-math.degrees(alpha))
  t.forward(h)
  t.right(90+math.degrees(alpha))
  t.forward(cateto_o)
  t.right(90)
  t.forward(cateto_a)
else:
  print('Não forma um triângulo retângulo')