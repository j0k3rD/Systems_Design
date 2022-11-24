class Persona():

    def __init__(self, nombre, apellido, dni):
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


class Alumno(Persona):

    def __init__(self, nombre, apellido, dni, matricula, email, promedio_nota: float):
        super().__init__(nombre, apellido, dni)
        self.__matricula = matricula
        self.__email = email
        self.__promedio_nota = promedio_nota

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
    def promedio_nota(self):
        return self.__promedio_nota
    
    @promedio_nota.setter
    def promedio_nota(self, promedio_nota):
        self.__promedio_nota = promedio_nota


class Alumnos():

    def __init__(self):
        self.alumnos = []
    
    def agregar_alumno(self, alumno):
        self.alumnos.append(alumno)


class OrdenarAlumnosPorPromedio(Alumnos):

    def __init__(self):
        super().__init__()
    
    def ordenar_alumnos(self):
        self.alumnos.sort(key=lambda alumno: alumno.promedio_nota, reverse=True)
        return self.alumnos
    

class MostrarListaOrdenadaDeAlumnos(OrdenarAlumnosPorPromedio):

    def __init__(self):
        super().__init__()
    
    def mostrar_lista_ordenada(self):
        for alumno in self.ordenar_alumnos():
            print(alumno.nombre, alumno.apellido, alumno.promedio_nota)


if __name__ == "__main__":
    alumno1 = Alumno("Bruno", "Gonzalez", "42567871", "12125","asd@gmail.com", "8.8")
    alumno2 = Alumno("Fernando", "Perez", "43567987", "65633","asd1@gmail.com", "7")
    alumno3 = Alumno("Lucrecia", "Romero", "42567846", "19566","asd3@gmail.com", "9")
    alumno4 = Alumno("Damian", "Gonzalez", "42567872", "85673","asd4@gmail.com", "6.5")

    mostrar_lista_ordenada = MostrarListaOrdenadaDeAlumnos()
    mostrar_lista_ordenada.agregar_alumno(alumno1)
    mostrar_lista_ordenada.agregar_alumno(alumno2)
    mostrar_lista_ordenada.agregar_alumno(alumno3)
    mostrar_lista_ordenada.agregar_alumno(alumno4)
    mostrar_lista_ordenada.mostrar_lista_ordenada()