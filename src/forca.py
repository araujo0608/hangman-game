from random import choice

class Forca:
    
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
    
    @staticmethod #função que lê o arquivo palavras.txt e retorna a lista de palavras
    def lerArquivo():
        lista_palavras = list()
        arquivo = open('src/palavras.txt', 'r')
        palavras = arquivo.readlines()

        
        for linha in palavras:
            linha = linha.strip() #removendo o \n
            lista_palavras.append(linha)
        
        arquivo.close()
        return lista_palavras
    
    @staticmethod #função que retorna uma palavra da lista
    def sortearPalavra(lista):
        return choice(lista)