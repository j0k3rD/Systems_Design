class Persona:
    def __init__(self, nombre, apellido, dni):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
    
    @property
    def nombre(self):
        return self.__nombre

    @property
    def apellido(self):
        return self.__apellido
    
    @property
    def dni(self):
        return self.__dni

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.dni}"
    

class Alumno(Persona):
    def __init__(self, nombre, apellido, dni, matricula, email, anio_cursado, promedio_nota):
        super().__init__(nombre, apellido, dni)
        self.__matricula = matricula
        self.__email = email
        self.__anio_cursado = anio_cursado
        self.__promedio_nota = promedio_nota
    
    @property
    def matricula(self):
        return self.__matricula
    
    @property
    def email(self):
        return self.__email
    
    @property
    def anio_cursado(self):
        return self.__anio_cursado
    
    @property
    def promedio_nota(self):
        return self.__promedio_nota
    
    def __str__(self):
        return f"{super().__str__()} {self.matricula} {self.email} {self.anio_cursado} {self.promedio_nota}"

    
class ListaAlumnos:
    def __init__(self):
        self.__lista = []
    
    def agregar_alumno(self, alumno):
        self.__lista.append(alumno)
    
    def total_alumnos(self):
        return len(self.__lista)
    
    def total_alumnos_anio(self, anio):
        total = 0
        for alumno in self.__lista:
            if alumno.anio_cursado == anio:
                total += 1
        return total
    
    def promedio_total_anio(self, anio):
        total = 0
        for alumno in self.__lista:
            if alumno.anio_cursado == anio:
                total += alumno.promedio_nota
        return total / self.total_alumnos_anio(anio)
    
    def mejor_promedio_anio(self, anio):
        mejor_promedio = 0
        mejor_alumno = None
        for alumno in self.__lista:
            if alumno.anio_cursado == anio:
                if alumno.promedio_nota > mejor_promedio:
                    mejor_promedio = alumno.promedio_nota
                    mejor_alumno = alumno
        return mejor_alumno


if __name__ == "__main__":
    lista = ListaAlumnos()
    lista.agregar_alumno(Alumno("Juan", "Perez", 12345678, 123, "juan@gmail.com", 1, 8))
    lista.agregar_alumno(Alumno("Maria", "Gomez", 12345678, 123, "mari@gmail.com", 1, 9))
    lista.agregar_alumno(Alumno("Pedro", "Gomez", 12345678, 123, "pedro@gmail.com", 2, 7))
    lista.agregar_alumno(Alumno("Jose", "Perez", 12345678, 123, "jose@gmail.com", 2, 8))
    lista.agregar_alumno(Alumno("Ana", "Gomez", 12345678, 123, "ana@gmail.com", 3, 9))

    print(lista.total_alumnos_anio(1))
    print(lista.total_alumnos_anio(2))
    print(lista.total_alumnos_anio(3))

    print(lista.promedio_total_anio(1))
    print(lista.promedio_total_anio(2))
    print(lista.promedio_total_anio(3))

    print(lista.mejor_promedio_anio(1))
    print(lista.mejor_promedio_anio(2))
    print(lista.mejor_promedio_anio(3))