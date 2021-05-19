def principal(): #funcao principal
  while True:
    exibeOpcoes()
    processaOpcoes()
    global opcao
    if opcao == 4:
      print('Obrigado por usar os serviços do Caixa Eletrônico')
      break
def Saldo(): #funcao saldo
  global saldo
  print(str('O seu saldo atual é de: ') + str(saldo))
def deposito(): #funcao deposito
  global saldo
  valor_deposito = float( input('Qual o valor que você quer depositar?') )
  if valor_deposito > 0:
    saldo =  saldo + valor_deposito
    print(str('O seu saldo agora é de: ') + str(saldo) )
  else:
    print('Valor inválido')
def saque(): #funcao saque
  global saldo
  valor_sacado = float(input('Qual valor você deseja sacar?'))
  if valor_sacado <= saldo:
    saldo =  saldo - valor_sacado
    print('Saque autorizado.' + ' Agora o seu saldo atual é de: ' + str(saldo) )
  else:
    print('Saldo insuficiente.')
def exibeOpcoes(): #funcao exibeOpcoes
  global opcao
  print('Qual operacao voce deseja realizar?')
  print('1 - SAQUE')
  print('2 - DEPOSITO')
  print('3 - SALDO')
  print('4 - SAIR')
  global opcao
  opcao = float(input('Escolha:'))
def processaOpcoes(): #funcao processaOpcoes
  global condicao
  global opcao
  if opcao == 1:
    saque()
  elif opcao == 2:
    deposito()
  elif opcao == 3:
    Saldo()
  elif opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4:
    print('Opção inválida, tente novamente!')
opcao = ''
saldo = 1000
principal()