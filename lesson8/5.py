'''
Задание №5
Продолжить работу над первым заданием.
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь.
'''
class Warehouse:
    def __init__(self, length, width, height, volume):
        self.length = length
        self.width = width
        self.height = height
        self.volume = volume

class Office_equipment:
    def __init__(self, quantity, producer):
        self.quantity = quantity
        self.producer = producer

class Printer(Office_equipment):
    def __init__(self, quantity, producer, printing_speed):
        self.printing_speed = printing_speed
        super().__init__(quantity, producer)

class Scanner(Office_equipment):
    def __init__(self, quantity, producer, scanning_speed):
        self.scanning_speed = scanning_speed
        super().__init__(quantity, producer)


class Xerox(Office_equipment):
    def __init__(self, quantity, producer, number_of_copies_per_cycle):
        self.number_of_copies_per_cycle = number_of_copies_per_cycle
        super().__init__(quantity, producer)