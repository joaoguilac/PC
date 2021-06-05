# 1. Física

Um dos problemas clássicos no ensino de Física é calcular quanto tempo levaria para que dois veículos que se deslocam em direções opostas se encontrem, dadas a distância entre eles e a velocidade de cada um.

Uma editora de livros digitais deseja incluir no seu catálogo de objetos de aprendizagem um elemento interativo em que os estudantes possam visualizar o deslocamento dos veículos e o ponto de encontro. A editora pede então que você desenvolva esse elemento.

Como protótipo, você deve ler do usuário três valores numéricos. O primeiro é a distância entre os veículos e os dois seguintes são a velocidade média de cada um. Seu programa deve apresentar o tempo que levará para os veículos se encontrarem e desenhar uma figura para ilustrar de forma proporcional os trajetos e o ponto de encontro, como exemplificado na figura abaixo.

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

<img alt="pencentual" src="images/percentual.png" />

### Exemplos de entrada e saída

```
Submetidas? 60
Completas? 60
Nota = 4.0

Submetidas? 30
Completas? 30
Nota = 2.0

Submetidas? 30
Completas? 0
Nota = 1.0

Submetidas? 60
Completas? 45
Nota = 3.5
```

# 4. Tempo

A UFRN entrou em recesso no dia 17 de março. Já fazem quantas semanas de lá pra cá?

Para facilitar essa pergunta rotineira, faça um programa que calcula o tempo decorrido em número de semanas e dias a partir do número de dias total do período. Seu programa deve perguntar ao usuário quantos dias decorreram e depois apresentar esse tempo em número de semanas e dias.

### Exemplos de entrada e saída

```
Quantos dias se passaram? 16
Isto equivale a 2 semanas e 2 dias

Quantos dias se passaram? 45
Isto equivale a 6 semanas e 3 dias

Quantos dias se passaram? 89
Isto equivale a 12 semanas e 5 dias

Quantos dias se passaram? 104
Isto equivale a 14 semanas e 6 dias
```

# 5. par ou ímpar

Escreva um programa que receba um número inteiro a e verifique se a é par ou impar. Caso seja par, seu programa deve escrever "par" e desenhar um círculo preenchido vermelho. Caso seja impar, ele deve escrever "ímpar" e desenhar um círculo preenchido de verde.

Para isso, será necessário, além das operações de desenho vistas nas atividades anteriores, a operação circle(r), onde r é o tamanho do raio do círculo a ser desenhado.

### Exemplos de entrada e saída

```
Qual o número? 5
ímpar

Qual o número? 36
par

Qual o número? 0
par

Qual o número? 21
ímpar
```

# 6. Ponto

A figura H abaixo é definida pelo conjunto de pontos (x,y) que atendem os seguintes critérios: x >= 0, y >= 0 e x^2 + y^2 <= 1.

<img alt="pencentual" src="images/regiao-H.png" />

Escreva um programa para verificar se um dado ponto p, definido através de suas coordenadas (x,y), pertence ou não à figura H. Seu programa deve ler do usuário os valores das coordenadas x e y e apresentar a mensagem "pertence" caso p pertença à figura ou "não pertence" caso contrário.

Para confirmar visualmente que o ponto pertence ou não à região, desenhe a figura (em uma escala bem maior que 1 para que sua região interna seja visível) e o ponto fornecido de uma cor diferente da figura.

Para isso, além das operações de desenho anteriores, será necessário girar a direção da caneta para esquerda (ou direita) através da operação left(a) (ou right(a)), onde a é o ângulo a ser girado. Além disso, faz-se neccessário usar um parâmetro adicional à operação circle() para que ele desenhe apenas uma parte do círculo, ou seja faça um arco. A operação recebe, então, dois parâmetros, no formato circle(r, a), onde r é o raio e a é o grau do arco a ser desenhado. Por fim, depois de desenhar o ponto fornecido pelo usuário, para vê-lo melhor, você esconder a "turtle" usando a operação hideturtle().

### Exemplos de entrada e saída

```
x:  1
y:  1
não pertence

x:  0.2
y:  0.2
pertence

x:  -0.1
y:  0.3
não pertence

x:  1
y:  0
pertence
```

# 7. Tempo melhorado

Você percebeu que o programa que você fez na atividade Tempo não apresentava o tempo de forma adequada. Por exemplo, ninguém diz "Isto equivale 6 semanas e 0 dias". Se não há dias adicionais, dizemos apenas "Isto equivale a 6 semanas". Da mesma forma, não dizemos "1 dias". Quando há apenas uma unidade, usamos o singular e dizemos "1 semana" ou "1 dia".

Faça uma nova versão do seu programa de forma que o mesmo calcule o tempo e, em função do número de semanas e dias, apresente o tempo decorrido de forma adequada.

### Exemplos de entrada e saída

```
Quantos dias se passaram? 7
Isto equivale a 1 semana

Quantos dias se passaram? 15
Isto equivale a 2 semanas e 1 dia

Quantos dias se passaram? 4
Isto equivale a 4 dias

Quantos dias se passaram? 104
Isto equivale a 14 semanas e 6 dias
```
