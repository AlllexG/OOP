import copy

# Итератор для последовательного перебора товаров на складе
class WarehouseIterator:

    # Конструктор итератора
    # Получает список товаров и устанавливает начальный индекс
    def __init__(self, products):
        self.products = products
        self.index = 0

    # Метод возвращает сам объект итератора
    # Необходим для работы цикла for
    def __iter__(self):
        return self

    # Метод возвращает следующий товар из списка
    def __next__(self):
        if self.index >= len(self.products):
            raise StopIteration

        product = self.products[self.index]
        self.index += 1

        return product


# Основной класс склада
class Warehouse:
    
    # Конструктор склада
    # capacity — максимальное количество товаров на складе
    def __init__(self, capacity):
        if capacity < 0:
            raise ValueError("Вместимость не можут быть отрицательной")

        self.capacity = capacity
        self.products = []

    # Метод добавления товара на склад
    def add_product(self, product):
        if len(self.products) >= self.capacity:
            raise ValueError("Нет места на складе")
        
        # Проверяем, существует ли уже товар с таким ID
        if self.find_by_id(product.id) is not None:
            raise ValueError("Товар с таким ID уже существует")

        self.products.append(product)
    
    # Метод удаления товара по его ID
    def remove_product(self, product_id):
        for product in self.products:
            if product.id == product_id:
                self.products.remove(product)
                return True

        return False

    # Метод поиска товара по ID
    def find_by_id(self, product_id):
        for product in self.products:
            if product.id == product_id:
                return product

        return None
    
    # Метод поиска товаров по категории
    def find_by_category(self, category):
         return [product for product in self.products 
                 if product.category == category]

    # Метод перемещения товара на другой склад
    def transfer_product(self, product_id, transfer_to):
        if transfer_to is self:
            raise ValueError("Перемещение на тот же склад")

        product = self.find_by_id(product_id)

        if product is None:
            raise ValueError("Товар не найден")

        transfer_to.add_product(product)
        self.remove_product(product_id)

    # Метод создания итератора для склада
    def __iter__(self):
        # Возвращаем новый объект WarehouseIterator
        return WarehouseIterator(self.products)

    # Метод глубокого копирования объекта
    def __deepcopy__(self, memo):
        new_warehouse = Warehouse(self.capacity)
        
        # Запоминаем связь между старым и новым объектом
        memo[id(self)] = new_warehouse
        
        new_warehouse.products = copy.deepcopy(self.products, memo)

        return new_warehouse

    # Метод перемещения содержимого склада
    def move(self):
        new_warehouse = Warehouse(self.capacity)
        new_warehouse.products = self.products

        self.products = []

        return new_warehouse

    # Метод отображения всех товаров на складе
    def show_products(self):
        if not self.products:
            print("Склад пустой")
            return

        for product in self:
            print(product)


