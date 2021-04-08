submetidas = int(input('Submetidas?'))
completas = int(input('Completas?'))

maximo_atividades = 60
porcentagem1 = submetidas / maximo_atividades
s = porcentagem1 * 4
porcentagem2 = completas / submetidas
c = (1 - porcentagem2) * 0.5 * s
c2 = s - c
print('Nota = ' + str(c2))

x = 0
y = 0
import turtle
t = turtle.Turtle()

#Nota máxima possível
t.penup()
t.goto(x, y)
t.pendown()
t.color("black")
t.pensize(10)
t.forward(60)

#Porcentagem das submetidas
t.penup()
t.goto(x, y)
t.pendown()
t.color("orange")
t.pensize(10)
t.forward(submetidas)

#Porcentagem das completas
t.penup()
t.goto(x, y)
t.pendown()
t.color("green")
t.pensize(10)
t.forward(completas)