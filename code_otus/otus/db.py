def get_rates(currency, dttm):
    return {
        '12:00:01': 30.5,
        '14:00:05': 31.7
    }


def save_rate(currency, rate):
    print(f'saved to db {currency} ({rate})')