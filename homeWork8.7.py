def make_album(artist_name, album_title):

    artist = {'artist': artist_name, 'title': album_title}
    return artist

artist = make_album('Elvis', 'Twist')
print(artist)
artist = make_album('Bob Marley', 'Amigo')
print(artist)
artist = make_album('Madonna', 'Florida')
print(artist)

def make_album(artist_name, album_title, tracks=''):
    artist = {'artist': artist_name, 'title': album_title}
    if tracks:
        artist['tracks'] = tracks
    return artist
artist = make_album('hendrix', 'Freedom', tracks=27)
print(artist)
artist = make_album('Elvis', 'Twist', tracks=89)
print(artist)



