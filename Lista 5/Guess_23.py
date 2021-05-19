print('Bem vindo ao guess 2/3!')
print('Podem participar vários jogadores. Cada um escolhe um número real entre 0 e 100 sem que os demais saibam do seu palpite. Depois de todos escolherem seus valores, ganha quem escolheu o número mais próximo de 2/3 da média dos valores escolhidos.')
print('')
inputescolhas = input('Escolhas:')
inputescolhas = inputescolhas.split()
floatescolhas = []
for t in inputescolhas:
  floatescolhas.append(float(t))
print(floatescolhas)

soma = 0
for i, t in enumerate(floatescolhas):
  soma = soma + t
media = soma/len(floatescolhas)
guess = media*2/3


minimo = 101
for i, t in enumerate(floatescolhas):
  diferenca = abs(t - guess)
  if diferenca < minimo:
    minimo = diferenca


print('Ganhadores:'),
for i, t in enumerate(floatescolhas):
  if minimo == abs(t - guess):
    indice = i
    print(indice),

print('// Ganhou quem escolheu o número'),
for i, t in enumerate(floatescolhas):
  if minimo == abs(t - guess):
    numero = t
    print(numero)