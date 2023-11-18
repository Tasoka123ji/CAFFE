from abc import ABC

class Descriptor(ABC):
    def __init__(self,name,age,email,phone_number) -> None:
        self.__name = name 
        self.__age = age
        self.__email = email
        self.__phone_number = phone_number 

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def setNmae(self,name):
        self.__name = name 
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def setAge(self,age):
        self.__age = age

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def setEmail(self,email):
        self.__email = email

    
    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def setPhone_number(self,phone_number):
        self.__phone_number = phone_number



class User(Descriptor):
    def __init__(self, name, age, email, phone_number) -> None:
        super().__init__(name, age, email, phone_number)