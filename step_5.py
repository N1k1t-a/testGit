WEATHER_FORECAST = {
    "moscow": {
        "temp": 5,
        "rain_chance": 52,
    },
    "sochi": {
        "rain_chance": 20,
    },
}


def get_weather(city: str) -> dict:
    forecast = WEATHER_FORECAST.get(city)
    if not forecast:
        raise ValueError(f"no data sor city {city!r}")

    return forecast


def rain_tomorrow(city: str) -> bool | None:
    print("Will it rain", city)
    try:
        weather = get_weather(city)

    except ValueError:
        return

    return weather["rain_chance"] > 50


print(rain_tomorrow("moscow"))
print(rain_tomorrow("moscw"))
