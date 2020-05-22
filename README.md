# Comportamento de rede

Este é um código simples para resolver a questão do comportamento de uma rede e como o processo de tranferência de informação deve funcionar.

Para isso devo utilizar a tecnologia Node.js

**Atividade**

1. Elabore a representação de uma rede com a configuração explicada a seguir. Faça quatro redes estrela de seis nós (1 central + 5). Escolha dois nós arbitrariamente e faça que eles sejam os nós centrais de novas estrelas de seis nós. Ligue os elementos centrais de modo que cada elemento central se ligue a outros dois elementos centrais. Baseado na topologia que você traçou, sem utilizar IP, escreva e discuta um método que permita que cada nó de sua rede possa enviar um nó ao destinatário. Considere não somente que os nós sabem certamente o nome de seus vizinhos, mas também que, a cada mensagem
recebida, o nó deve julgar se ela é para si ou para outro. Se for para outro, ele deve encaminhar a mensagem pelo caminho correto.

2. Desafio: Implemente em sua linguagem de programação de preferência um programa capaz de reproduzir o comportamento acima descrito.

Fonte das perguntas: Redes de computadores da teoria à prática com Netkit
Fonte do vídeo de estudo: https://www.youtube.com/watch?v=rAvfHZjoR5M&t=526s

Maior parte do código foi baseado neste vídeo, que também me ensinou mais um pouco sobre grafos