people = ['mateus', 'matheus', 'lucas', 'ricardo', 'gabriel', 'bruno miguel', 'juan', 'diego']

favorite_languages = {
      'mateus': 'lua',
      'crespin': 'c#',
      'vinicius': 'java',
      'diego': 'php',
      'bruno miguel': 'rust',
      }

for person in people:
    if person in favorite_languages.keys():
        print(f'Hello, {person.title()}! Thank you for responding the poll.')
    else:
        print(f'Can you answer the poll, {person.title()}?')