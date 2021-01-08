"""
1) Статистика по всему промежутку времени [D]
2) Подсчет общего количества трат и поступлений [D]
3) Статистика общих трат и поступлений по нескольким месяцам [D]
4) Аналогично пункту (3) только по какой-то категории [D]
5) Программа для нескольких пользователей []
6) * Шифровать данные каждого пользователя паролем [D]
"""

import datetime as dt
from collections import defaultdict
import json
import os.path


def greetings():
    print("Приветствуем вас в приложении".center(40))
    print('-' * 40)
    print("Учёт финансов".center(40))
    print('-' * 40)
    print("Режимы работы:".center(40))
    print('-' * 40)
    print("[1] Добавить зачисление")
    print("[2] Добавить трату")
    print("[3] Получить статистику")
    print("[4] Выйти из программы")
    print("[5] Создать пользователя")
    print("[6] Войти")
    print('-' * 40)
    print("Формат ввода даты: YY-MM-DD".center(40))


def ask_file(FILENAME):
    print('-' * 40)
    print('Путь к файлу по-умолчанию :'.center(40))
    print(f'{FILENAME}'.center(40))
    print('-' * 40)
    print('Нажмите Enter для работы'.center(40))
    print('с этим файлом'.center(40))
    print('Введите имя файла, если'.center(40))
    print('нужно работать с другим'.center(40))
    command = input()
    if command:
        if os.path.isfile(FILENAME):
            FILENAME = command
            print('-' * 40)
            print('Файл выбран'.center(40))
        else:
            print('Такого файла нет!'.center(40))
            print('Использую файл по-умолчанию'.center(40))

    return FILENAME


def ask_mode():
    print('-' * 40)

    return input('Введите режим работы: ')


def wrong():
    print('-' * 40)
    print('Вы ввели некорректный режим работы ')


def ask_cost(ast_str):
    number = None
    while number is None:
        num_str = input('Введите сумму: ')
        if num_str.isdigit():
            number = int(num_str)
        else:
            print('Вы ввели некорректное число!')
            continue

    return number


def ask_date(ask_str):
    date = None
    while date is None:
        date_str = input(ask_str)
        splitted = date_str.split('-')

        check = []
        for string in splitted:
            check.append(string.isdigit())

        if not(all(check)):
            print('Часть даты не число!')
            continue

        splitted[0] = '20' + splitted[0]
        year, month, day = map(int, splitted)
        date = dt.date(year, month, day)  # TODO регулярные выражения

    return date  # TODO с помощью исключения написать все проверки


def ask_income():
    print('-' * 40)
    cat = input('Введите категорию: ')
    cost = ask_cost('Введите сумму поступления: ')
    date = ask_date('Введите дату поступления: ')

    return ['+', cat, date, cost]


def ask_spend():
    print('-' * 40)
    cat = input('Введите категорию: ')
    cost = ask_cost('Введите сумму траты: ')
    date = ask_date('Введите дату траты: ')

    return ['-', cat, date, cost]


def ask_interval():
    date1 = ask_date('Введите начало интервала: ')
    date2 = ask_date('Введите конец интервала: ')

    return date1, date2


def ask_all_time():
    past_date = '1900-01-01'
    array = past_date.split('-')
    year, month, date = map(int, array)
    past_date = dt.date(year, month, date)

    now = dt.datetime.today()
    now = now.strftime('%Y-%m-%d')
    now = now.split('-')
    year, month, day = map(int, now)
    today_date = dt.date(year, month, day)

    return past_date, today_date


