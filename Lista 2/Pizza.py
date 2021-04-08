#Cálculo
S = int(input('Fizeram a atividade'))
N = int(input('Não fizeram'))
alunos = S + N
porcS = S / alunos * 100
porcN = N / alunos * 100
print(str(porcS) + '% fez a atividade e ' + str(porcN) + '% não fez.')

#Pizza
import turtle
t = turtle.Turtle()
n = 3.6 * porcN
t.begin_fill()
t.color('blue')
t.circle(60)
t.end_fill()
t.begin_fill()
t.color("green")
t.circle(60, n)
t.left(90)
t.forward(60)
t.end_fill()
t.hideturtle()

def maisdametadedovalordaprova():
  