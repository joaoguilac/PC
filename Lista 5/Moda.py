lista = []
N = int(input('Quantos elementos o conjunto possui?')) 
for i in range(N):
  valor = int(input("Digite o " + str(i+1) + "o valor: "))
  lista.append(valor)

def teste_frequencia(n_, lista_):
  cont = 0
  for i, n in enumerate(lista_):
    if n_ == n:
      cont = cont + 1
  return cont
def teste_elementomoda(n_):
  for i, t in enumerate(lista_moda):
    if n_ == t:
      return "já existe"

frequencia = 1
for i, n in enumerate(lista):
  vezes = teste_frequencia(n, lista)
  if vezes > frequencia:
    frequencia = vezes

lista_moda = []
for i, n in enumerate(lista):
  vezes = teste_frequencia(n, lista)
  if vezes == frequencia:
    resposta = teste_elementomoda(n)
    if resposta == "já existe":
      continue
    else:
      lista_moda.append(n)
print('A moda do conjunto é:'),
for i, t in enumerate(lista_moda):
  print(t),