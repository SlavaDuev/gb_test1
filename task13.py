class Animal:
    def __init__(self, name, birth_date):
        self._name = name  # Инкапсуляция: атрибуты скрыты
        self._birth_date = birth_date
        self._commands = []

    def add_command(self, command):
        self._commands.append(command)

    def get_commands(self):
        return self._commands

    def __str__(self):
        return f"{self._name}, дата рождения: {self._birth_date}"

# Наследуемые классы
class Pet(Animal):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)

class PackAnimal(Animal):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)

# Наследуемые классы для конкретных типов животных
class Dog(Pet):
    pass

class Cat(Pet):
    pass

class Hamster(Pet):
    pass

class Horse(PackAnimal):
    pass

class Camel(PackAnimal):
    pass

class Donkey(PackAnimal):
    pass
