languages = ['english','spanish','portuguese','chinese','korean','french']

print(languages)

languages.append('italian')
languages.insert(3,'assembly')

print(languages)

del languages[4]
languages.pop()

print(languages)

languages.remove('assembly')

print(sorted(languages))
print(languages)

languages.sort()
print(languages)

languages.reverse()
print(languages)

print(len(languages))