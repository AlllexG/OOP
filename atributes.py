# Класс Price отвечает за хранение цены товара.
# Проверяет, чтобы цена не была отрицательной.
class Price:
    def __init__(self, value):
        if value < 0:
            raise ValueError("Цена не может быть отрицательной")
        self.value = int(value)

    def getValue(self):
        return self.value

    def setValue(self, new_value):
        if new_value < 0:
            raise ValueError("Цена не может быть отрицательной")
        self.value = int(new_value)

    def __str__(self):
        return str(self.value)

# Класс Quantity отвечает за хранение количества товара.
# Проверяет, чтобы цена не была отрицательной.
class Quantity:
    def __init__(self, value):
        if value < 0:
            raise ValueError("Количество не может быть отрицателным")
        self.value = int(value)

    def getValue(self):
        return self.value

    def setValue(self, new_value):
        if new_value < 0:
            raise ValueError("Количество не может быть отрицательной")
        self.value = int(new_value)

    # Изменяет количество товара на указанное значение.
    # delta может быть положительным или отрицательным.
    def change(self, delta):
        new_value = self.value + delta

        if new_value < 0:
            raise ValueError("Количество не может быть отрицательным")

        self.value = new_value

    def __str__(self):
        return str(self.value)

# Класс Weight отвечает за хранение веса товара.
# Проверяет, чтобы цена не была отрицательной.
class Weight:
    def __init__(self, value):
        if value < 0:
            raise ValueError("Вес не может быть отрицательным")
        self.value = float(value)

    def getValue(self):
        return self.value

    def setValue(self, new_value):
        if new_value < 0:
            raise ValueError("Вес не может быть отрицательной")
        self.value = float(new_value)

    def __str__(self):
        return str(self.value)



