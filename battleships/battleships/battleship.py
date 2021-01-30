from board import Dot


class Ship:
    def __init__(self, head, length, orientation):
        self.head = head
        self.length = length
        self.orientation = orientation
        self.lives = length  # длину корабля приравниваем к его количеству жизней

    @property           # объявляем свойства корабля
    def dots(self):
        ship_dots = []  # список в котором храним точки корабля

        for i in range(self.length):  # проходимся по точкам корабля в его длине
            # определяем точки x и y по носу корабля
            cur_x = self.head.x
            cur_y = self.head.y

            if self.orientation == 0:
                cur_x += i  # если корабль лежит у нас носом по стороне 'x', шагаем по точке на + i
            elif self.orientation == 1:
                cur_y += i  # тоже самое но по стороне 'y'

            ship_dots.append(Dot(cur_x, cur_y))  # добавляем точки корабля в пустой список с помощью метода Dot

        return ship_dots

    def shooten(self, shot):
        return shot in self.dots  # проверяем выстрел в точках корабля
