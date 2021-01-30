from board import Dot

from random import randint


class Player:
    def __init__(self, board, enemy):
        self.board = board  # доска игрока
        self.enemy = enemy  # доска противника

    def ask(self):  # метод ask будет наследоваться другими классами и изменятся, поэтому мы можем его пропустить
        raise NotImplementedError

    def move(self):
        while True:
            try:
                target = self.ask()  # объявляем переменную таргет для инпута выстрела
                repeat = self.enemy.shot(target)  # возращаем выстрел координат по доске противника
                return repeat
            except BaseException as e:
                print(e)


class AI(Player):   # наследуем методы из класса Player
    def ask(self):  # меняем метод ask из класса родителя
        d = Dot(randint(0, 5), randint(0, 5))
        print(f'AI shot at {d.x + 1, d.y + 1}')
        return d


class User(Player):  # наследуем методы из класса Player
    def ask(self):   # меняем метод ask из класса родителя
        while True:
            cords = input('Where do you want to shoot? ').split()
            if len(cords) != 2:
                print('Wrong coordinates!')
                continue

            x, y = cords
            if not(x.isdigit()) or not(y.isdigit()):
                print('Wrong input! Should be only numbers!')
                continue

            x, y = int(x), int(y)
            return Dot(x - 1, y - 1)
