"""Obtener una unica instancia del objeto DameLaMismaHora"""
import datetime, time

class DameLaMismaHora():
    def __init__(self):
        self.hr =  datetime.datetime.now()
    
obj1 = DameLaMismaHora()
print(obj1)
print(obj1.hr)
time.sleep(5)

obj2 = DameLaMismaHora()
print(obj2)
print(obj2.hr)

if obj1 == obj2:
    print("Son iguales perri")
else:
    print("na q ver")
