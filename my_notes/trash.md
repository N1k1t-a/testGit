# Это просто моя мусорка

Здесь не будет ничего важного

is - происходит сравнение по ячейки в памяти. А == производит сравнение по значениям

```python
from dataclasses import dataclass


@dataclass(frozen=True) # frozen = True означает, что поля датаклассов неизменяемы
class Aboba:
    name: str
    age: int


object_class = Aboba(name="John", age=19)

# При попытке изменить любое поле код упадет с ошибкой dataclasses.FrozenInstanceError
object_class.age=19
# Об этом даже IDE подсказывает

```
`
еще короче, если мы используем в dataclass frozen=True, то тогда можно подписывать slots=True
потому что это делает хранение датаклассов более эффективным
`
```python
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Example:
    pass
```

`
также по еще по фишкам датаклассов
можно такие классы преобразоывавать в словарь с помощью функции asdict
`

```python
from dataclasses import dataclass, asdict


@dataclass
class EmployeeName:
    first_name: str
    last_name: str

my_employee = EmployeeName(first_name="Nikita", last_name="Telegin")

my_employee_dict: dict = asdict(my_employee)
print(my_employee_dict) # Выведется словарь
```

## Исключения стоит обрабатывать там, где мы можем с ними разумно справиться


## JSON

`
json, он же JavaScript Object Notation - это текстовый формат для хранения и обмена данными. По сути, это способ
представить словари, списки и атомарные значения в виде строки
`

Дла работы с **json** в питончике есть модуль json
пример кода
```python
import json

data_dict = {
    "name": "Nikita",
    "age": 20,
    "is_active": True,
    "skills": [
        "python",
        "json"
    ],
}

data_json = json.dumps(data_dict) # с помощью dumps мы преобразовывем словарь в json
# Но в таком случае кириллица закодировалась. Чтобы такого не происходило надо добавить параметр
data_json_too = json.dumps(data_dict, ensure_ascii=False, indent=4) # с помощью indent мы добавляем отступов в строку

# если же нам требуется записать json в файл, мы должны использовать dump()

with open("aboba.json", "w") as f:
    json.dump(data_json_too, f)

# Чтобы преобразовать json файл в словарь, нужно использовать loads()

data_dict_too = json.loads(data_json)
```

`
Важная штука, о которой часто не упоминают обучающие материалы. Модуль json работает только с базовыми типами Python: 
dict, list, str, int, float, bool и None. Проблема возникает, если мы хотим сериализовать более сложные объекты, 
например, datetime или decimal.Decimal.
`
```python
from datetime import datetime
from decimal import Decimal
import json

data = {
    "price": Decimal("19.99"),
    "created_at": datetime(2026, 3, 14, 1, 46)
}
print(json.dumps(data))
# Такой код упадет с ошибкой!
```

```python
"""
Чтобы мы могли превращать в json эти типа, 
мы можем передавать в default функцию, которая их преобразовывает"""
from datetime import datetime
from decimal import Decimal

import json


def custom_serializer(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError(f"Type {type(obj)} not serializable")

data = {
    "price": Decimal("19.13"),
    "created_at": datetime(2026, 3, 14, 1, 46),
}

print(json.dumps(data, default=custom_serializer, indent=True))

```
## orjson 
ну конечно же наш православный json хорош. Но когда мы хотим сделать процесс быстрее, нам нужен новый модуль orjson
он уже не встроенный, его надо скачивать 

```python
import orjson

data = {
    "name": "Nikita",
    "age": 1000,
}

data_json = orjson.dumps(data)
print(data_json.decode()) # функция decode приводит байты к utf-8
```

Чтобы сериализовать _datetime_, нужно указать опции:
```python
from datetime import datetime

import orjson

print(
    orjson.dumps({"now": datetime.now()}, option=orjson.OPT_NAIVE_UTC)
)
```