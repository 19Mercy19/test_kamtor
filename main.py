import time

import requests
import datetime as dt


key = r"https://data.binance.com/api/v3/ticker/price?symbol="

CURRENC = "XRPUSDT"
HOUR = 3600


def get_price(currencies: str) -> float:
    "Get currencies price."
    url = key + currencies
    data = requests.get(url)
    price = float(data.json()['price'])
    return price


def check_different(value: float, max_value: float) -> str or None:
    "Get different between value and max_value."
    if value / max_value < 0.99:
        print("The price has fallen by 1% from the max in the last hour")


def main() -> None:
    while True:

        check_time = dt.datetime.now()
        current_time = dt.datetime.now()

        diff = (check_time - current_time).seconds

        max_price = 0

        while diff < HOUR:
            price = get_price(CURRENC)
            # print(f"price {price}, \ntime {check_time}\n")
            if max_price < price:
                max_price = price
            # print("max_price", max_price, '\n', 50*'-')
            check_different(price, max_price)
            check_time = dt.datetime.now()
            diff = (check_time - current_time).seconds
            time.sleep(10)

        # print(f"Max from this time {max_price}\n\n\n")


if __name__ == '__main__':
    main()
