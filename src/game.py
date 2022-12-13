from forca import Forca
from time import sleep
from termcolor import colored

jogar = True


while jogar:
    print('\n \n')
    while True:
        obj_forca = Forca(0)
        palavras = obj_forca.lerArquivo()  # lendo arquivo das palavras
        palavra_secreta = obj_forca.sortearPalavra(palavras)  # sorteando a palavra secreta
        obj_forca.apresentacaoInicial()  # apresentando inicio do jogo
        obj_forca.criarMatrizD2(palavra_secreta)  # criando relação palavra secreta com pontilhados

        acabou = False

        while acabou == False:
            obj_forca.apresentarForca()  # Mostrando desenho da forca
            palpite = obj_forca.recebePalpite()  # Recebendo palpite do usuário
            if palpite in palavra_secreta:
                let = colored(f' {palpite.upper()}', 'green', attrs=['bold'])
                print('ACERTOU! A PALAVRA SECRETA TEM A LETRA ' + str(let))
                sleep(3)
                obj_forca.atualizarMatrizD2(palpite)
                obj_forca.setPalavraAtual()
            else:
                msg = colored('ERROU! A PALAVRA SECRETA NÃO TEM ESSA LETRA', 'red', attrs=['bold'])
                print(msg)
                obj_forca.setErros(1)
                sleep(3)

            acabou = obj_forca.terminouPartida(palavra_secreta) # Verificando se o jogo acabou

        situacao = obj_forca.getSituacao() # Verificando se o usuário perdeu ou venceu

        if situacao == 'ganhou':
            print('--' * 20)
            print(colored(f'Parabéns, você venceu! A palavra correta é {str(palavra_secreta.title())}', 'green', attrs=['bold']))
            print(colored(f'Você chutou essas letras {obj_forca.palpitesFeitos}', 'green', attrs=['bold']))
            print('--' * 20)
            sleep(3)
            break
        else:
            print('--' * 20)
            print(colored(f'Ops! Você perdeu! A palavra correta era {str(palavra_secreta.title())}', 'red', attrs=['bold']))
            print(colored(f'Você chutou essas letras {obj_forca.palpitesFeitos}', 'red', attrs=['bold']))
            print(colored('Mais sorte na próxima vez!', 'blue', attrs=['bold']))
            print('--' * 20)
            sleep(2)
            break
    msg = colored('jogar novamente? [S/N]: ', 'yellow', attrs=['bold'])
    jogar_novamente = str(input(msg)).strip()[0].upper()
    jogar = False if jogar_novamente == 'N' else True
