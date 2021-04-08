x = 0
y = 0
import turtle
t = turtle.Turtle()
comprimento1 = int(input("Qual o primeiro número?"))
t.penup()
t.goto(x, y)
t.pendown()
t.color("black")
t.pensize(10)
t.forward(comprimento1)

comprimento2 = int(input("Qual o segundo número?"))
t.penup()
t.goto(x, y + 15)
t.pendown()
t.color("blue")
t.pensize(10)
t.forward(comprimento2)

comprimento3 = int(input("Qual o terceiro número?"))
t.penup()
t.goto(x, y + 30)
t.pendown()
t.color("gray")
t.pensize(10)
t.forward(comprimento3)

media = (comprimento1 + comprimento2 + comprimento3) / 3
print('média = ' + str(media))
t.penup()
t.goto(x, y + 45)
t.pendown()
t.color("red")
t.pensize(10)
t.forward(media)