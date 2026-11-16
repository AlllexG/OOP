from abc import ABC, abstractmethod

from atributes import Price, Quantity, Weight
from products import Smartphone, Laptop, Tshirt, Jacket, Milk, Bread

# Абстрактный класс фабрики.
# Определяет общий интерфейс создания товаров.
class ProductFactory(ABC):

    @abstractmethod
    def create_product(self, name, price, quantity, weight):
        pass


# Фабрика для создания электроники.
class ElectronicsFactory(ProductFactory):

    # В зависимости от названия создаёт нужный тип товара.
    def create_product(self, name, price, quantity, weight):
        if name == "Smartphone":
            return Smartphone(Price(price), Quantity(quantity), Weight(weight))
        elif name == "Laptop":
            return Laptop(Price(price), Quantity(quantity), Weight(weight))
        else:
            raise ValueError("Неизвестный товар электорники")


# Фабрика для создания одежды.
class ClothesFactory(ProductFactory):

    def create_product(self, name, price, quantity, weight):
        if name == "Tshirt":
            return Tshirt(Price(price), Quantity(quantity), Weight(weight))
        elif name == "Jacket":
            return Jacket(Price(price), Quantity(quantity), Weight(weight))
        else:
            raise ValueError("Неизвестный товар одежды")


# Фабрика для создания продуктов питания.
class FoodFactory(ProductFactory):

    def create_product(self, name, price, quantity, weight):
        if name == "Milk":
            return Milk(Price(price), Quantity(quantity), Weight(weight))
        elif name == "Bread":
            return Bread(Price(price), Quantity(quantity), Weight(weight))
        else:
            raise ValueError("Неизвестный товар еды")
