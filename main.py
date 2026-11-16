import copy

from warehouse import Warehouse
from factories import ElectronicsFactory, ClothesFactory, FoodFactory

#Сценарий 1. Создание склада и работа с товарами
print("===СЦЕНАРИЙ 1===")

warehouse1 = Warehouse(5)

# Електроника
electronics_factory = ElectronicsFactory()

iphone_x = electronics_factory.create_product("Smartphone", 500, 10, 0.5)
lenovo_yoga_7 = electronics_factory.create_product("Laptop", 1200, 5, 2.25)

warehouse1.add_product(iphone_x)
warehouse1.add_product(lenovo_yoga_7)

# Одежда
clothes_factory = ClothesFactory()

blue_tshirt = clothes_factory.create_product("Tshirt", 20, 100, 0.25)

warehouse1.add_product(blue_tshirt)

# Еда
food_factory = FoodFactory()

bread_w_seeds = food_factory.create_product("Bread", 1.5, 150, 0.356)
chocolate_milk = food_factory.create_product("Milk", 2, 80, 1.5)

warehouse1.add_product(bread_w_seeds)
warehouse1.add_product(chocolate_milk)

warehouse1.show_products()

#Изменение кол-ва и цены
bread_w_seeds.change_quantity(-25)
iphone_x.set_price(550)

print("\nПосле изменения товаров:")
print(iphone_x)
print(bread_w_seeds)

#Удаление товара
warehouse1.remove_product(3)
print("\nПосле удаления товара:")
warehouse1.show_products()

#Итерация
print("\nПеребор товаров с поиском по категории 'элктроники'")
for product in warehouse1.find_by_category("electronics"):
    print(product)

#Сценарий 2. Копирование склада
print("===СЦЕНАРИЙ 2===")

warehouse2 = copy.deepcopy(warehouse1)

print("\nИсходный склад:")
warehouse1.show_products()

print("\nКопия склада:")
warehouse2.show_products()

#Изменение товара в копии

iphone_x_copy = warehouse2.find_by_id(1)
iphone_x_copy.change_quantity(-3)

print("\nПосле изменения копии:")

print("\nИсходный товар:")
print(warehouse1.find_by_id(1))

print("\nТовар в копии:")
print(warehouse2.find_by_id(1))

#Сценарий 3. Перемещение между складами
print("===СЦЕНАРИЙ 3===")

warehouse3 = Warehouse(3)

iphone_x.transfer(warehouse1, warehouse3)

print("\nПервый склад:")
warehouse1.show_products()

print("\nВторой склад:")
warehouse3.show_products()

warehouse4 = warehouse3.move()
print("\nСклад после перемещения:")
warehouse3.show_products()

print("\nНовый склад:")
warehouse4.show_products()
