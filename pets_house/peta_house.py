from classes import Cat, Clients, Guests

cat1 = Cat('Джесси', "Женский", "1 год")
cat2 = Cat('Сэм', "Мужской", "2 года")

clients = Clients()
guests = Guests()


def console():
    print('Добро пожаловать в задание C.10')
    print('-' * 40)
    print('Введите [1] для базы кошек')
    print('Введите [2] для клиентов')
    print('Введите [3] для гостей')
    print('Введите [4] для выхода из программы')
    choose = int(input('Введите --> [1] [2] [3] [4] <--  '))

    if choose == 1:
        print('Имя:', cat1.name, 'Пол:', cat1.sex, 'Возраст', cat1.age)
        print('Имя:', cat2.name, 'Пол:', cat2.sex, 'Возраст', cat2.age)
        input('Нажмите Enter обратно в меню ')
        console()

    elif choose == 2:
        clients_menu()

    elif choose == 3:
        guest_menu()

    elif choose == 4:
        exit('Выход из программы')


def clients_menu():
    print('-' * 40)
    print('Введите [1] для списка клиентов')
    print('Введите [2] чтобы добавить клиента')
    print('Введите [3] чтобы найти клиента')
    print('Введите [4] для выхода в обратное меню')
    choose = int(input('Введите --> [1] [2] [3] [4] <--  '))

    if choose == 1:
        print('Список клиентов:')
        print('*'*40)
        clients.list()
        input('Нажмите Enter обратно в меню ')
        clients_menu()

    elif choose == 2:
        name = input('Введите имя клиента ')
        surname = input('Введите фамилию клиента ')
        balance = input('Введите баланс клиента ')
        clients.add(name, surname, balance)
        print(f'Вы добавили - {name} {surname} в базу. Баланс = {balance}')
        print('-'*40)
        input('Нажмите Enter обратно в меню ')
        clients_menu()

    elif choose == 3:
        surname = input('Введите фамилию клиента ')
        surname = clients.find(surname)

        if len(surname) > 0:
            print('Клиент в базе есть')
        else:
            print('Клиента нет')

    elif choose == 4:
        console()


def guest_menu():

    print('-' * 40)
    print('Введите [1] для списка гостей')
    print('Введите [2] чтобы добавить гостя')
    print('Введите [3] чтобы найти гостя')
    print('Введите [4] для выхода в обратное меню')
    choose = int(input('Введите --> [1] [2] [3] [4] <--  '))

    if choose == 1:
        print('Список гостей:')
        print('*' * 40)
        guests.list()
        input('Нажмите Enter обратно в меню ')
        guest_menu()

    elif choose == 2:
        name = input('Введите имя гостя ')
        surname = input('Введите фамилию гостя ')
        city = input('Введите город проживания ')
        status = input('Статус гостя ')
        guests.add(name, surname, city, status)
        print(f'Вы добавили - {name} {surname}, г.{city}, статус "{status}"')
        print('-' * 40)
        input('Нажмите Enter обратно в меню ')
        guest_menu()

    elif choose == 3:
        pass

    elif choose == 4:
        console()


console()
