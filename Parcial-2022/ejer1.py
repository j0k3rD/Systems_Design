from abc import ABC, abstractmethod

from numpy import number

class User():
    def __init__(self, name, lastname, dni):
        self.__name = name
        self.__lastname = lastname
        self.__dni = dni
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def lastname(self):
        return self.__lastname

    @lastname.setter
    def lastname(self, lastname):
        self.__lastname = lastname

    @property
    def dni(self):
        return self.__dni

    @lastname.setter
    def lastname(self, dni):
        self.__dni = dni
    

class AccountClass(ABC):
    def __init__(self, type):
        pass

    def deposit():
        pass

    def withdraw():
        pass


class Sueldo_Account():
    def type():
        pass

    def deposit(balance, amount):
        commision = 0.05
        balance = amount


class Normal_Account():
    def type():
        pass


class BanckAccount():
    def __init__(self, number_account:str, balance:float, alias:str, user: User, account_class: AccountClass):
        self.number_account = number
        self.balance = balance
        self.alias = alias
        self.user = user
        self.account_class = account_class