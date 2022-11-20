def kelvin_to_fahrenheit(kelvin):
    return int(kelvin * 1.8 - 459.67)


def time_convert(base, add):
    hour = (base + add) % 24
    if hour == 0:
        time = "24:00"
    else:
        time = f"{hour}:00"
    return time
