from population_functions import city_country

def test_city_country():
    formatted_city_country = city_country('santiago', 'chile')
    assert formatted_city_country == 'Santiago, Chile.'

def test_city_country_population():
    formatted_city_country = city_country('santiago', 'chile', population='5000000')
    assert formatted_city_country == 'Santiago, Chile - Population 5000000.'