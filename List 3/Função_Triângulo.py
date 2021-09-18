import turtle
t = turtle.Turtle()

def desenhaTriangulo(_x1, _y1, _x2, _y2, _x3, _y3): #triângulo
  t.penup()
  t.goto(_x1,_y1)
  t.pendown()
  t.begin_fill()
  t.goto(_x2,_y2)
  t.goto(_x3,_y3)
  t.end_fill() 

x1, y1 = input("Valores de X1 e Y1: ").split()
x2, y2 = input("Valores de X2 e Y2: ").split()
x3, y3 = input("Valores de X3 e Y3: ").split()

if (float(x1) - float(x2))*(float(y3) - float(y2)) - (float(x3) - float(x2))*(float(y1) - float(y2)) == 0:
  print('Pontos Colineares, não forma triângulo.')
elif x1 == x2 and x2 == x3:
  print('Pontos Colineares, não forma triângulo.')
elif y1 == y2 and y2 == y3:
  print('Pontos Colineares, não forma triângulo.')
else:
  desenhaTriangulo(float(x1), float(y1), float(x2), float(y2), float(x3), float(y3))