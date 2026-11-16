from product import Product

# Класс смартфона.
# Наследуется от Product и относится к категории электроники.
class Smartphone(Product):
    def __init__(self, price, quantity, weight):
        super().__init__(price, quantity, weight, "electronics")

    # Возвращает информацию о смартфоне.
    def get_info(self):
        return f"""---Смартфон ID: {self.id}---:
                    Цена: {self.price},
                    Кол-во: {self.quantity},
                    Вес: {self.weight}.\n"""

# Класс ноутбука.
# Наследуется от Product и относится к категории электроники.
class Laptop(Product):
    def __init__(self, price, quantity, weight):
        super().__init__(price, quantity, weight, "electronics")

    # Возвращает информацию о ноутбуке.
    def get_info(self):
        return f"""---Ноутбук ID: {self.id}---:
                    Цена: {self.price},
                    Кол-во: {self.quantity},
                    Вес: {self.weight}.\n"""

# Класс футболки.
# Наследуется от Product и относится к категории одежды.
class Tshirt(Product):
    def __init__(self, price, quantity, weight):
        super().__init__(price, quantity, weight, "clothes")

    # Возвращает информацию о футболке.
    def get_info(self):
        return f"""---Футболка ID: {self.id}---:
                    Цена: {self.price},
                    Кол-во: {self.quantity},
                    Вес: {self.weight}.\n"""

# Класс куртки.
# Наследуется от Product и относится к категории одежды.
class Jacket(Product):
    def __init__(self, price, quantity, weight):
        super().__init__(price, quantity, weight, "clothes")

    # Возвращает информацию о куртке.
    def get_info(self):
        return f"""---Куртка ID: {self.id}---:
                    Цена: {self.price},
                    Кол-во: {self.quantity},
                    Вес: {self.weight}.\n"""

# Класс молока.
# Наследуется от Product и относится к категории еды.
class Milk(Product):
    def __init__(self, price, quantity, weight):
        super().__init__(price, quantity, weight, "food")

    # Возвращает информацию о молоке.
    def get_info(self):
        return f"""---Молоко ID: {self.id}---:
                    Цена: {self.price},
                    Кол-во: {self.quantity},
                    Вес: {self.weight}.\n"""

# Класс хлеба.
# Наследуется от Product и относится к категории еды.
class Bread(Product):
    def __init__(self, price, quantity, weight):
        super().__init__(price, quantity, weight, "food")

    # Возвращает информацию о хлебе.
    def get_info(self):
        return f"""---Хлеб ID: {self.id}---:
                    Цена: {self.price},
                    Кол-во: {self.quantity},
                    Вес: {self.weight}.\n"""
