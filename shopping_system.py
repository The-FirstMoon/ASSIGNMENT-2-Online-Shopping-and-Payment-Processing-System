
from abc import ABC, abstractmethod


# the grandpa class
class Product(ABC):
    def __init__(self, name, price):
        if price < 0:
            raise ValueError("Price cannot be negative.")

        self.name = name
        self.price = price

    @abstractmethod
    def get_total_price(self):
        pass


# the son product class
class PhysicalProduct(Product):
    def __init__(self, name, price, shipping_cost):
        super().__init__(name, price)

        if shipping_cost < 0:
            raise ValueError("Shipping cost cannot be negative.")

        self.shipping_cost = shipping_cost

    def get_total_price(self):
        return self.price + self.shipping_cost


# the online class
class DigitalProduct(Product):
    def get_total_price(self):
        return self.price


# the order will have more than one product
class Order:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def calculate_total(self):
        return sum(
            product.get_total_price()
            for product in self.products
        )

    def display_order(self):
        print("\nOrder details:")

        for product in self.products:
            print(
                f"{product.name}: "
                f"${product.get_total_price():.2f}"
            )

        print(f"Order total: ${self.calculate_total():.2f}")


# grandpa class for payment
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


# card class
class CardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Processing card payment of ${amount:.2f}")
        print("Card payment successful!")


# cash payment class anaother one
class CashPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Collecting cash payment of ${amount:.2f}")
        print("Cash payment successful!")


# checkout class use both order and payment classes
class Checkout:
    def __init__(self, order, payment_method):
        self.order = order
        self.payment_method = payment_method

    def process(self):
        if not self.order.products:
            raise ValueError("Cannot checkout an empty order.")

        amount = self.order.calculate_total()

        self.order.display_order()
        print("\nCheckout started...")
        self.payment_method.pay(amount)
        print("Checkout completed!")


# example of the assignment working
if __name__ == "__main__":
    keyboard = PhysicalProduct("Keyboard", 50.00, 5.00)
    book = PhysicalProduct("Python Book", 20.00, 3.00)
    ebook = DigitalProduct("Python E-book", 10.00)
    course = DigitalProduct("Python Course", 30.00)

    # First order: multiple products, card payment
    order1 = Order()
    order1.add_product(keyboard)
    order1.add_product(ebook)

    checkout1 = Checkout(order1, CardPayment())
    checkout1.process()

    print("\n" + "=" * 35)

    # Second order: multiple products, cash payment
    order2 = Order()
    order2.add_product(book)
    order2.add_product(course)

    checkout2 = Checkout(order2, CashPayment())
    checkout2.process()
