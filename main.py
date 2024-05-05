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

    def _set_level(self, level):
        self.__level = level



class Admin(User):
    def __init__(self, id, name):
        super().__init__(id, name)
        super()._set_level("admin")
        self.__users = []

    def add_user(self, user):
        if not any(u.get_id() == user.get_id() for u in self.__users):
            self.__users.append(user)
            print(f"Пользователь {user.get_name()} успешно добавлен.")
        else:
            print("Пользователь уже существует.")

    def remove_user(self, user_id):
        for i, user in enumerate(self.__users):
            if user.get_id() == user_id:
                removed_user = self.__users.pop(i)
                print(f"Пользователь {removed_user.get_name()} успешно удален.")
                return
        print("Пользователь не найден.")

    def list_users(self):
        print("----")
        if self.__users:
            print("Список пользователей:")
            for user in self.__users:
                user_info = f"ID: {user.get_id()}, Name: {user.get_name()}, Level: {user.get_level()}"
                print(user_info)

        else:
            print("Список пользователей пуст.")
        print("----")


admin = Admin("007", "Агент")
user1 = User("002", "Иван")
user2 = User("003", "Света из бухгалтерии")
print(admin.get_level() + " " + admin.get_name() + " " + str(admin.get_id()))
print(user1.get_level() + " " + user1.get_name() + " " + str(user1.get_id()))
print(user2.get_level() + " " + user2.get_name() + " " + str(user2.get_id())+ "\n")
admin.add_user(user1)
admin.add_user(user2)
admin.list_users()
admin.remove_user("003")
admin.list_users()
