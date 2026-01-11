def city_country(city, country):
    return f'{city.title()}, {country.title()}'

place = city_country('guarulhos', 'brazil')    
print(place)

place = city_country('seoul', 'south korea')    
print(place)

place = city_country('paris', 'france')    
print(place)