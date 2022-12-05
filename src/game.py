from forca import Forca
from time import sleep

while True:
    
    obj_forca = Forca(0)

    palavras = obj_forca.lerArquivo() #lendo arquivo das palavras
    palavra_secreta = obj_forca.sortearPalavra(palavras) #sorteando a palavra secreta

    obj_forca.apresentacaoInicial()

    obj_forca.criarMatrizD2(palavra_secreta)

    acabou = False

    while acabou == False:
        obj_forca.apresentarForca()
        palpite = obj_forca.recebePalpite()
        if palpite in palavra_secreta:
            print('ACERTOU! A PALAVRA SECRETA TEM A LETRA {}'.format(palpite.upper()))
            sleep(3)
            obj_forca.atualizarMatrizD2(palpite)
            obj_forca.setPalavraAtual(palpite)
        else:
            print('ERROU! A PALAVRA SECRETA NÃO TEM ESSA LETRA')
            obj_forca.setErros(1)
            sleep(3)
        
        acabou = obj_forca.terminouPartida(palavra_secreta)
    
    # Estastísticas finais da partida
    # Deseja jogar de novo? Se não, dá um break
