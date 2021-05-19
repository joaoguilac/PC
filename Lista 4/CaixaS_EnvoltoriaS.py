import turtle
import random
t = turtle.Turtle()
t.speed(10)

def desenhar_caixa(xc,yc,lc,ac): #Caixa
  t.penup()
  t.goto(xc,yc)
  t.pendown()
  t.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
  t.forward(lc)
  t.right(90) 
  t.forward(ac)
  t.right(90)
  t.forward(lc)
  t.right(90)
  t.forward(ac)
  t.right(90)
def testaColisao(xc1, yc1, lc1, ac1, xc2, yc2, lc2, ac2): #Teste de Colisão
  posicao1 = xc1 + lc1
  posicao2 = yc1 - ac1
  ponto1 = xc2 + lc2
  ponto2 = yc2 - ac2
  if xc2 >= xc1 and xc2 <= posicao1 and yc2 <= yc1 and yc2 >= posicao2: 
    print('Colide!')
  elif ponto1 >= xc1 and ponto1 <= posicao1 and yc2 <= yc1 and yc2 >= posicao2: 
    print('Colide!')
  elif ponto1 >= xc1 and ponto1 <= posicao1 and ponto2 <= yc1 and ponto2 >= posicao2: 
    print('Colide!')
  elif xc2 >= xc1 and xc2 <= posicao1 and ponto2 <= yc1 and ponto2 >= posicao2:
    print('Colide!')
  elif yc2 >= yc1 and xc2 <= xc1 and ponto2 <= posicao2 and ponto1 >= xc1: 
    print('Colide!')
  elif yc2 >= yc1 and xc2 >= xc1 and ponto2 <= posicao2 and xc2 <= posicao1: 
    print('Colide!')
  elif xc2 <= xc1 and yc2 >= yc1 and ponto2 >= posicao2 and ponto2 <= yc1:
    print('Colide!')
  elif xc2 <= xc1 and yc2 <= yc1 and ponto2 <= posicao2 and yc2 >= posicao2:
    print('Colide!')
  elif xc2 <= xc1 and yc2 <= yc1 and ponto1 >= posicao1 and ponto2 >= posicao2:
    print('Colide!')
  else: 
    print('Não colide!')
   
 
x1, y1 = input("Digite as coordenadas da primeira caixa:").split()
l1, a1 = input("Digite a largura e altura da primeira caixa:").split()
x2, y2 = input("Digite as coordenadas da segunda caixa:").split()
l2, a2 = input("Digite a largura e altura da segunda caixa:").split()

desenhar_caixa(float(x1), float(y1), float(l1), float(a1)) 
desenhar_caixa(float(x2), float(y2), float(l2), float(a2))
t.hideturtle()
testaColisao(float(x1), float(y1), float(l1), float(a1), float(x2), float(y2), float(l2), float(a2))