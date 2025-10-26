
class Product:

    def __init__(self, name: str, price: int, stock: int):
        if stock < 0:
            raise ValueError("Количество товара на складе не может быть отрицательным")
        self.name = name
        self.price = price 
        self.stock = stock
    
    def __hash__(self):
        return hash((self.name, self.price))
    
    def __eq__(self, other):
        if isinstance(other, Product):
            return self.name == other.name and self.price == other.price
        return False

    def update_stock(self, quantity: int) -> None:
        
        new_stock = self.stock + quantity
        if new_stock < 0:
            raise ValueError("Недопустимое количество.")
        self.stock = new_stock


class Order:

    def __init__(self, store):
        self.products = {}
        self._store = store
    
    def add_product(self, product: Product, quantity: int) -> None:
        if quantity <= 0:
            raise ValueError("Количество должно быть положительным")
        if not isinstance(product, Product):
            raise ValueError(f"Товар {product} не найден на складе")
        if product not in self._store.products:
            raise ValueError("Товар не доступен в магазине")
        if product.stock < quantity:
            raise ValueError(f"Недостаточно товара {product.name} на складе. Доступно: {product.stock}")

        self.products[product] = self.products.get(product, 0) + quantity
    
    def remove_product(self, product: Product, quantity: int = None):

        if product not in self.products:
            raise KeyError("Товар отсутствует в заказе")
        
        if quantity is None or self.products[product] <= quantity:
            del self.products[product]
        else:
            self.products[product] -= quantity

    def calculate_total(self) -> int:
        return sum(product.price * qty for product, qty in self.products.items())
    
    def confirm(self):
        if not self.products:
            raise ValueError("Нельзя подтвердить пустой заказ")
        
        for product, qty in self.products.items():
            if product.stock < qty:
                raise ValueError(f"Недостаточно товара '{product.name}' на складе при подтверждении заказа. "
                                 f"Доступно: {product.stock}, требуется: {qty}")
        for product, qty in self.products.items():
            product.stock -= qty


class Store:

    def __init__(self):
        
        self.products = []

    def add_product(self, product: Product):
        if not isinstance(product, Product):
            raise TypeError("Такой товар отсутствует на складе")
        
        for p in self.products:
            if p == product:
                p.stock += product.stock
                return
        self.products.append(product)

    def list_products(self):
        if not self.products:
            print("Магазин пуст.")
            return
        print("Доступные товары:")
        for product in self.products:
            print(f"- {product.name}: цена {product.price}, на складе: {product.stock}")
    
    def create_order(self):
        return Order(self)


# Создаем магазин
store = Store()

# Создаем товары
product1 = Product("Ноутбук", 1000, 5)
product2 = Product("Смартфон", 500, 10)

# Добавляем товары в магазин
store.add_product(product1)
store.add_product(product2)

# Список всех товаров
store.list_products()

# Создаем заказ
order = store.create_order()

# Добавляем товары в заказ
order.add_product(product1, 2)
order.add_product(product2, 3)

# подтверждение заказа
order.confirm()

# Выводим общую стоимость заказа
total = order.calculate_total()
print(f"Общая стоимость заказа: {total}")

# Проверяем остатки на складе после заказа
store.list_products()