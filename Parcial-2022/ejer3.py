class Empresa():
    def __init__(self, nombre, empleados, cantidad_ventas):
        self.__nombre = nombre
        self.__cantidad_ventas = cantidad_ventas
        self.empleados = []
    
    def agregar_empleado(self, empleado):
        self.__empleados.append(empleado)

    def ver_salarios(self):
        for empleado in self.empleados:
            print("Los salarios de los empleados es: ", empleado.salario)

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def empleados(self):
        return self.__empleados

    @empleados.setter
    def empleados(self, empleados: list):
        self.__empleados = empleados

    @property
    def cantidad_ventas(self):
        self.__cantidad_ventas
    
    @cantidad_ventas.setter
    def cantidad_ventas(self,cantidad_ventas):
        self.__cantidad_ventas = cantidad_ventas

    def calcular_comision(self):
        for empleado in self.empleados:
            if self.cantidad_ventas > (self.cantidad_ventas * empleado):
                return empleado.__salario + 35000

class SalarioFijoEmpleado():
    def __init__(self, nombre, apellido, tiempo_trabajado):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__tiempo_trabajado = tiempo_trabajado
        self.__salario = 100000

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self,apellido):
        self.__apellido = apellido

    def adicional(self, tiempo_trabajo:int):
        if tiempo_trabajo < 2:
            return self.__salario
        elif 2 < tiempo_trabajo < 5:
            return self.__salario == self.__salario + (self.__salario*0.05)
        elif 5 < tiempo_trabajo < 10:
            return self.__salario == self.__salario + (self.__salario*0.1)
        elif 10 < tiempo_trabajo < 20:
            return self.__salario == self.__salario + (self.__salario*0.15)
        elif tiempo_trabajo > 20:
            return self.__salario == self.__salario + (self.__salario*0.20)


class AComisionEmpleado():
    def __init__(self, nombre, apellido):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__salario = 80000
        
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self,apellido):
        self.__apellido = apellido
    


if __name__=="__main__":

    empleado1 = SalarioFijoEmpleado("Roberto", "Martinez", '15')
    empleado2 = SalarioFijoEmpleado('Fernando', 'Cara', '5')
    empleado1.adicional(50)
    empleado2.adicional(3)

    empleado3 = AComisionEmpleado('Hugo', 'Rodriguez')
    empleado4 = AComisionEmpleado('Fernanda', 'Navarro')

    empresa1 = Empresa('Sancor', [], 3000000)
    empresa1.agregar_empleado(empleado1)
    empresa1.agregar_empleado(empleado2)
    empresa1.agregar_empleado(empleado3)
    empresa1.agregar_empleado(empleado4)



    empresa1.calcular_comision()

    empresa1.ver_salarios()




