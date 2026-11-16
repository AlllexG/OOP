from abc import ABC, abstractmethod
from atributes import Price, Quantity, Weight

# Абстрактный базовый класс для всех товаров.
class Product(ABC):

    # Статический счетчик для создания уникального ID
    next_id = 1

    def __init__(self, price, quantity, weight, category):
        self.id = Product.next_id
        Product.next_id += 1

        self.price = price
        self.quantity = quantity
        self.weight = weight
        self.category = category

    # Перемещение товара на другой склад.
    def transfer(self, transfer_from, transfer_to):
        transfer_from.transfer_product(self.id, transfer_to)
    
    # Изменение количества товара.
    def change_quantity(self, delta):
        self.quantity.change(delta)
    
    # Изменение цены товара.
    def set_price(self, new_price):
        self.price = new_price
    
    # Абстрактный метод получения информации о товаре.
    @abstractmethod
    def get_info(self):
        pass

    # Возвращает информацию о товаре при его выводе.
    def __str__(self):
        return self.get_info()
