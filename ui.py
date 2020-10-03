from artist_artwork_database import Artist, Artwork
def message(msg):
    print(msg)


def get_new_artist():
    new_artist_name = input('Enter new artist name: ').title()
    new_artist_email = input('Enter new artist email: ')
    print('New artist sucefully added. ')
    return Artist(new_artist_name, new_artist_email)

def get_new_artwork():
    artist_name = input('Enter artist name: ').title()
    artwork_name = input ('Enter artwork name: ').title()
    price = float(input('Enter price (EX: 100000): '))
    available = str(input('Enter availability: '))
    print('New artwork successfully added. ')
    return Artwork(artist_name, artwork_name, price, available)




