# 1. Física

Um dos problemas clássicos no ensino de Física é calcular quanto tempo levaria para que dois veículos que se deslocam em direções opostas se encontrem, dadas a distância entre eles e a velocidade de cada um.

Uma editora de livros digitais deseja incluir no seu catálogo de objetos de aprendizagem um elemento interativo em que os estudantes possam visualizar o deslocamento dos veículos e o ponto de encontro. A editora pede então que você desenvolva esse elemento.

Como protótipo, você deve ler do usuário três valores numéricos. O primeiro é a distância entre os veículos e os dois seguintes são a velocidade média de cada um. Seu programa deve apresentar o tempo que levará para os veículos se encontrarem e desenhar uma figura para ilustrar de forma proporcional os trajetos e o ponto de encontro, como exemplificado na figura abaixo.

<img alt="pencentual" src="images/prob_fisica.png" />

Para calcular o tempo, utilize a equação abaixo, onde Vr é a velocidade relativa (como os veículos estão em sentidos contrários, Vr é a soma de suas velocidades), Dr é a distância relativa (distância entre os veículos) e Δt é o tempo decorrido.

Vr=Dr/Δt

### Exemplos de entrada e saída

```
Distância (km): 50
Velocidade 1 (km/h): 60
Velocidade 2 (km/h): 40
Tempo de encontro (h) = 0.5

Distância (km): 150
Velocidade 1 (km/h): 80
Velocidade 2 (km/h): 70
Tempo de encontro (h) = 1.0

Distância (km): 220
Velocidade 1 (km/h): 40
Velocidade 2 (km/h): 60
Tempo de encontro (h) = 2.2
```

# 2. Pizza

Seus professores de Pensamento Computacional gostariam de discutir os resultados das atividades apresentando proporcionalmente quantos alunos fizeram uma determinada atividade e quantos não fizeram. Para facilitar essa discussão, eles pediram para você desenvolver um programa para desenhar um gráfico de pizza, como o ilustrado abaixo, com a quantidade de alunos que fizeram e que não fizeram uma atividade.

<img alt="pencentual" src="images/prob_pizza.png" />

Escreva um programa que lê dois valores inteiros do usuário e apresenta a proporção desses valores em %. Seu programa deve também desenhar um gráfico de pizza com as proporções.

### Exemplos de entrada e saída

```
Fizeram a atividade: 21
Não fizeram: 9
70.0% fez a atividade e 30.0% não fez.

Fizeram a atividade: 27
Não fizeram: 3
90.0% fez a atividade e 10.0% não fez.

Fizeram a atividade: 26
Não fizeram: 14
65.0% fez a atividade e 35.0% não fez.
```

# 3. Alvo

Seus amigos gostam muito de jogar dardo. Sempre que se encontram, passam horas jogando. O problema é que, vez por outra, a contagem se perde e ficam discutindo quem tem mais pontos. Você tem então a ideia de automatizar o processo capturando através de sensores a posição do dardo no alvo e calculando quantos pontos um dardo fez.

Para verificar se seus sensores estão bem ajustados, faça um programa que lê dos sensores (mas aqui será do usuário) os valores das coordenadas x e y de um dardo sobre o painel de alvo. Para conferir com a realidade, seu programa deve desenhar o painel de alvo e o ponto em que o dardo se encontra, como ilustrado na figura abaixo. Seu programa deve também apresentar quantos pontos o dardo fez, considerando 10 pontos para a faixa preta, 40 pontos para a azul, 70 para a vermelha e 100 para a amarela.

<img alt="pencentual" src="images/prob_alvo.png" />

O cálculo da pontuação do dardo é realizado em função da distância do ponto ao centro do alvo, bem como a largura de cada faixa. A distância entre dois pontos (x1,y1) e (x2,y2) é calculada pela equação abaixo. Caso o centro do alvo seja a coordenada (0,0) a equação é simplificada para a raiz da soma dos quadrados das coordenadas do dardo.



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
