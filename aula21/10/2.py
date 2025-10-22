#Aula 21/10/2025


#Classes
class Client():
    # Contrutor
    def __init__(self,name,cpf, address, address_number, address_complement, dt_birth, phone, email):
        #Atributos privados
        self.__name = name
        self.__cpf = cpf
        self.__address = address
        self.__address_number = address_number
        self.__address_complement = address_complement
        self.__dt_birth = dt_birth
        self.__phone = phone
        self.__email = email


    # getters
    @property
    def name(self):
        return self.__name

    @property
    def cpf(self):
        return self.__cpf

    @property
    def address(self):
        return self.__address

    @property
    def address_number(self):
        return self.__address_number

    @property
    def address_complement(self):
        return self.__address_complement

    @property
    def dt_birth(self):
        return self.__dt_birth

    @property
    def phone(self):
        return self.__phone

    @property
    def email(self):
        return self.__email

    # setters
    @name.setter
    def name(self, name):
        self.__name = name

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @address.setter
    def address(self, address):
        self.__address = address

    @address_number.setter
    def address_number(self, address_number):
        self.__address_number = address_number

    @address_complement.setter
    def address_complement(self, address_complement):
        self.__address_complement = address_complement

    @dt_birth.setter
    def dt_birth(self, dt_birth):
        self.__dt_birth = dt_birth

    @phone.setter
    def phone(self, phone):
        self.__phone = phone

    @email.setter
    def email(self, email):
        self.__email = email


#Instancias
#getters
@property
def name(self):
    return self.__name

@property
def cpf(self):
    return self.__cpf

@property
def address(self):
    return self.__address

@property
def address_number(self):
    return self.__address_number

@property
def address_complement(self):
    return self.__address_complement

@property
def dt_birth(self):
    return self.__dt_birth

@property
def phone(self):
    return self.__phone

@property
def email(self):
    return self.__email

#setters
@name.setter
def name(self, name):
    self.__name = name

@cpf.setter
def cpf(self, cpf):
    self.__cpf = cpf

@address.setter
def addres(self, address):
    self.__address = address

@address_number.setter
def address_number (self, address_number):
    self.__address_number = address_number

@address_complement.setter
def address_complement(self, address_complement):
    self.__address_complement = address_complement

@dt_birth.setter
def dt_birth(self, dt_birth):
    self.__dt_birth = dt_birth

@phone.setter
def phone(self, phone):
    self.__phone = phone

@email.setter
def email(self, email):
    self.__email = email


#instancias
client=Client("joao", 12345678900, "rua a", 123, "apto 45", "01/01/2000", 1199999999, "richardgigante@yahoo.com")

# functions
def __str__(self):
    return (
        f"Name: {self.__name}\n"
        f"CPF: {self.__cpf}\n"
        f"Address: {self.__address}, {self.__address_number}, {self.__address_complement}\n"
        f"Date of Birth: {self.__dt_birth}\n"
        f"Phone: {self.__phone}\n"
        f"Email: {self.__email}"
    )


#Exit
print(client.name)
print(client.cpf)
print(client.address)
print(client.address_number)
print(client.address_complement)
print(client.dt_birth)
print(client.phone)
print(client.email)

