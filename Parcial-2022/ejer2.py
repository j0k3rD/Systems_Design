from abc import ABC, abstractmethod

from numpy import isin

class Individuo(ABC):
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

    def mostrar_informacion(self):
        return f'{self.__nombre}, {self.__apellido}, {self.__dni}'


class Estudiante(Individuo):
    def __init__(self, nombre, apellido, dni):
        super().__init__(nombre, apellido, dni)


class Profesor(Individuo):
    def __init__(self, nombre, apellido, dni, cv, skills):
        super().__init__(nombre, apellido, dni)
        self.__cv = cv
        self.skills = skills
        
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

    @property
    def cv(self):
        return self.cv

    @cv.setter
    def cv(self, cv):
        self.cv = cv    

    def agregar_skill(self):
        nueva_skill = input('Ingrese su nueva habilidad: ')
        self.skills.append(nueva_skill)


class TallerDeCapacitacion():
    def __init__(self, fecha, tema) -> None:
        self.fecha = fecha
        self.tema = tema
        self.grupo_profesores = []
        self.estudiantes = []

    def agregar_individuo(self, individuo):
        if isinstance(individuo, Profesor):
            self.grupo_profesores.append(individuo)
        elif isinstance(individuo, Estudiante):
            self.estudiantes.append(individuo)
        return 'Individio Agregado'

    def mostrar_profesores(self):
        for profesor in self.grupo_profesores:
            return(profesor.mostrar_informacion())
    
    def mostrar_estudiantes(self):
        for estudiante in self.estudiantes:
            return(estudiante.mostrar_informacion())

    def mostrar_info_taller(self):
        return f'Fecha: {self.fecha}, Tema: {self.tema}, Profesores: {self.mostrar_profesores()}, Estudiantes: {self.mostrar_estudiantes()}'


if __name__=="__main__":
    estudiante1 = Estudiante('Aaron', 'Moya', 42750981)
    estudiante2 = Estudiante('Marcos', 'Miglierina', 43123456)
    estudiante3 = Estudiante('Nicolas', 'Mayoral', 42567890)

    profesor1 = Profesor('Raul', 'Fonseca', 123456728, 'CV', ['Python', 'Java', 'Golang', 'TypeScript'])
    profesor2 = Profesor('Fernando', 'Rosado', 123456789, 'CV', ['Python', 'Java', 'Golang', 'TypeScript'])
    profesor3 = Profesor('Juan', 'Perez', 123456789, 'CV', ['Python', 'Java', 'Golang', 'TypeScript'])


    taller1 = TallerDeCapacitacion('2021-10-10', 'Python')
    
    taller1.agregar_individuo(estudiante3)
    taller1.agregar_individuo(profesor1)
    taller1.agregar_individuo(estudiante2)
    taller1.agregar_individuo(profesor2)

    print(taller1.mostrar_info_taller())