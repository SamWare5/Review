
def make_album (artist_name, album_title, tracks =0):

    if tracks:
        artist = {'artist': artist_name, 'title': album_title,'Tracks' :tracks }
    else :
        artist = {'artist': artist_name, 'title': album_title}


    return artist


Entry01 = make_album("Artist 1 ","Album 1")
Entry02 = make_album("Artist 2 ","Album 2")
Entry03 = make_album("Artist 3 ","Album 3")
Entry04 = make_album("Artist 4 ","Album 4 ",5)

print(Entry01)
print(Entry02)
print(Entry03)
print(Entry04)


print("(enter 'q' at any time to quit)")
print("\nPlease tell me your album :")

while True:

    artist_name = input("Artist Name: ")
    if (artist_name == 'q'):
            break


    album_title = input("Album tile: ")
    if (album_title == 'q'):
            break

    tracks = input(" How Many tracks: ")
    if (tracks == 'q'):
            break
    Continue = input("Enter 'y' to enter next: ")
    if (Continue != 'y'):
            break


Entry05 = make_album(artist_name,album_title,tracks)

print(Entry05)