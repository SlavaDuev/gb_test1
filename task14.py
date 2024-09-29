class AnimalRegistry:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def classify_animal(self, name, birth_date, animal_type):
        if animal_type.lower() == 'dog':
            return Dog(name, birth_date)
        elif animal_type.lower() == 'cat':
            return Cat(name, birth_date)
        elif animal_type.lower() == 'hamster':
            return Hamster(name, birth_date)
        elif animal_type.lower() == 'horse':
            return Horse(name, birth_date)
        elif animal_type.lower() == 'camel':
            return Camel(name, birth_date)
        elif animal_type.lower() == 'donkey':
            return Donkey(name, birth_date)
        else:
            print("Неизвестный тип животного.")
            return None

    def list_commands(self, animal):
        print(f"Команды для {animal}: {animal.get_commands()}")

    def train_animal(self, animal, new_command):
        animal.add_command(new_command)
        print(f"{animal} обучен новой команде: {new_command}")

    def display_menu(self):
        while True:
            print("\n1. Завести новое животное\n2. Показать команды животного\n3. Обучить новое команде\n4. Выход")
            choice = input("Выберите действие: ")

            if choice == '1':
                name = input("Введите имя животного: ")
                birth_date = input("Введите дату рождения (YYYY-MM-DD): ")
                animal_type = input("Введите тип животного (dog, cat, hamster, horse, camel, donkey): ")
                new_animal = self.classify_animal(name, birth_date, animal_type)
                if new_animal:
                    self.add_animal(new_animal)
                    print(f"{new_animal} добавлен в реестр.")
            elif choice == '2':
                name = input("Введите имя животного для отображения команд: ")
                animal = self.find_animal_by_name(name)
                if animal:
                    self.list_commands(animal)
                else:
                    print("Животное не найдено.")
            elif choice == '3':
                name = input("Введите имя животного для обучения: ")
                animal = self.find_animal_by_name(name)
                if animal:
                    new_command = input("Введите новую команду: ")
                    self.train_animal(animal, new_command)
                else:
                    print("Животное не найдено.")
            elif choice == '4':
                break
            else:
                print("Неверный выбор. Попробуйте снова.")

    def find_animal_by_name(self, name):
        for animal in self.animals:
            if animal._name == name:
                return animal
        return None

# Пример использования
registry = AnimalRegistry()
registry.display_menu()