def stat(data, date1, date2):
    income_stat = defaultdict(list)
    spend_stat = defaultdict(list)

    for typ, cat, date, cost in data:
        if date1 <= date <= date2:
            if typ == '+':
                income_stat[cat].append(cost)
            if typ == '-':
                spend_stat[cat].append(cost)

    print('-' * 40)
    print('Статистика поступлений')
    print('-' * 40)
    for cat, cost_list in income_stat.items():
        print(f'   {cat:20} - {sum(cost_list)}')

    total = []

    for cat, count in income_stat.items():
        total.append(sum(count))
    print(f'   Общая сумма          - {sum(total)}')
    print('-' * 40)
    print('Статистика трат')
    print('-' * 40)

    total2 = []

    for cat, cost_list in spend_stat.items():
        print(f'   {cat:20} - {sum(cost_list)}')
    for cat, count in spend_stat.items():
        total2.append(sum(count))
    print(f'   Общая сумма          - {sum(total2)}')


def cat_search(data, date1, date2):
    print('[1] Поиск по категории "Поступления"')
    print('[2] Поиск по категории "Траты"')
    choose = input('Введите режим работы: ')

    income_stat = defaultdict(list)
    spend_stat = defaultdict(list)

    if choose == '1':
        search = input('Введите название категории по поиску: ')
        for typ, cat, date, cost in data:
            if date1 <= date <= date2:
                if typ == '+':
                    income_stat[cat].append(cost)

        for cat, cost in income_stat.items():
            if cat == search:
                print(f'   {cat:20} - {sum(cost)}')

    elif choose == '2':
        search = input('Введите название категории по поиску: ')

        for typ, cat, date, cost in data:
            if date1 <= date <= date2:
                if typ == '-':
                    spend_stat[cat].append(cost)

        for cat, cost in spend_stat.items():
            if cat == search:
                print(f'   {cat:20} - {sum(cost)}')


def loop(data):

    while True:
        mode = ask_mode()
        if mode == "1":
            data.append(ask_income())
        elif mode == "2":
            data.append(ask_spend())
        elif mode == "3":
            print("[1] Получить статистику по интервалу времени")
            print("[2] Получить статистику по категории")
            print("[3] Получить статистику за все время")
            choose = input('Введите режим работы: ')
            if choose == '1':
                beg, end = ask_interval()
                stat(data, beg, end)
            elif choose == '2':
                beg, end = ask_all_time()
                cat_search(data, beg, end)
            elif choose == '3':
                beg, end = ask_all_time()
                stat(data, beg, end)
        elif mode == '5':
            new_user()
        elif mode == '6':
            user_login()
        elif mode == "4":
            break
        else:
            wrong()

    print('-' * 40)
    print("Данные сохранены!".center(40))
    print('-' * 40)

    return data


def save(data, FILENAME):
    for rec in data:
        rec[2] = str(rec[2])
    with open(FILENAME, 'w') as f:
        json.dump(data, f)


def read(FILENAME):
    if os.path.isfile(FILENAME):
        with open(FILENAME) as f:
            data = json.load(f)
    else:
        data = []

    for rec in data:
        date_ints = map(int, rec[2].split('-'))
        rec[2] = dt.date(*date_ints)

    return data


def new_user():
    user_name = input('Введите свой логин: ')
    user_pw = input('Введите свой пароль: ')

    with open('accounts.json', 'r') as f:
        accounts = json.load(f)

    if user_name in accounts:
        print('Пользователь уже существует!')
    else:
        accounts[user_name] = user_pw
        accounts = json.dumps(accounts)
        print(f'Пользователь {user_name} создан!')

    with open('accounts.json', 'w') as f:
        f.write(accounts)


def user_login():
    user_name = input('Введите логин: ')
    user_pw = input('Введите пароль: ')

    with open('accounts.json', 'r') as f:
        accounts = json.load(f)

    if user_name in accounts and accounts[user_name] == user_pw:
        print(f'Вы вошли в систему, как {user_name}')
    else:
        print('Неправильно введен пароль или имя пользователя')


def main(FILENAME):
    greetings()
    FILENAME = ask_file(FILENAME)
    data = read(FILENAME)
    data = loop(data)
    save(data, FILENAME)


main('my_journal.json')

