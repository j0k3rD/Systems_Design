from abc import ABC

class Product():

    def __init__(self, name, price, code):
        self.__name = name
        self.__price = price
        self.__code = code

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
    
    @property
    def price(self):
        return self.__price

    @property
    def code(self):
        return self.__code

    

class Products():
    
    def __init__(self):
        self.products = []
    
    def add_product(self, product):
        self.products.append(product)


class PaymentMethod(ABC):
    pass

class CashMethod(PaymentMethod):
    pass

class CreditMethod(PaymentMethod):
    pass

class DebitMethod(PaymentMethod):
    pass

class Ahora12Method(PaymentMethod):
    pass


class SearchProduct():
    
    def __init__(self, products):
        self.products = products
    
    def search(self, name):
        for product in self.products:
            if product.name == name:
                return product
        return None


class Discount():

    def __init__(self, product):
        self.product = product
    
    def calculate_discount(self, price, payment_method: PaymentMethod):
        if isinstance(payment_method, CashMethod):
            return price * 0.1
        elif isinstance(payment_method, CreditMethod):
            return price * 0.20
        elif isinstance(payment_method, DebitMethod):
            return price * 0
        elif isinstance(payment_method, Ahora12Method):
            return price * 0.25
        else:
            return 0
    

class ShowProductWithDiscount():

    def __init__(self, payment_method):
        self.payment_method = payment_method
    
    def show(self, product_select):
        search_product = SearchProduct(products.products)
        product = search_product.search(str(product_select))
        discount = Discount(product)

        if product is not None:
            for method in self.payment_method:
                print(f"El producto {product.name} tiene un precio de ${product.price} y un descuento de ${discount.calculate_discount(product.price, method)} con el metodo de pago {method.__class__.__name__}")
        else:
            print("El producto no existe")


if __name__ == "__main__":
    products = Products()
    products.add_product(Product("Coca Cola", 100, 1))
    products.add_product(Product("Pepsi", 90, 2))
    products.add_product(Product("Fanta", 85, 3))

    product_select = input("Ingrese el codigo del producto: ")

    payment_method = [CashMethod(), CreditMethod(), DebitMethod(), Ahora12Method()]
    show_product_with_discount = ShowProductWithDiscount(payment_method)
    show_product_with_discount.show(product_select)