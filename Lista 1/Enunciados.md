# 1. Comprimento

Escreva um programa que lê do usuário um valor e desenhe uma reta horizontal com o comprimento dado pelo usuário. A reta deve ser vermelha e ter uma espessura de 10 pixels.

Será necessário importar a biblioteca de desenho turtle e usar as operações pensize(), color() e forward() de uma "caneta" (chamada aqui de "turtle") criada pela biblioteca.

# 2. Média

Escreva um programa que lê do usuário três números inteiros e, em seguida, apresenta a média dos números lidos.

A cada vez que o usuário entrar com um valor, o programa deve desenhar uma linha horizontal de espessura 10 e comprimento dado pelo valor dado pelo usuário. As linhas devem estar uma acima da outra. Acima delas, desenhe uma linha vermelha com o comprimento da média calculada.

Para isso, além das operações utilizadas na atividade Comprimento, você poderá também usar penup(), pendown() e goto(x, y) para "levantar a caneta", "baixar a caneta" e ir para uma dada coordenada, respectivamente.

### Exemplos de entrada e saída

```
valor 1: 3
valor 2: 5
valor 3: 1
média = 3.0

valor 1:  3
valor 2:  8
valor 3:  1
média = 4.0

valor 1:  16
valor 2:  25
valor 3:  -14
média = 9.0

valor 1:  25
valor 2:  0
valor 3:  1
média = 8.666666666666666
```

# 3. Nota

As atividades que são passadas para o curso de Pensamento Computacional valem até 4,0 pontos na média final da disciplina. As atividades completas (corretas) entregues no prazo valem 100% de seus pontos e as incompletas ou fora do prazo valem 50%. Faça um programa para te ajudar a saber qual será sua nota correspodente às atividades em função do número de atividades completas e incompletas que você submeteu. Considere um número total de 60 atividades ao longo do curso.

O programa deve perguntar ao usuário quantas atividades foram submetidas ao todo e, destas, quantas foram completas (corretas dentro do prazo). O programa deverá, então, apresentar a nota correspodente.

O programa deve também desenhar duas linhas horizontais, uma sobre a outra, para mostrar o percentual de atividades completas sobre a total de submetidas, como ilustrado na figura abaixo.

<img alt="pencentual" src="https://github.com/ThiagoOliveiraCordeiro/ThiagoOliveiraCordeiro/blob/master/programming.svg" />
