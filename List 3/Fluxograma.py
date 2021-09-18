continuar = True
while continuar:
  sal = int(input('Digite seu salário'))
  op = input('Deseja calcular a renda anual (s/n)?')
  if op == "s":
    ra = sal * 13
    print('Renda anual é ' + str(ra))
    op = input('Continuar?')
    if op == "n":
      break
  else:
    op = input('Continuar?')
    if op == "n":
      break
print('Obrigado por nos consultar')