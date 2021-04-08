import turtle
t = turtle.Turtle()
esquerda = int(input('esquerda:'))
topo = int(input('topo:'))
largura = int(input('largura:'))
altura = int(input('altura:'))
x = int(input('x:'))
y = int(input('y:'))

#Caixa
t.penup()
t.goto(esquerda,topo)
t.pendown()
t.color('navy')
t.forward(largura)
t.right(90)
t.forward(altura)
t.right(90)
t.forward(largura)
t.right(90)
t.forward(altura)
#Ponto
t.penup()
t.goto(x,y)
t.pendown()
t.color('black')
t.dot(5)
t.hideturtle()

x2 = esquerda + largura
y2 = topo - altura
if x >= esquerda and x <= x2 and y <= topo and y >= y2: 
  print('Colide!')
else:
  print('Não colide!')
  
#Testei com uma caixa -5,5,10,10 Os pontos: -1,-1;1,-1;-1,1;1,1 todos colidem, mas seu programa diz que nao!