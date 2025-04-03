from db import save_rate
from currency import currency_rate


def main():
    print('started')
    currency = "USD"
    today_rate = currency_rate(currency)
    print(f'rate is {today_rate}')
    save_rate(currency, today_rate)
    print('finished')


if __name__ == '__main__':
    main()
