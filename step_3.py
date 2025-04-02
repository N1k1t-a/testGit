class User:
    def __init__(self, name: str):
        self.name = name
        self._password = None

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self.set_password(value)

    def set_password(self, new_password):
        self._password = hash(new_password)

    def password_valid(self, password) -> bool:
        return hash(password) == self.password


user = User("john")
user.password = "qwerty1234"

print(user.name, user.password)

print(user.password_valid("qwrty"))
print(user.password_valid("qwerty1234"))
