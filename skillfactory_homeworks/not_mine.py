def greetings():
    print()
    print('Игра крестики нолики расчитанная на двух игроков.\nПервым ходит крестик')
    print('*' * 20)
    print('Для того, чтобы поставить "X" или "0" - воспользуйтесь координатами на доске.')
    print('Сначала вводится координата y (столбик), затем x (строка).')
    print('*' * 20)
    print('Удачной игры!')


underscore = '_'

board = [[underscore for x in range(3)] for y in range(3)]


def display_board():
    print(' ', '0', '1', '2')
    for y, row in enumerate(board):
        print(y, ' '.join(board[y]))


def player_input():
    while True:
        coordinats = input('Введите координаты для хода: ').split()

        if len(coordinats) != 2:
            print('Вы ввели неправильные координаты.\nВведите их через пробел.')
            print()
            continue

        x, y = coordinats
        x, y = int(x), int(y)

        if x not in (0, 1, 2) and y not in (0, 1, 2):
            print('Вы ввели неправильные координаты.\nВведите их еще раз!')
            print()
            continue

        if board[x][y] != underscore:
            print('Эта клеточка уже занята!')
        else:
            return x, y


def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(board[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True
    return False


def main():
    greetings()
    counter = 0
    while True:
        display_board()

        if counter % 2 == 0:
            print("Ходит крестик!")
        else:
            print("Ходит нолик!")

        x, y = player_input()

        if counter % 2 == 0:
            board[x][y] = "X"
        else:
            board[x][y] = "0"

        if check_win():
            display_board()
            break


        counter += 1
        if counter > 8:
            print('Ничья!')
            break


main()