from forca import Forca
from time import sleep


jogar = True

while jogar:
    while True:
        obj_forca = Forca(0)
        palavras = obj_forca.lerArquivo() #lendo arquivo das palavras
        palavra_secreta = obj_forca.sortearPalavra(palavras) #sorteando a palavra secreta

        obj_forca.apresentacaoInicial() #apresentando inicio do jogo

        obj_forca.criarMatrizD2(palavra_secreta) #criando relação palavra secreta com pontilhados

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
            
            print(obj_forca.getPalavraAtual())
            acabou = obj_forca.terminouPartida(palavra_secreta)
        
        situacao = obj_forca.getSituacao()
        if situacao == 'ganhou':
            print('--' * 20)
            print('Parabéns, você venceu! A palavra correta é {}'.format(palavra_secreta))
            print('Você chutou essas letras {}'.format(obj_forca.palpitesFeitos))
            print('--' * 20)
        else:
            print('--' * 20)
            print('Ops! Você perdeu! A palavra correta era {}'.format(palavra_secreta))
            print('Você chutou essas letras {}'.format(obj_forca.palpitesFeitos))
            print('Mais sorte na próxima vez!')
            print('--' * 20)
        
    jogar_novamente = str(input('\nDeseja jogar novamente? [S/N]: ')).strip().upper()[0]
    jogar = False if jogar_novamente == 'N' else True

# Função de vencer não pegou, após chutar todas as letras corretamentea