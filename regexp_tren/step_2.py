"""
Функция findall()
"""

import re

text = "У меня 2 пары носков, 0 рублей на карте, а вообще Я Никита! Мне 999 лет"

numbers = re.findall(r"\d+", text)

print(numbers)  # ['2', '0', '999']
