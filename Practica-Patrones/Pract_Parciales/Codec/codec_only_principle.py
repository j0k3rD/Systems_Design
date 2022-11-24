import hashlib
from abc import ABC, abstractmethod

class File():

    def __init__(self, name):
        self.__name = name
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name

    def read(self):
        with open(self.name, 'rb') as file:
            bytes = file.read()
        return bytes

class EncodyingProcess(ABC):
    
    def __init__(self, file):
        self.file = file
    
    @abstractmethod
    def encoding(self):
        pass

class MD5(EncodyingProcess):

    def __init__(self):
        pass

    def encoding(self, file):
        readable_hash = hashlib.md5(file.read()).hexdigest()
        print(readable_hash)


class SHA_256(EncodyingProcess):

    def __init__(self):
        pass

    def encoding(self, file):
        readable_hash = hashlib.sha256(file.read()).hexdigest()
        print(readable_hash)


class SHA_3(EncodyingProcess):

    def __init__(self):
        pass

    def encoding(self, file):
        readable_hash = hashlib.sha3_256(file.read()).hexdigest()
        print(readable_hash)


class ChooseEncrypt():

    def encrypt_strategy(self, file, encrypter):
        options = {
            'md5': lambda: MD5().encoding(file),
            'sha256': lambda: SHA_256().encoding(file),
            'sha3': lambda: SHA_3().encoding(file),
        }
        if encrypter in options:
            options[encrypter]()
        else:
            print("No existe el algoritmo de encriptacion.")
    
    
if __name__ == "__main__":
    origin_file = File('asd/Pract_Parciales/Codec/codec_only_principle.py')
    encrypter = input("Ingrese el tipo de encriptacion: ")
    choose_encrypt = ChooseEncrypt()
    choose_encrypt.encrypt_strategy(origin_file, encrypter)