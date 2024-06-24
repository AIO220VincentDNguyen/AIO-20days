from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, name, price, manufacturer, quantity):
        self.name = name
        self.price = price
        self.manufacturer = manufacturer
        self._quantity = quantity

    @abstractmethod
    def production_info(self, order_quantity):
        pass

class Phone(Product):
    def __init__(self, name, price, manufacturer, quantity, screen_size):
        super().__init__(name, price, manufacturer, quantity)
        self.screen_size = screen_size
    def production_info(self, order_quantity):
        return print(f'Name: {self.name}, Price: {self.price}, Manufacturer: {self.manufacturer}, Quantity: {order_quantity}, Screen size: {self.screen_size}')

class Laptop(Product):
    def __init__(self, name, price, manufacturer, quantity, memory_size, cpu):
        super().__init__(name, price, manufacturer, quantity)
        self.memory_size = memory_size
        self.cpu = cpu
    def production_info(self, order_quantity):
        return print(f'Name: {self.name}, Price: {self.price}, Manufacturer: {self.manufacturer}, Quantity: {order_quantity}, Memory size: {self.memory_size}, CPU: {self.cpu}')

class TV(Product):
    def __init__(self, name, price, manufacturer, quantity, resolution):
        super().__init__(name, price, manufacturer, quantity)
        self.resolution = resolution
    def production_info(self, order_quantity):
        return print(f'Name: {self.name}, Price: {self.price}, Manufacturer: {self.manufacturer}, Quantity: {order_quantity}, Resolution: {self.resolution}')

class Order:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.products = []
    def add_product(self, product, quantity):
        self.products.append((product, quantity))
    def calculate_total_price(self):
        total_price = 0
        for product, quantity in self.products:
            total_price += product.price * quantity
        return total_price
    def generate_invoice(self):
        print(f'Customer: {self.customer_name}')
        print('Products:')
        for product, quantity in self.products:
            product.production_info(quantity)
        print(f'Total price: {self.calculate_total_price()}')

# check
phone = Phone("iPhone", 1000, "Apple", 50, "6.1 inches")
laptop = Laptop("MacBook", 1500, "Apple", 30, "16GB", "Intel i7")
tv = TV("Samsung TV", 800, "Samsung", 20, "4K")

order = Order("Vincent D Nguyen")
order.add_product(phone, 1)
order.add_product(laptop, 2)
order.add_product(tv, 1)
order.generate_invoice()