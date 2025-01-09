def number_conversion(number):
    dict = {"30": "Stephen",
            "24": "Kobe",
            "11": "Ming"}
    return dict[number]


def team_conversion():
    numbers = ["30", "24", "11"]
    return ", ".join([number_conversion(number) for number in numbers])
