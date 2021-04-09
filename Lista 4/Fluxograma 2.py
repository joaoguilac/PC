import random

def opcao_1():
  global n_jogos6
  n_jogos6 = int(input('Quantos jogos?'))
  n = 0
  while not n == n_jogos6:
    n1 = random.randint(1,60)
    n2 = random.randint(1,60)
    n3 = random.randint(1,60)
    n4 = random.randint(1,60)
    n5 = random.randint(1,60)
    n6 = random.randint(1,60)
    n = n + 1
    print('Jogo ' + str(n) + ':' )
    print(str(n1), str(n2), str(n3), str(n4), str(n5), str(n6))
def opcao_2():
  global n_jogos9
  n_jogos9 = int(input('Quantos jogos?'))
  n = 0
  while not n == n_jogos9:
    n1 = random.randint(1,60)
    n2 = random.randint(1,60)
    n3 = random.randint(1,60)
    n4 = random.randint(1,60)
    n5 = random.randint(1,60)
    n6 = random.randint(1,60)
    n7 = random.randint(1,60)
    n8 = random.randint(1,60)
    n9 = random.randint(1,60)
    n = n + 1
    print('Jogo ' + str(n) + ':' )
    print(str(n1), str(n2), str(n3), str(n4), str(n5), str(n6), str(n7), str(n8), str(n9))
def opcao_3():
  global n_jogos12
  n_jogos12 = int(input('Quantos jogos?'))
  n = 0
  while not n == n_jogos12:
    n1 = random.randint(1,60)
    n2 = random.randint(1,60)
    n3 = random.randint(1,60)
    n4 = random.randint(1,60)
    n5 = random.randint(1,60)
    n6 = random.randint(1,60)
    n7 = random.randint(1,60)
    n8 = random.randint(1,60)
    n9 = random.randint(1,60)
    n10 = random.randint(1,60)
    n11 = random.randint(1,60)
    n12 = random.randint(1,60)
    n = n + 1
    print('Jogo ' + str(n) + ':' )
    print(str(n1), str(n2), str(n3), str(n4), str(n5), str(n6), str(n7), str(n8), str(n9), str(n10), str(n11), str(n12))

n_jogos6 = 0
n_jogos9 = 0
n_jogos12 = 0
print('Bem vindo à calculadora da Mega Sena')
while True:
  print('Escolha a opção:')
  print('1 - 6 dezenas')
  print('2 - 9 dezenas')
  print('3 - 12 dezenas')
  print('4 - Calcular valor da aposta e sair')
  opcao = int(input('Opção:'))
  if opcao == 1:
    opcao_1()
  elif opcao == 2:
    opcao_2()
  elif opcao == 3:
    opcao_3()
  elif opcao == 4:
    valor_aposta = 4.5*n_jogos6 + 378*n_jogos9 + 4.158*n_jogos12
    print('Valor da sua aposta é:')
    print('R$' + str(valor_aposta))
    print('Boa sorte!')
    break