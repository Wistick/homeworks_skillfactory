q = [
    "stepan",
    "anna",
    "ivanova",
    "anna",
    "stepan1",
    "anna2",
    "vlad",
    "arina",
    "ivanova",
    "vlad_ivanov",
    "stepan",
    "arina",
    "stepan15",
    "ivanova",
    "arina_ivanova"
]


def console():

    print('Новая регистрация пользователя')
    print('Введите [1] для регистрации')
    print('Введите [2] чтобы посмотреть список зарегистрированных пользователей')
    print('Введите [3] чтобы выйти')
    choose = int(input('Введите [1] [2] [3] -> '))

    if choose == 1:
        registration()

    elif choose == 2:
        print(*q, sep='\n')
        input('Нажмите Enter чтобы выйти в обратное меню ')
        console()

    elif choose == 3:
        exit('Выход из программы осуществлен')


def registration():

    while True:
        register = input('Введите ваше имя, чтобы зарегистрироваться: ').strip().lower()

        if register not in q:
            q.append(register)
            print(f'Логин "{register}" зарегистрирован')
            input('Нажмите Enter чтобы выйти в обратное меню ')
            console()
        else:
            print('* Пользователь с такими именем уже существует')
            print('Хотите продолжить регистрацию? Enter (y/N)')

            choose = input().lower().strip()

            while choose != 'y' and choose != 'n':
                choose = input('Enter (y/N)\n')

            if choose == 'y':
                registration()
            elif choose == 'n':
                console()


console()
