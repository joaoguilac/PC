import turtle
t = turtle.Turtle()
t.speed(10)
import math

def planocartesiano():
  t.color('blue')
  t.penup()
  t.goto(0,-180)
  t.pendown()
  t.left(90)
  t.goto(0,180)
  t.penup()
  t.goto(0,190)
  t.color('black')
  t.write('y')
  t.right(90)
  cont1 = 0
  for i in range(10):
    t.penup()
    t.goto(0,0-cont1)
    t.pendown()
    t.pensize(3)
    t.forward(-3)
    t.forward(6)
    cont1 = cont1 + 20
  t.penup()
  t.goto(-14,-183)
  t.write('-9')
  t.penup()
  t.goto(-11,-3)
  t.write('0')
  cont2 = 0
  for i in range(10):
    t.penup()
    t.goto(0,0+cont2)
    t.pendown()
    t.pensize(3)
    t.forward(-3)
    t.forward(6)
    cont2 = cont2 + 20
  t.penup()
  t.goto(-11,177)
  t.write('9')
  t.hideturtle()
    
def boxplot(menor, _quartil1, mediana, _quartil3, maior):
  t.penup()
  t.goto(20, menor*20)
  t.pendown()
  t.forward(60)
  t.penup()
  t.goto(50, menor*20)
  t.pendown()
  t.left(90)
  t.goto(50, _quartil1*20)
  t.color('royal blue')
  t.begin_fill()
  t.goto(20, _quartil1*20)
  t.goto(20, _quartil3*20)
  t.goto(80, _quartil3*20)
  t.goto(80, _quartil1*20)
  t.goto(20, _quartil1*20)
  t.end_fill()
  t.color('black')
  t.penup()
  t.goto(80, mediana*20)
  t.pendown()
  t.goto(20, mediana*20)
  t.penup()
  t.goto(50, _quartil3*20)
  t.pendown()
  t.goto(50, maior*20)
  t.goto(20, maior*20)
  t.goto(80, maior*20)
  t.hideturtle()

planocartesiano()

repeat = 0
print('Bem vindo ao BoxPlot-ish, devido a escala do desenho seus números devem estar entre -9 e 9.')
N = int(input('Digite o número de elementos no conjunto de dados')) 
for i in range(N + repeat):
  j = float(input('Valor de cada elemento do conjunto:'))
  if i == 0:
    x = j
    menor_valor = j
  if j < x:
    while j <= x:
      print('Erro! Conjunto tem que ser Ordenado')
      j = float(input('Qual o valor de cada elemento do conjunto')) 
    repeat = repeat + 1
  x = j
  if i == round(N * 1/4):
    quartil_1 = j
  if i+1 == round(N * 3/4):
    quartil_3 = j
  if N % 2 > 0:
    if i == (N-1)/2:
      med = j
  if N % 2 == 0:
    if i == (N/2)-1:
      a = j
    if i == N/2:
      b = j
      med = (a+b)/2
maior_valor = j

boxplot(menor_valor, quartil_1, med, quartil_3, maior_valor)
print('O menor valor é: ' + str(menor_valor))
print('Quartil 1 é: ' + str(quartil_1))
print('A mediana é: ' + str(med))
print('Quartil 3 é: ' + str(quartil_3)) 
print('O maior valor é: ' + str(maior_valor))