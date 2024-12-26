class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f" {self.name} снесён, но он останется в истории")

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
            return
        for floor in range(1, new_floor + 1):
            print(floor)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def comparison_(self, other, operator):
        if isinstance(other, House):
            return operator(self.number_of_floors, other.number_of_floors)
        if isinstance(other, int):
            return operator(self.number_of_floors, other)
        return NotImplemented

    def __eq__(self, other):
        return self.comparison_(other, lambda x, y: x == y)

    def __lt__(self, other):
        return self.comparison_(other, lambda x, y: x < y)

    def __le__(self, other):
        return self.comparison_(other, lambda x, y: x <= y)

    def __gt__(self, other):
        return self.comparison_(other, lambda x, y: x > y)

    def __ge__(self, other):
        return self.comparison_(other, lambda x, y: x >= y)

    def __ne__(self, other):
        return self.comparison_(other, lambda x, y: x != y)

    def __add__(self, value):
        if isinstance(value, int) and value > 0:
            return House(self.name, self.number_of_floors + value)
        return self

    def __radd__(self, value):
        self.number_of_floors += value
        return self

    def __iadd__(self, value):
        self.number_of_floors += value
        return self

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

del h2  # Удаление объектов
del h3

print(House.houses_history)