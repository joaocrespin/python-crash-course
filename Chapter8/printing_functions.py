def test_function():
    '''Use it to test uf the import worked'''
    print("If you are seeing this, the import worked!")

def say_hello(name):
    '''Say hello to any name you put in the parameter "name".'''
    return f'Hello, {name}!'

def bake_bread(time):
    '''Bake a bread for a "minutes" minutes.'''
    time = int(time)
    if time == 60:
        print('Perfect time for a small bread, it smells delicious!')
    elif time < 60:
        print('It\'s raw, no one will eat it.')
    elif time > 60:
        print('Its\'s burnt, no one will eat it...')

def simple_parrot(word):
    '''Says the input back to you'''
    print(word)

def the_end():
    '''The end of the module'''
    print('This chapter was very useful, thank you!')
    return