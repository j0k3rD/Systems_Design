import hashlib
from abc import ABC, abstractmethod


class EncodingAdapter(ABC):

    @abstractmethod
    def encoding(self, file):
        pass


class MD5(EncodingAdapter):

    def __init__(self):
        pass

    def encoding(self, file):
        with open(file, 'rb') as md5_file:
            bytes = md5_file.read()
            readable_hash = hashlib.md5(bytes).hexdigest()
        print(readable_hash)


class SHA_256(EncodingAdapter):

    def __init__(self):
        pass

    def encoding(self, file):
        with open(file, 'rb') as sha256_file:
            bytes = sha256_file.read()
            readable_hash = hashlib.sha256(bytes).hexdigest()
        print(readable_hash)


class SHA_3(EncodingAdapter):

    def __init__(self):
        pass

    def encoding(self, file):
        with open(file, 'rb') as sha3_file:
            bytes = sha3_file.read()
            readable_hash = hashlib.sha3_256(bytes).hexdigest()
        print(readable_hash)

class EncoderImpl():

    def __init__(self, adaptee:EncodingAdapter):
        self.adaptee = adaptee

    def encoding(self, file):
        encoded = self.adaptee.encoding(file)
        return encoded

def main():
    origin_file = "test.txt"

    md5_encoder = EncoderImpl(MD5())
    sha256_encoder = EncoderImpl(SHA_256())
    sha3_encoder = EncoderImpl(SHA_3())
    
    option = int(input('''\nChoose the encoding option:
                        1. MD5
                        2. SHA-256
                        3. SHA3\n'''))
    if option == 1:
        print("\nYour encoding MD5 is: ")
        md5_encoder.encoding(origin_file)
    elif option == 2:    
        print("\nYour encoding SHA-256 is: ")
        sha256_encoder.encoding(origin_file)
    elif option == 3:
        print("\nYour encoding SHA-3 is: ")
        sha3_encoder.encoding(origin_file)
    else:
        print('\nInvalid Option.')
 
if __name__=='__main__':
    main()

