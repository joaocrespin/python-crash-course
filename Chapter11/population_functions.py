def city_country(city, country, population=''):
    if population:
        return f'{city.title()}, {country.capitalize()} - Population {population}.'
    return f'{city.title()}, {country.capitalize()}.'