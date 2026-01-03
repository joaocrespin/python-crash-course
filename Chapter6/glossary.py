words = {
    'variables': 'Variables are like sticky notes, you are simply writing a name on a label and sticking it onto the data.',
    'list': 'A list is a collection of items organized in a particular order.',
    'insert': 'The insert method allows to insert an element at a given position at a list: list.insert(position, value).',
    'constants': 'Constants are variables that never change.',
    'underscores': 'Underscores are used to make numbers more readable in definitions.',
    'pep8':'PEP 8 is Python\'s official style guide, a set of guidelines for writing clean, readable, and consistent Python code.',
    'reverse':'Reversed is a method used in lists, it allows yopu to reverse the order of the elements on a list permanently.',
    'set':'A set is a collection of data that never repeats.',
    'comments':'Comments explain what the code is supposed to do and how it works.',
    'tuples':'Tuples are immutable lists.',
}

print('---- GLOSSARY ----')
# print(f'Variables: {words.get('variables')}')
# print(f'List: {words.get('list')}')
# print(f'Insert: {words.get('insert')}')
# print(f'Constants: {words.get('constants')}')
# print(f'Underscores:{words.get('underscores')}')

for word, meaning in words.items():
    print(f'{word.capitalize()}: {meaning}')