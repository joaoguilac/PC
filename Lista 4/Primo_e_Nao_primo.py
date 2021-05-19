print("Forneça dois números inteiros n1 e n2 (n2 > n1).")
n1 = int(input('n1:' ))
n2 = int(input('n2:' ))

def teste_primo(numero):
  for j in range(1,n2+2):
    divisao = numero % j 
    if divisao == 0 and j != 1 and j != numero:
      print(str(i) + ' Não primo')
      break
    elif divisao == 0 and j == 1:
      continue
    elif divisao == 0 and j == numero:
      continue
    elif j > numero:
      print(str(i) + ' Primo')
      break

for i in range(n1,n2+1):
  teste_primo(i)