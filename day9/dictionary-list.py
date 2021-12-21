travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {"country": country_visited, "visits": times_visited, "cities": cities_visited}
    travel_log.append(new_country)


add_new_country(country_visited="Russia", times_visited=2, cities_visited=["Moscow", "Saint Petersburg"])


print(travel_log)
