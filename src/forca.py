from random import choice
from time import sleep

class Forca:
    
    #Construtor dos atributos da classe
    
    def __init__(self, erros):
      self.erros = erros
      self.palavraAtual = ''
      self.situacao = ''
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
    
    @staticmethod #função de apresentação inicial do programa
    def apresentacaoInicial():
      print(' ---- BEM VINDO AO JOGO DA FORCA ----')
      print(' Vou sortear uma palavra do arquivo "palavras.txt" e você tem 7 tentativas para acertar a palavra!')
      sleep(3)
      print('analisando banco de palavras...')
      sleep(5)
      print('escolhendo palavra...')
      sleep(3)
      print('palavra escolhida! Tudo certo, vamos começar')
    

    def criarMatrizD2(self, palavra_secreta):
      '''
      função que cria a matriz de cada letra da palavra secreta com pontilhado, nessa estrutura.
      ex: pera
      [
      [p][_]
      [e][_]
      [r][_]
      [a][_]
      ]
      
      quando o usuario acertar a letra, copio a letra correspondente para o pontilhado
      ex: ele acerta a letra "r"
       [
      [p][_]
      [e][_]
      [r][r]
      [a][_]
      ]
      
      Seguindo essa lógica, eu só mostro a coluna 1 na apresentação do jogo
      '''
      dados = []
      
      for pos in range(0, len(palavra_secreta)):
        dados.append(palavra_secreta[pos])
        dados.append('_')
        self.palavraD2.append(dados[:])
        dados.clear()
    
    def atualizarMatrizD2(self, letra_acertada): # função que atualiza os pontilhados
      for linha in range(0, len(self.palavraD2)):
        if letra_acertada == self.palavraD2[linha][0]:
          self.palavraD2[linha][1] = letra_acertada
    
    def apresentarForca(self): #Função que apresenta o estado atual da Forca
      print(' ====== FORCA ======')
      print(self.FORCAIMG[self.getErros()])
      
      for linha in range(0, len(self.palavraD2)):
        print('{:^3}'.format(self.palavraD2[linha][1]), end=' ')
      
      print('')
    
    def recebePalpite(self): #Função que recebe e retorna um palpite válido
      while True:
        print('OBS: se digitar palavra vamos considerar apenas a primeira letra dela')
        novo_palpite = str(input('Chute uma letra: ')).strip().lower()[0]
        print('ANALISANDO RESPOSTA...')
        sleep(4)
        if novo_palpite.isalpha():
          if novo_palpite in self.palpitesFeitos:
            print('!!! VOCÊ JÁ USOU ESSA LETRA !!!')
            sleep(3)
            print('LETRAS USADAS: ')
            for p in self.palpitesFeitos:
              print('{}'.format(p),end=' ')
            print('')
            sleep(3)
          else:
            self.palpitesFeitos.append(novo_palpite)
            break
        else:
          print('!!! ENTRADA INVÁLIDA !!!')
          print('!!! DIGITE APENAS UMA LETRA !!!')
          print('')
          sleep(3)
      
      return novo_palpite
      
    def terminouPartida(self, palavra_secreta): #Função que verifica se o jogo acabou
      if palavra_secreta == self.getPalavraAtual():
        self.getSituacao('ganhou')
        return True
      elif self.getErros() == 7:
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
    
    
    def setPalavraAtual(self, letra):
      letra = str(letra)
      self.palavraAtual = letra.join(self.palavraAtual)
    