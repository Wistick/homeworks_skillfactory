class BoardException(Exception):  # заводим свой собственный класс исключения, наследуемся от родителя всех исключений
    pass


class BoardWrongShipException(BoardException):  # наследуем исключение от нашего собственного
    pass


class BoardOutException(BoardException):
    def __str__(self):
        return f'You are trying to shoot out of board!'


class BoardUsedException(BoardException):
    def __str__(self):
        return f'You have already shot here!'
