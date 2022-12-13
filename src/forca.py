from random import choice
from time import sleep
from termcolor import colored


class Forca:

    # Construtor dos atributos da classe
    def __init__(self, erros):
        self.erros = erros
        self.palavraAtual = ''  # progresso da palavra chutada pelo usuário
        self.situacao = ''  # Se perdeu ou ganhou
        self.palavraD2 = list()
        self.palpitesFeitos = list()

        self.FORCAIMG = [
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
        ]  # "Imagens" da Forca em ASCII art
    @staticmethod
    def lerArquivo():
        """ Função que lê o arquivo palavras.txt e retorna a lista de palavras

        """
        lista_palavras = list()
        arquivo = open('palavras.txt', 'r')
        palavras = arquivo.readlines()

        for linha in palavras:
            linha = linha.strip()  # removendo o \n
            lista_palavras.append(linha.lower())

        arquivo.close()
        return lista_palavras

    @staticmethod
    def sortearPalavra(lista):
        """
        Função que retorna uma palavra da lista
        """
        return choice(lista)

    @staticmethod
    def apresentacaoInicial():
        """
        Função de apresentação inicial do programa
        """
        print(colored(' ---- BEM VINDO AO JOGO DA FORCA ----', 'blue', attrs=['bold']))
        print(colored('Vou sortear uma palavra do arquivo "palavras.txt"', 'blue', attrs=['bold']))
        sleep(3)
        print(colored('analisando banco de palavras...', 'blue', attrs=['bold']))
        sleep(5)
        print(colored('escolhendo palavra...', 'blue', attrs=['bold']))
        sleep(3)
        print(colored('palavra escolhida! Tudo certo, vamos começar', 'blue', attrs=['bold']))
    def criarMatrizD2(self, palavra_secreta):
        """ Função que cria a matriz de cada letra da palavra secreta com pontilhado, nessa estrutura.

                  ex: pera
                  [
                  [p][_]
                  [e][_]
                  [r][_]
                  [a][_]
                  ]

                  Quando o usuario acertar a letra, ele copia a letra correspondente para o pontilhado
                  ex: ele acerta a letra "r"
                   [
                  [p][_]
                  [e][_]
                  [r][r]
                  [a][_]
                  ]

                  Seguindo essa lógica, eu basta mostrar ao usuario a coluna 1 na apresentação do jogo
              """

        dados = []

        for pos in range(0, len(palavra_secreta)):
            dados.append(palavra_secreta[pos])
            dados.append('_')
            self.palavraD2.append(dados[:])
            dados.clear()
    def atualizarMatrizD2(self, letra_acertada):

        """ Função que atualiza a matriz de pontilhados

        Argumentos
            -> parametro letra_acertada: recebe a letra que o usuario ACERTOU
        Retornos
            -> sem retornos, apenas atualiza a matriz
        """

        for linha in range(0, len(self.palavraD2)):
            if letra_acertada == self.palavraD2[linha][0]:
                self.palavraD2[linha][1] = letra_acertada
    def apresentarForca(self):
        """
        Função que apresenta o estado atual da Forca de acordo com o número de erros
        """
        print(' ====== FORCA ======')
        print(self.FORCAIMG[self.getErros()])

        for linha in range(0, len(self.palavraD2)):
            print('{:^3}'.format(self.palavraD2[linha][1]), end=' ')

        print('')
    def recebePalpite(self):
        """
        Função que recebe e retorna um palpite válido

        Retornos
            -> retorna a letra que o usuário "chutou"
        """
        while True:
            print(colored('OBS: se digitar palavra vamos considerar apenas a primeira letra dela', 'green', attrs=['bold']))
            novo_palpite = str(input('Chute uma letra: ')).strip().lower()[0]
            print('ANALISANDO RESPOSTA...')
            sleep(4)
            if novo_palpite.isalpha():
                if novo_palpite in self.palpitesFeitos:
                    print(colored('!!! VOCÊ JÁ USOU ESSA LETRA !!!', 'orange', attrs=['bold']))
                    sleep(3)
                    print(colored('LETRAS USADAS: ', 'orange', attrs=['bold']))
                    for p in self.palpitesFeitos:
                        print(f'{p}', end=' ')
                    print('')
                    sleep(3)
                else:
                    self.palpitesFeitos.append(novo_palpite)
                    break
            else:
                print(colored('!!! ENTRADA INVÁLIDA !!!', 'red', attrs=['bold']))
                print(colored('!!! DIGITE APENAS UMA LETRA !!!', 'red', attrs=['bold']))
                print('')
                sleep(3)

        return novo_palpite
    def terminouPartida(self, palavra_secreta):
        """
        Função que verifica se o jogo acabou

        Argumentos
            -> paramentro palavra_secreta: recebe a palavra secreta sorteada

        Retornos
            -> retorna True, caso o usuário ganhe ou perca
            -> retorna False, caso o usuário nem ganhe nem perca
        """

        if palavra_secreta == self.getPalavraAtual():
            self.setSituacao('ganhou')
            return True
        elif self.getErros() == 6:
            self.setSituacao('perdeu')
            return True
        else:
            return False


    # Getter e Setters
    def getErros(self):
        return self.erros
    def setErros(self, erros):
        self.erros += erros
    def getSituacao(self):
        return self.situacao
    def setSituacao(self, situacao):
        self.situacao = situacao
    def getPalavraAtual(self):
        return self.palavraAtual
    def setPalavraAtual(self):
        """ Função set que concatena a coluna de pontilhados da matriz e joga no atributo da classe

        """
        atual = ''
        for linha in range(0, len(self.palavraD2)):
            atual += self.palavraD2[linha][1]
        self.palavraAtual = atual
