import datetime, time

class DameLaMismaHrSingleton():
    __uniq_instance = None

    def __init__(self):
        if DameLaMismaHrSingleton.__uniq_instance is None:
            DameLaMismaHrSingleton.__uniq_instance = self
            self.hr =  datetime.datetime.now()

    @staticmethod
    def get_instance():
        if DameLaMismaHrSingleton.__uniq_instance is None:
            return DameLaMismaHrSingleton()
        else:
            return DameLaMismaHrSingleton.__uniq_instance
    
    def get_hr(self):
        return self.hr

if __name__=='__main__':
    obj1 = DameLaMismaHrSingleton().get_instance()
    print(obj1)
    print(obj1.get_hr())
    time.sleep(5)

    obj2 = DameLaMismaHrSingleton().get_instance()
    print(obj2)
    print(obj2.get_hr())

    if obj1 == obj2:
        print("Son iguales perri")
    else:
        print("na q ver")


