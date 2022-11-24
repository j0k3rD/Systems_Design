class New_User():

    usr_info = []
    
    def name(self):
        name = input("Ingrese su nombre: ")
        self.usr_info.append(name)
    
    def lastname(self):
        lastname = input("Ingrese su apellido: ")
        self.usr_info.append(lastname)
    
    def email(self):
        email = input("Ingrese su email: ")
        self.usr_info.append(email)
    
    def nickname(self):
        nickname = input("Ingrese su nickname: ")
        self.usr_info.append(nickname)
    
    def password(self):
        password = input("Ingrese su contraseña: ")
        self.usr_info.append(password)

    def choose_social_network(self):
        social_network = input("Ingrese su red social: ")
        self.usr_info.append(social_network)

    def show_info(self):
        print('Informacion del Usuario creado: ','Nombre:',self.usr_info[0], 'Apellido:',self.usr_info[1], 'Email:',self.usr_info[2], 'Nickname:',self.usr_info[3], 'Contraseña:',self.usr_info[4], 'Red Social:', self.usr_info[5])
    

class FacadeMode():

    def __init__(self):
        self.__new_user = New_User()
    
    def all(self):
        self.__new_user.name()
        self.__new_user.lastname()
        self.__new_user.email()
        self.__new_user.nickname()
        self.__new_user.password()
        self.__new_user.choose_social_network()
        self.__new_user.show_info()


class Creator():

    def __init__(self, facade:FacadeMode):
        self.__facade = facade
    
    def execute(self):
        self.__facade.all()

if __name__ == "__main__":
    facade = FacadeMode()
    creator = Creator(facade)
    creator.execute()