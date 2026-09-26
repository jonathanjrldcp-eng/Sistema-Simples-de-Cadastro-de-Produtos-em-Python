# Sistema Simples de Cadastro de Produtos em Python

Este pequeno projeto em Python simula um sistema básico de registro de produtos via terminal. Ele demonstra como capturar dados do usuário e armazená-los de forma organizada utilizando as estruturas de dados fundamentais da linguagem.

## Conceitos Abordados no Código

* **Dicionários (`dict`):** Estrutura de chave-valor usada para agrupar as características de cada item individualmente (`nome`, `preco`, `quantidade`).
* **Listas (`list`):** Estrutura usada para armazenar os múltiplos dicionários criados, funcionando como um pequeno "banco de dados" na memória do programa.
* **Laços de Repetição (`for`):** Aplicados em dois momentos: primeiro para repetir a rotina de cadastro 3 vezes, e depois para iterar sobre a lista e exibir os resultados cadastrados.
* **Conversão de Tipos (Casting):** Transformação das entradas de texto em números reais (`float` para preços) e inteiros (`int` para quantidades).
* **Strings Formatadas (f-strings):** Usadas para imprimir o relatório final de forma limpa, injetando as variáveis diretamente no texto.
* **Manipulação de Terminal:** Uso da biblioteca `os` e da função `input()` para pausar o sistema e limpar a tela a cada novo registro, melhorando a experiência do usuário.

## Como Funciona a Execução

1. O script solicita que o usuário insira o nome, o preço e a quantidade de um produto.
2. Os dados são salvos em um dicionário, que é imediatamente adicionado à lista principal.
3. O sistema pausa pedindo para pressionar "Enter" e, em seguida, limpa o terminal.
4. O ciclo se repete para um total de 3 produtos.
5. Por fim, o programa percorre a lista e exibe um relatório com todos os produtos cadastrados.

## Como Executar

1. Certifique-se de ter o Python (versão 3.x) instalado em sua máquina.
2. Salve o script em um arquivo, por exemplo, `cadastro_produtos.py`.
3. Abra o terminal (ou prompt de comando), navegue até o diretório do arquivo e digite:

   ```bash
   python cadastro_produtos.py
   ```
4. Siga as instruções na tela preenchendo os dados solicitados.

*Este exercício é uma ótima base para quem quer entender como construir sistemas de inventário ou carrinhos de compras em Python!*
