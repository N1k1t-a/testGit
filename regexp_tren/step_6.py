"""
Иногда нам нужно из, найденного совпадения, извлечь отдельные части
"""

import re

date_only = "03.05.2006"

group_date = re.search(r"(\d{2})\.(\d{2})\.(\d{4})", date_only)

if group_date:
    day = group_date.group(1)
    month = group_date.group(2)
    year = group_date.group(3)

    print(f"your pa was born in {day=}, {month=}, {year=}")  # your pa was born in day='03', month='05', year='2006'
