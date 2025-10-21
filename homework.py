

class Product:

    def __init__(self, name: str, price: int, stock: int):
        self.name = name
        self.price = price 
        self.stock = stock


class Store:

    def __init__(self, products: list[Product]):
        
        self.products = products

    def add_product(prd: Product):





prd1 = [p1, p2]

s1 = Store(prd1)
s2 = Store()


s1.add_product(...)
s2.add_product()
