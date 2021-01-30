from exceptions import *

from termcolor import colored as colour


class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y  # сравниваем точки друг с другом.

    def __repr__(self):
        return f'{self.x, self.y}'  # возвращаем точки в строковом представлении, чтобы прочитать их в списке


class Board:
    def __init__(self, size=6, hidden=False):
        self.size = size
        self.hidden = hidden
        # печатаем доску с помощью list comprehension
        self.board = [
            [' ' for _ in range(size)] for _ in range(size)
        ]

        self.count = 0   # заводим счетчек для подсчета уничтоженный кораблей на доске
        self.ships = []  # пустой список кораблей на доске
        self.busy = []   # пустой список занятых точке на доске

    def __str__(self):
        res = ''
        res += '    1 | 2 | 3 | 4 | 5 | 6 |'
        for y, row in enumerate(self.board):
            res += f'\n{y + 1} | ' + ' | '.join(row) + ' | '

        if self.hidden:                   # в зависимости от параметра hidden - True/False
            res = res.replace('■', ' ')   # выполняется условие, замена всех кораблей на пробелы

        return res

    def out(self, d):  # проверяем точки координат x и y на доске если они на ней лежат.
        return not ((0 <= d.x < self.size) and (0 <= d.y < self.size))

    def add_ship(self, ship):
        for d in ship.dots:                    # проходимся по точкам корабля в методе dots
            if self.out(d) or d in self.busy:  # если точка за доской или в использованных точках
                raise BoardWrongShipException()  # вызываем исключение
        for d in ship.dots:              # снова проходимся по точкам корабля в методе dots
            self.board[d.x][d.y] = '■'   # если прошлое условие не выполнено - добавляем на коордианты символ корабля
            self.busy.append(d)          # помещаем эту координату в список с занятыми точками

        self.ships.append(ship)  # добавляем корабль в список кораблей на доске
        self.contour(ship)       # добавляем контур вокруг корабля

    def contour(self, ship, verb=False):
        near = [
            (-1, -1), (-1, 0), (-1, 1),  # список near хранит все сдвиги на соседнии клекти
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]

        for d in ship.dots:       # проходимся по точкам кораблей
            for dx, dy in near:   # распаковываем все возможные координаты контура
                cur = Dot(d.x + dx, d.y + dy)  # добавляем с помощью метода Dot к кординате d координаты контура
                if not(self.out(cur)) and cur not in self.busy:  # проверяем если точки не за доской и не заняты
                    if verb:  # в зависимости от параметра hidden - True/False
                        self.board[cur.x][cur.y] = '•'  # помечаем контур символом
                    self.busy.append(cur)  # добавляем координату контура / сдвига в список занятых точек на доске

    def shot(self, d):
        if self.out(d):
            raise BoardOutException()   # вызываем исключение если точка выстрела за доской
        if d in self.busy:
            raise BoardUsedException()  # вызываем исключение если по точке уже стреляли / контур

        self.busy.append(d)  # если исключения не было, добавляем точку выстрела в список занятых точек

        for ship in self.ships:  # проходимся по корабляем в списке кораблей
            if d in ship.dots:   # проходимся по точкам в кораблей
                ship.lives -= 1  # если попадание - отнимаем 1 жизнь
                self.board[d.x][d.y] = 'X'
                if ship.lives == 0:       # если жизней осталось ноль
                    self.count += 1       # прибавляем 1 уничтоженный корабль
                    self.contour(ship, verb=True)  # обводим контур корабля и параметром True показываем его на доске
                    print(colour('You have destroyed a battleship!', 'red', attrs=['bold']))
                    return False  # ход переходит к другому игроку
                else:
                    print(colour('Hit!', 'red'))
                    return True   # продолжаем ходить

        self.board[d.x][d.y] = '•'  # если усовия не выполнены, помечаем координаты символом - мимо!
        print(colour('Miss!', 'red'))
        return False

    def begin(self):
        self.busy = []  # перед стартом игры обнуляем список.
