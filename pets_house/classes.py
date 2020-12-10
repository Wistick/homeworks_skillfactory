class Cat:

    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def getName(self):
        return self.name

    def getSex(self):
        return self.sex

    def getAge(self):
        return self.age


class Database:

    def __init__(self):
        self.clientDB = []
        self.guestDB = []

        self.clientDB.append(("Иван", "Петров", 50))
        self.clientDB.append(("Лера", "Постоянная", 1000))


class Clients(Database):

    def list(self):
        for (name, surname, balance) in self.clientDB:
            print(f'{name} {surname} {balance}')

    def add(self, name, surname, balance):
        self.clientDB.append((name, surname, balance))

    def find(self, surname):
        prefix = []

        for (name, surname, balance) in self.clientDB:
            if surname == surname:
                prefix.append(surname)
        return prefix


class Guests(Database):

    def list(self):
        for (name, surname, city, status) in self.guestDB:
            print(f'{name} {surname} {city} {status}')

    def add(self, name, surname, city, status):
        self.guestDB.append((name, surname, city, status))

    def find(self, surname):
        pass
