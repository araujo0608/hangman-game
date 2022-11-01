import random
import typing
import time
#from IPython.display import clear_output


#img hangman
HANGMANIMG = [
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

def read_words() -> typing.List[str]:
    """
    Le arquivo com words que podem ser utilizadas
    como parte do jogo
    """
    pass


def generate_random_word(words: str) -> typing.List[str]:
    """
    Função que retorna uma string a partir da
    lista de words

    :param words: lista com words que podem ser sorteadas
    :return: word secreta do jogo
    """
    pass


def print_with_spaces(word: str) -> None:
    """
    Recebe uma string word ou lista e imprime essa com
    espaço entre suas letras ou strings

    :param word: word secreta do jogo
    """
    pass


def print_game(wrongs_letters: typing.List[str], corrects_letters: typing.List[str], secret_word: str,) -> None:
    """
    Feito a partir da variável global que contem as imagens
    do jogo em ASCII art, e támbem as letras chutadas de
    maneira correta e as letras erradas e a word secreta

    :param wrongs_letters: lista de letras chutadas incorretamente
    :param corrects_letters: lista de letras chutadas corretamente
    :param secret_word: word secreta do jogo
    """
    pass


def receive_guess(user_guess: typing.List[str]) -> str:
    """
    Função feita para garantir que o usuário coloque uma
    entrada válida, ou seja, que seja uma única letra
    que ele ainda não tenha chutado

    :param user_guess: lista de letras chutadas anteriormente
    :return: nova letra chutada
    """
    pass


def play_again() -> bool:
    """
    Função que pede para o usuário decidir se ele quer
    jogar novamente e retorna um booleano representando
    a resposta

    :return: True se o jogador informou que deseja jogar novamente
    """
    return input("Você quer jogar novamente? (sim ou nao)\n").upper().startswith("S")


def verify_if_won(secret_word: str, corrects_letters: typing.List[str]) -> bool:
    """
    Função que verifica se o usuário acertou todas as
    letras da word secreta

    :param secret_word: word secreta do jogo
    :param corrects_letters: lista de letras chutadas corretamente
    :return: booleano informando se o jogador ganhou o jogo
    """
    pass


main()