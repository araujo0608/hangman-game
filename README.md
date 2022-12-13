# **JOGO DA FORCA**

Um simples jogo da forca escrito em python3 e terminal colorido

## SE QUISER FAZER POR CONTA PRÓPRIA. ESSAS SÃO AS REGRAS GERAIS

   1. Carregue o arquivo palavras.txt para obter a lista de palavras possíveis
   2. Sorteie uma palavra aleatória da lista acima
   3. Imprima o estado da forca atual com os _ _ _ embaixo da forca com as letras a serem chutadas
   4. Peça para o usuário chutar uma letra
   5. Se a letra estiver correta substitua os _ onde ela aparece
   6. Se estiver errada, imprima embaixo da forca as letras erradas e atualize o boneco
   7. Caso o usuário perca, informe o número de chutes corretos e errados e a palavra correta
   8. Caso o usuário ganhe, informe uma mensagem de sucesso
   9. Ao final pergunte se o usuário quer jogar novamente
   10. Lembre-se que a mesma letra não pode ser chutada novamente, e que não se pode colocar caracteres especiais ou com acento


## REQUISITOS

---

* `python3`
* módulo `termcolor` para colorir terminal
  * `pip3 install termcolor --upgrade` 
* Conhecimento de básico de `POO` (Programação Orientada a Objeto)

<BR>

## COMO EXECUTAR

---

1. Clone o repositório
2. Adicione as palavras que deseja usar no arquivo `palavras.txt` sem acento, sem espaços, sem caracteres especiais e apenas um por linha

![palavras](/fotos/palavras.png)

## Recomendação de boneco em ASCII Art

~~~python
FORCAIMG = [
    """

      +---+
      |   |
          |
          |
          |
          |
    =========""",
    """

      +---+
      |   |
      O   |
          |
          |
          |
    =========""",
    """

      +---+
      |   |
      O   |
      |   |
          |
          |
    =========""",
    """

      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========""",
    """

      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========""",
    """

      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========""",
    """

      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========""",
]


~~