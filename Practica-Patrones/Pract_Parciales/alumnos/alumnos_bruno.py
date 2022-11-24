class Persona():

    def __init__(self, nombre: str, apellido: str, dni: str):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
    
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
    def apellido(self, apellido):
        self.__apellido = apellido
    
    @property
    def dni(self):
        return self.__dni
    
    @dni.setter
    def dni(self, dni):
        self.__dni = dni

    def __str__(self):
        return f"{self.nombre}, {self.apellido}, {self.dni}"


class Alumno(Persona):

    def __init__(self, matricula: str, email: str, promedio: float, nombre: str, apellido: str, dni: str):
        super().__init__(nombre, apellido, dni)
        self.__matricula = matricula
        self.__email = email
        self.__promedio = promedio

    @property
    def matricula(self):
        return self.__matricula
    
    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula
    
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email):
        self.__email = email
    
    @property
    def promedio(self):
        return self.__promedio
    
    @promedio.setter
    def promedio(self, promedio):
        self.__promedio = promedio
    
    def _str_(self) -> str:
        return super()._str() + f", Matricula: {self.matricula}, Email: {self.email}, Promedio: {self._promedio}"

    
class OrdenarAlumnos():
    
    def __init__(self):
        self.__alumnos = []

    def agregar(self, alumno: Alumno):
        if alumno not in self.__alumnos:
            self.__alumnos.append(alumno)
        else:
            print("El alumno ya existe")

    def ordenar(self):
        self.__alumnos.sort(key=lambda alumno: alumno.promedio, reverse=True)
    
    def show_by_order(self):
        for alumno in self.__alumnos:
            print(alumno)
        

def main():
    alumno1 = Alumno("123", "email", 7.5, "Juan", "Perez", "12345678")
    alumno2 = Alumno("456", "email", 8.5, "Maria", "Gomez", "87654321")
    alumno3 = Alumno("789", "email", 9.5, "Pedro", "Rodriguez", "12345678")
    alumno4 = Alumno("321", "email", 10.0, "Jose", "Lopez", "87654321")

    ordenar = OrdenarAlumnos()
    ordenar.agregar(alumno1)
    ordenar.agregar(alumno2)
    ordenar.agregar(alumno3)
    ordenar.agregar(alumno4)

    ordenar.ordenar()
    ordenar.show_by_order()


if __name__ == "__main__":
    main()