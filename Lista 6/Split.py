def funcaoSplit(lista, elementoseparador):
  print("Sequências resultantes:")
  a = []
  nenhum = 0
  for j in range(len(lista)):
    a.append(lista[j])
  for d, v in enumerate(a):
    if v == elementoseparador and a[d-1] != v:
      print("")
    if v == elementoseparador:
      nenhum = nenhum + 1
    if v != elementoseparador:
      print(v),
  if nenhum == len(a):
    print("Nenhuma")



sequencia = input("Qual a sequência?").split()
for i, t in enumerate(sequencia): 
  sequencia[i] = int(sequencia[i])
separador = int(input("Qual o elemento separador?"))
funcaoSplit(sequencia, separador)