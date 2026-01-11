def make_album(artist, title, songs=None):
    album = {'artist': artist, 'title': title}

    if songs:
        album['songs'] = songs

    return album

while True:
    print(f'\nEnter an album\'s artist and tile (say "q" to quit):')
    
    artist = input('Artist: ')
    if artist == 'q':
        break
    
    title = input('Title: ')
    
    if title == 'q':
        break
    
    print(make_album(artist, title))