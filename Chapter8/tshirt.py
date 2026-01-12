def make_shirt(size, message):
    '''Stitches a shirt of "size" size and a message "message" in it.'''
    print(f'We are producing a size {size.upper()} shirt '
            f'with "{message}" written in it.')

make_shirt('small', 'this is not a big message')
make_shirt(message='I\'m Batman',size='medium')