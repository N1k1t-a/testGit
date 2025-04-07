from pydantic import BaseModel, Field, constr, conint


def default_value() -> list[str]:
    return ["sale"]


class User(BaseModel):
    id: int
    name: str
    email: str = None
    username: constr(min_length=4, max_length=32)
    age: conint(ge=17)

    account_id: int = Field(default=None, alias="accountId")

    def inc_age(self):
        self.age += 1

    class Config:
        validate_assignment = True  # Позволяет проверять (валидировать) значения при присваивании новых значений уже существующим полям модели.
        validate_by_name = True  # Разрешает инициализацию (создание экземпляра) модели по именам полей, даже если у них есть алиасы (alias).


class Product(BaseModel):
    price: float
    weight: int
    categories: list[str] = Field(default_factory=default_value)

    class Config:
        frozen = True # делаем так, чтобы объекты были неизменяемы


def main():
    admin = User(id=1,
                 name="admin",
                 username="александра",
                 age=18
                 )
    print(admin)
    print([admin])

    user_data = {
        "age": 50,
    }

    john = User(
        id=1,
        name="john",
        username="john",
        **user_data,
        account_id=1
    )

    print(john)
    john.inc_age()
    print(john)


    bread = Product(price=55.2, weight=100)
    print(bread)
    bread.categories.append('mild')
    print(bread)

    milk = Product(price=12.3, weight=122)
    print(milk)
    milk.categories.append("xyeta")
    print(milk)


if __name__ == "__main__":
    main()
