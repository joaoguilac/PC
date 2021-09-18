#Cálculo do tempo
D = int(input('Distância (km):'))
V1 = int(input('Velocidade 1 (km/h):'))
V2 = int(input('Velocidade 2 (km/h):'))
Vr = V1 - (-V2)
t = D / Vr
print('Tempo de encontro (h) = ' + str(t))

#Figura
S0_carro1 = 0
S1_carro1 = V1 * t
S0_carro2 = D
S1_carro2 = (V2 * t)
import turtle
t = turtle.Turtle()
t.penup()
t.goto(S0_carro1,0)
t.pendown()
t.color('blue')
t.pensize(20)
t.forward(S1_carro1)
t.penup()
t.goto(S0_carro2,0)
t.pendown()
t.color('green')
t.pensize(20)
t.backward(S1_carro2)
t.color('black')
t.dot(20)