favorite_places = {
    'crespin': ['são josé dos campos'],
    'malu': ['são paulo', 'belo horitzonte'],
    'andre': ['chile', 'greece', 'italy'],
}

for name, places in favorite_places.items():
    if len(places) > 1:
        print(f"\n{name.capitalize()}'s favorite places are:")
        for place in places:
            print(f'\t{place.title()}')
    else:
        print(f"\n{name.capitalize()}'s favorite place is: {places[0].title()}")