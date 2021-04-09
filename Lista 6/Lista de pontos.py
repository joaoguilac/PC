import turtle
t = turtle.Turtle()

def definicao_pontos():
  p = []
  Pontos = []
  for i in range(pontos):
    p = input("Digite o " + str(i+1) + "º" + " ponto:").split()
    for j in range(len(p)):
      p[j] = int(p[j])
    if i == 0:
      inicio = p 
    desenho_poligono(p, i,inicio)
    Pontos.append(p)
  return Pontos

def desenho_poligono(v, d, comeback):
  global pontos
  t.hideturtle()
  if d == 0:
    t.penup()
  t.goto(v)
  if d == 0:
    t.pendown()
  t.begin_fill()
  t.dot(7)
  if d == pontos-1:
    t.goto(comeback)

pontos = int(input("Quantos pontos tem o polígono?")) 
poligono = (definicao_pontos())
t.end_fill()
print("Polígono ="),
for l, k in enumerate(poligono):
  print(k[0], k[1]),