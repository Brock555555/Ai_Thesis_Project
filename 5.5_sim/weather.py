import random


def random_weather():
    weather_types = [
        "Sunny",
        "Cloudy",
        "Rainy",
        "Heatwave",
        "Foggy"
    ]

    return random.choice(weather_types)