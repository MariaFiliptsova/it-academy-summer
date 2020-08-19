"""Создайте  модель из жизни. Это может быть бронирование комнаты в отеле,
покупка билета в транспортной компании, или простая РПГ.
Создайте несколько объектов классов, которые описывают ситуацию
Объекты должны содержать как атрибуты так и методы класса для симуляции
различных действий. Программа должна инстанцировать объекты
и эмулировать какую-либо ситуацию - вызывать методы,
взаимодействие объектов и т.д.
"""


class Room:
    total_rooms = 250
    total_booked = 0
    available = 250
    doubles_booked = 0
    twins_booked = 0
    suites_booked = 0
    under_repair = 0

    def __init__(self, bed, view, amount, category):
        self.bed = bed
        self.view = view
        self.amount = amount
        self.category = category

    def room_type(self):
        print(f'There are {self.amount} {self.category} rooms left with '
              f'{self.bed} and {self.view} view.')

    def under_construction(self):
        Room.under_repair += 1
        Room.available -= 1
        print(f'{self.category} is under repair')
        if self.category == 'double':
            self.amount -= 1
            print(f'There are only {self.amount} {self.category} rooms left')
        elif self.category == 'twin':
            self.amount -= 1
            print(f'There are only {self.amount} {self.category} rooms left')
        elif self.category == 'suite':
            self.amount -= 1
            print(f'There are only {self.amount} {self.category} rooms left')


twin_lake = Room('2 single beds', 'lake', 100, 'twin')
twin_garden = Room('2 single beds', 'garden', 50, 'twin')
double_lake = Room('1 double bed', 'lake', 50, 'double')
double_garden = Room('1 double bed', 'garden', 35, 'double')
suite = Room('1 king size bed', 'lake', 15, 'suite')

twin_lake.room_type()
twin_lake.under_construction()
twin_lake.room_type()

suite.room_type()
suite.under_construction()
suite.room_type()


class Client:

    def __init__(self, name, surname, guestnumber):
        self.name = name
        self.surname = surname
        self.guestnumber = guestnumber

    def book_double(self):
        Room.total_booked += 1
        Room.available -= 1
        print(f'{self.name} {self.surname} just booked a double room for '
              f'{self.guestnumber} guests')

    def book_twin(self):
        Room.total_booked += 1
        Room.available -= 1
        print(f'{self.name} {self.surname} just booked a twin room for '
              f'{self.guestnumber} guests')

    def book_suite(self):
        Room.total_booked += 1
        Room.available -= 1
        print(f'{self.name} {self.surname} just booked a suite room for '
              f'{self.guestnumber} guests')


client1 = Client('Alex', 'Petrov', 2)
client2 = Client('Ivan', 'Ivanov', 1)
client3 = Client('Vanya', 'Pupkin', 5)

client1.book_twin()
client2.book_double()
client3.book_suite()

print(f'The total number of rooms booked is {Room.total_booked}')
print(f'The total number of rooms under repair is {Room.under_repair}')
print(f'The total number of rooms available at the moment is {Room.available}')
