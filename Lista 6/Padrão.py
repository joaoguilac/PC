def funcaoEntrada():  
  lista1 = input("Qual a 1ª sequência?")
  lista1 = sequenciaInteira(lista1)
  lista2 = input("Qual a 2ª sequência?")
  lista2 = sequenciaInteira(lista2)
  a = False
  for i, t in enumerate(lista2):
    for j, v in enumerate(lista1):
      if j == len(lista1)-1 and lista1[j] == lista2[i+j]:
        print("Há um casamento de padrão no índice " + str(i))
        a = True
        break
      if len(lista2) - i+j >= len(lista1):
        if lista1[j] != lista2[i+j]:
          break
        else:
          continue
      else:
        print("Não há casamento de padrão")
        a = True
        break
    if a == True:
        break

def sequenciaInteira(x):
  x = x.split()
  for i, t in enumerate(x):
    x[i] = int(x[i])
  return x

funcaoEntrada()