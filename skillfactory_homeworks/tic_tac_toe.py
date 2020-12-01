import random

"""Документация"""


def instructions():
    print('ТУТ БУДЕТ ОПИСАНИЕ')


underscore = '_'

board = [[underscore for x in range(3)] for y in range(3)]


def display_board(board):
    print(' ', '0', '1', '2')
    for y, row in enumerate(board):
        print(y, ' '.join(board[y]))


def get_player_char():
    player_char = input("Выберите кем будете играть 'X' или '0': ").upper().strip(' ')
    while player_char not in ('X', '0'):
        print('Неверный ввод. Повторите.')
        player_char = input("Выберите кем будете играть 'X' или '0': ").upper().strip(' ')

    return player_char


def get_opponent_char(char):
    return '0' if char == 'X' else 'X'


def get_computer_input(board):
    x, y = random.randint(0, 2), random.randint(0, 2)
    while board[x][y] != underscore:
        x, y = random.randint(0, 2), random.randint(0, 2)
    return x, y


def get_player_input(board):
    while True:
        coordinats = input('Введите координаты для хода: ').split()

        if len(coordinats) != 2:
            print('Неверный ввод. Повторите.')
            print('Вводите координаты через пробел')
            continue

        x, y = coordinats
        x, y = int(x), int(y)

        if x not in (0, 1, 2) or y not in (0, 1, 2):
            print('Неверный ввод. Повторите.')
            continue

        if board[x][y] != underscore:
            print('Эта клеточка уже занята!')
        else:
            return x, y


def check_win(char, board):
    opponent_char = get_opponent_char(char)
    for y in range(3):
        if opponent_char not in board[y] and underscore not in board[y]:
            return True

    for x in range(3):
        column = board[0][x], board[1][x], board[2][x]
        if opponent_char not in column and underscore not in column:
            return True

    diagonal = board[0][0], board[1][1], board[2][2]
    if opponent_char not in diagonal and underscore not in diagonal:
        return True

    diagonal = board[0][2], board[1][1], board[2][0]
    if opponent_char not in diagonal and underscore not in diagonal:
        return True

    return False


def check_game_tie():
    pass


def choose_turn():
    pass


def main():
    instructions()
    player_char = get_player_char()
    computer_char = get_opponent_char(player_char)
    count = 0
    while True:
        display_board(board)
        x, y = get_player_input(board)
        board[x][y] = player_char
        if check_win(player_char, board):
            display_board(board)
            print('Вы победили!')
            break

        x, y = get_computer_input(board)
        board[x][y] = computer_char
        if check_win(computer_char, board):
            display_board(board)
            print('Компьютер победил!')
            break


main()
