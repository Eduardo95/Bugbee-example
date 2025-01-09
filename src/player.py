def number_conversion(number):
    dict = {"30": ["Stephen", "Curry"],
            "24": ["Kobe", "Bryant"],
            "11": ["Ming", "Yao"]}
    return dict[number]


def team_conversion():
    numbers = ["30", "24", "11"]
    return ", ".join([number_conversion(number) for number in numbers])
