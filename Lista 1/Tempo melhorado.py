dias = int(input('Quantos dias se passaram?'))
semanas = dias // 7
dias2 = dias % 7
if semanas == 0:
  if dias2 != 1:
    print('Isto equivale a ' + str(dias2) + ' dias')
  else:
    print('Isto equivale a ' + str(dias2) + ' dia')
elif semanas == 1:
  if dias2 == 0:
    print('Isto equivale a ' + str(semanas) + ' semana')
  elif dias2 == 1:
    print('Isto equivale a ' + str(semanas) + ' semana e ' + str(dias2) + ' dia')
  elif dias2 > 1:
    print('Isto equivale a ' + str(semanas) + ' semana e ' + str(dias2) + ' dias')
elif semanas > 1:
  if dias2 == 0:
    print('Isto equivale a ' + str(semanas) + ' semanas')
  elif dias2 == 1:
    print('Isto equivale a ' + str(semanas) + ' semanas e ' + str(dias2) + ' dia')
  elif dias2 > 1:
    print('Isto equivale a ' + str(semanas) + ' semanas e ' + str(dias2) + ' dias')