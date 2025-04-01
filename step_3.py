class User:
    def __init__(self, name: str):
        self.name = name
        self.password = None


user = User("john")
user.password = "qwerty1234"

print(user.name, user.password)