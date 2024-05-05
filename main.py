import random
class User:
    def __init__(self, id, name, level="user"):
        self.__id = id
        self.__name = name
        self.__level = level
    def get_name(self):
        return self.__name
    def get_level(self):
        return self.__level
    def get_id(self):
        return self.__id

    def set_name(self, name):
        self.__name = name



class Admin(User):
    def __init__(self, id, name):
        super().__init__(id, name)
        self.__level = "admin"
        self.__users = []

admin = Admin("007", "Агент")
user1 = User("002", "Иван")
user2 = User("003", "Света из бухгалтерии")

