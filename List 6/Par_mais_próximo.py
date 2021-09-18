valores = input("Quais os valores?")
valores = valores.split()
for i, t in enumerate(valores):
  valores[i] = int(valores[i])

#Subtração base para as condições seguintes 
subtracao = abs(valores[0] - valores[1]) 

def menor_subtracao(x): #Teste da menor diferença entre os números
  global subtracao
  for j in range(len(valores)):
    if x != j:
      if abs(valores[x] - valores[j]) < subtracao:
        subtracao = abs(valores[x] - valores[j])

def parmaisproximo(y): #Teste para saber o par mais próximo
  for l in range(len(valores)):
    teste = abs(valores[y] - valores[l])
    if y != l:
      if  teste == subtracao:
        print('Par mais próximo: '  + str(valores[y]) + ' e ' + str(valores[l]))
        return True
        break

for i, t in enumerate(valores): 
  menor_subtracao(i)

for k, u in enumerate(valores): 
  retorno = parmaisproximo(k)
  if retorno == True:
    break