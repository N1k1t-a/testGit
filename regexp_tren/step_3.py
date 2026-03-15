"""
Создаем шаблон с поиском всех почтовых адресов
"""

import re

text = "Пишите нам на info@example.com или support@domain.org"
all_emails = re.findall(r"\w+@\w+.\w+", text)
print(all_emails)
