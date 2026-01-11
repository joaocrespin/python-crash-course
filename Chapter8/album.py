def make_album(artist, title, songs=None):
    album = {'artist': artist, 'title': title}

    if songs:
        album['songs'] = songs

    return album

album = make_album('wonder girls', 'reboot')
print(album)

album = make_album('yves', 'soft error')
print(album)

album = make_album('martinho da vila', 'martinho da vila')
print(album)

album = make_album('lamp', 'for lovers', 8)
print(album)