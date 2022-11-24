from abc import ABC, abstractmethod

class Order:
    items = []
    quantities = []
    prices = []
    status = 'open'

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)
    
    def total_price(self):
        total = 0
        for i in range(len(self.items)):
            total += self.quantities[i] * self.prices[i]
        return total


class Authorizer(ABC):

    @abstractmethod
    def is_authorized(self) -> bool:
        return self.authorized


class SMSAuth(Authorizer):

    authorized = False

    def verify_code(self, code):
        print(f"Verifying code {code}")
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized


class NotARobot(Authorizer):
    authorized = False

    def not_a_robot(self):
        print(f"Are you a robot? Naaaa...")
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized


class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, order):
        pass


class DebitPaymentProcess(PaymentProcessor):

    def __init__(self, security_code, authorizer: Authorizer):
        self.authorizer = authorizer
        self.security_code = security_code

    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Not Authorized")
        print('Processing debit payment type')
        print(f'Verifying security code {self.security_code}')
        order.status = 'paid'


class CreditPaymentProcess(PaymentProcessor):

    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print('Processing credit payment type')
        print(f'Verifying security code {self.security_code}')
        order.status = 'paid'


class PaypalPaymentProcess(PaymentProcessor):   

    def __init__(self, email_address, authorizer: Authorizer):
        self.authoriezer = authorizer
        self.email_address = email_address
        self.verified = False

    def pay(self, order):
        if not self.authoriezer.is_authorized():
            raise Exception("Not Authorized")
        print('Processing PayPal payment type')
        print(f'Verifying email address {self.email_address}')
        order.status = 'paid'    


order = Order()
order.add_item('Shoes', 1, 100)
order.add_item('T-shirt', 2, 50)
order.add_item('Pants', 1, 80)

print(order.total_price())
authorizer = NotARobot()
processor = DebitPaymentProcess("125915", authorizer)
authorizer.not_a_robot()
processor.pay(order)