class CounterError(Exception):
    pass

class Counter:
    def __init__(self):
        self._count = 0
        self._resource_open = False

    def __enter__(self):
        if self._resource_open:
            raise CounterError("Ресурс уже открыт!")
        self._resource_open = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._resource_open:
            self._resource_open = False

    def add(self):
        if not self._resource_open:
            raise CounterError("Счётчик должен использоваться в блоке try-with-resources!")
        self._count += 1
        print(f"Счётчик увеличен, текущее значение: {self._count}")

# Пример использования:
try:
    with Counter() as counter:
        counter.add()  # Добавление нового животного
except CounterError as e:
    print(e)
