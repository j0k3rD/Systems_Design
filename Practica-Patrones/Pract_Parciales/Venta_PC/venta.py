class Seller():

    def __init__(self, name):
        self.__name = name
        
class Product():

    def __init__(self, name, price):
        self.__name = name
        self.__price = price
        # self.__code = code

#Para hacerlos privados y llamarlos se puede hacer de las dos formas.
    def get_name(self):
        return self.__name

    def set_name(self, name:str):
        self.__name = name

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, price:float):
        self.__price = price
    
    # @property
    # def code(self):
    #     return self.__price
    
    # @code.setter
    # def code(self, code:str):
    #     self.__code = code
        
    # def __str__(self):
    #     return f'{self.__name} {self.__price} {self.__code}'

class Sale():

    product_list = []

    def make_sale(self, product, seller):
        sale_price = 0
        self.product_list.append(product)
        self.__seller1 = Seller(seller)
        for product in self.product_list:
            sale_price = sale_price + product.price
        self.price = sale_price
        return (self.product_list , self.__seller1, self.price)

    def calculate_commission(self, price):
        if 500 >= price <= 1000:
            commision = price*10/100
            print('Su comision final sera de: ',commision)
        elif 1000 >= price <= 1500:
            commision = price*25/100
            print('Su comision final sera de: ',commision)
        elif price > 1500:
            commision = price*35/100
            print('Su comision final sera de: ',commision)  
        else:
            print('No hay comision')

if __name__=='__main__':
    sale1 = Sale()
    i9 = Product('i9 13900k', 1000)
    mother = Product('Mother Asus', 500)
    ram = Product('Ram 32gb', 200)

    sale1.make_sale(i9, 'Juan')
    sale1.make_sale(mother, 'Juan')
    sale1.make_sale(ram, 'Juan')
    sale1.calculate_commission(sale1.price)