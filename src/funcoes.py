from time import sleep

IMGFORCA = [
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

palavra_sorteada = "BRASIL"
secreta = []
for index in range(0, len(palavra_sorteada)):
    secreta.append(palavra_sorteada[index])
    
numero_erros = 0
numero_acertos = 0
letras_acertadas = []
letras_erradas = []


def imprimir_img(erros):
    print(IMGFORCA[erros])

def imprimir_pontilhados(palavra_sorteada, letras_acertadas, letras_erradas):
    print('')
    
    for index in range(0, len(palavra_sorteada)):
        print('_ '.format(palavra_sorteada[index]), end='')
    
    
def main(erros, acertos):
    letra = recebe_palpite()
    
    if letra in palavra_sorteada:
        # print('{} tem na palavra {}'.format(chute, palavra_sorteada))
        acertos += 1
        letras_acertadas.append(letra)
    else:
        #print('Errou! Não pode mais usar a letra {}'.format(chute))
        letras_erradas.append(letra)
        erros += 1
        
    
    
def recebe_palpite():
    pergunte = True
    while pergunte:
        imprimir_img(numero_erros)
        imprimir_pontilhados(palavra_sorteada, letras_acertadas, letras_erradas)
        print('')
        chute = input('Advinhe a próxima letra: ').strip()
        
        print('analisando...')
        sleep(2)
        
        if chute.isalpha() and len(chute) == 1:
            pergunte = False
        else:
            print('ERRO! DIGITE APENAS UMA LETRA!\n')
    
    return chute.upper()
