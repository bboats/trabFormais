# Linguagens Formais e Autômatos : Trabalho Final

## Definição
1. Criar um programa que, dado um AFN M , definido em um arquivo texto, execute as seguintes operações:

#### • Converta M em um AFD N equivalente;
#### • Após a conversão, permita ao usuário fornecer uma lista de palavras α para reconhecimento por N;
#### • Para cada w de α, o programa deve determinar se w ∈ ACEIT A(N) ou w ∈ REJEITA(N) e apresentar o resultado;

2. Selecionar e descrever um cenário de um sistema real (linguagem) que contenha, pelo menos, 5 operações relevantes (alfabeto);
3. Definir formalmente a linguagem L que descreve o comportamento do sistema escolhido, associando símbolos as suas operações;
4. Apresentar um AFN que reconheça a linguagem L;
5. Criar uma lista de 10 palavras a serem reconhecidas pelo AFN, sendo que, destas, 5 devem ser aceitas e 5 devem ser rejeitadas;
6. Utilizar o AFN do item 4 em conjunto com as palavras do item 5 para testar o programa do item 1.



## Instruções
O formato do arquivo de entrada contendo a definição do AFN deve seguir o padrão de "exemploEntrada.txt".

As conversões de AFN para AFD devem seguir o algoritmo apresentado na prova do teorema correspondente, de forma a garantir a sua equivalência. Qualquer otimização ou alteração deve ser devidamente provada como meio de se obter um AFD equivalente.

No caso do teste de reconhecimento de palavras pelo autômato M D , as mesmas devem ser fornecidas pelo usuário (linha de comando ou arquivo de entrada) e o resultado deve ser "ACEITA" ou "REJEITA" para cada palavra w da lista.
