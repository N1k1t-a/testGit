"""
Первый файлик, где я пробую знакомиться с регулярными выражениями
библа re
"""

import re

text = "сегодня пятница, а завтра суббота"
result = re.search("пятница", text)

if result:
    print(result)
    print(result.group())  # Пятница


result = re.search("понедельник", text)
print(result)  # None
