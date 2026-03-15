"""
Иногда требуется проверить соответствует ли строка формату
"""

import re


def is_phone_number(text):
    pattern = r"^\+7\s?\d{3}\s?\d{3}-\d{2}-\d{2}$"
    return re.match(pattern, text) is not None


print(is_phone_number("+7 123 456-78-90"))
print(is_phone_number("+7123456-78-90"))
print(is_phone_number("123-456-7890"))
