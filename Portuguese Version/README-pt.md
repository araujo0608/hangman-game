# Jogo da Forca

Um simples jogo da forca escrito em python3

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

## Código de estrutura para iniciar o código:

~~~python
import random
import typing
import time
from IPython.display import clear_output


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


def main():
    """
    Função Principal do programa
    """
    pass


def le_palavras() -> typing.List[str]:
    """
    Le arquivo com palavras que podem ser utilizadas
    como parte do jogo
    """
    pass


def gera_palavra_aleatoria(palavras: str) -> typing.List[str]:
    """
    Função que retorna uma string a partir da
    lista de palavras

    :param palavras: lista com palavras que podem ser sorteadas
    :return: palavra secreta do jogo
    """
    pass


def imprime_com_espacos(palavra: str) -> None:
    """
    Recebe uma string palavra ou lista e imprime essa com
    espaço entre suas letras ou strings

    :param palavra: palavra secreta do jogo
    """
    pass


def imprime_jogo(
    letras_erradas: typing.List[str],
    letras_acertadas: typing.List[str],
    palavra_secreta: str,
) -> None:
    """
    Feito a partir da variável global que contem as imagens
    do jogo em ASCII art, e támbem as letras chutadas de
    maneira correta e as letras erradas e a palavra secreta

    :param letras_erradas: lista de letras chutadas incorretamente
    :param letras_acertadas: lista de letras chutadas corretamente
    :param palavra_secreta: palavra secreta do jogo
    """
    pass


def recebe_palpite(palpites_feitos: typing.List[str]) -> str:
    """
    Função feita para garantir que o usuário coloque uma
    entrada válida, ou seja, que seja uma única letra
    que ele ainda não tenha chutado

    :param palpites_feitos: lista de letras chutadas anteriormente
    :return: nova letra chutada
    """
    pass


def jogar_novamente() -> bool:
    """
    Função que pede para o usuário decidir se ele quer
    jogar novamente e retorna um booleano representando
    a resposta

    :return: True se o jogador informou que deseja jogar novamente
    """
    return input("Você quer jogar novamente? (sim ou nao)\n").upper().startswith("S")


def verifica_se_ganhou(
    palavra_secreta: str, letras_acertadas: typing.List[str]
) -> bool:
    """
    Função que verifica se o usuário acertou todas as
    letras da palavra secreta

    :param palavra_secreta: palavra secreta do jogo
    :param letras_acertadas: lista de letras chutadas corretamente
    :return: booleano informando se o jogador ganhou o jogo
    """
    pass


main()
~~~