from board import *
from battleship import Ship
from player import *


class Game:
    def __init__(self, size=6):
        self.size = size
        pl = self.choose_place()
        co = self.random_board()

        co.hidden = True

        self.ai = AI(co, pl)
        self.user = User(pl, co)

    def random_board(self):
        board = None
        while board is None:
            board = self.random_place()
        return board

    def random_place(self):
        lens = [3, 2, 2, 1, 1, 1, 1]
        board = Board(size=self.size)
        attempts = 0
        for length in lens:
            while True:
                attempts += 1
                if attempts > 2000:
                    return None
                # создаем корабль - с помощью метода randint и нашего класса Dot
                # рандомно выбираем точки расположения корабля
                # length - выбирает длину корабля из списка lens
                # последний параметр рандомно выбирает положение корабля по координатам 'x' и 'y' между 0 и 1
                ship = Ship(Dot(randint(0, self.size), randint(0, self.size)), length, randint(0, 1))
                try:
                    board.add_ship(ship)
                    break
                except BoardWrongShipException:
                    pass

        board.begin()
        return board

    def choose_place(self):
        # у меня по какой то причине слетала длина корабля через обыкновенную проверку
        # сделал через отлов исключений
        lens = [3, 2, 2, 1, 1, 1, 1]
        board = Board(size=self.size)
        print(colour('Place your 6 battleships!', 'red'))
        print(colour('First has 3 lives\nSecond and third have 2 lives\nLast four ships have 1 live!', 'red'))
        print(colour(board, 'blue'))
        for length in lens:
            for _ in range(1, len(lens)+1):
                try:
                    ask_user = input('Input coordinates where you want to place your battleship ').split()
                    x, y = ask_user
                    x, y = int(x), int(y)
                except ValueError:
                    print('Wrong coordinates! Should be numbers!')
                    continue

                try:
                    j = int(input('Now choose orientation between 0 and 1 '))
                except ValueError:
                    print('Should be numbers! Sorry, try again!')
                    continue

                ship = Ship(Dot(x-1, y-1), length, j)
                try:
                    board.add_ship(ship)
                    print(colour(board, 'blue'))
                    break
                except BoardWrongShipException:
                    print('Error! You must place your battleship on board and at free place!')

        board.begin()
        return board
