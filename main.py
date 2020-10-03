from artist_artwork_database import Artist, ArtworkArtistDB
import ui

def create_menu():
    print('''
    1. Add new artist
    2. Search Artwork by Artist
    3. Add new Artwork
    4. Display Artwork
    5. Delete Artwork
    6. Display Artwork
    7. Quit
    ''')
    print('Enter a choice: ')
    return(input())


def add_new_artist():
    add_new_artist = ui.get_new_artist()
    try:
        add_new_artist.save()
    except:
        ui.message('\n Artist already in the database. \n')



def add_new_artwork():
    add_new_artwork = ui.get_new_artwork()
    try:
        add_new_artwork.save()
    except:
        ui.message('\nArtwork already in the database. \n')


def quit_program():
    ui.message('Thanks! Adios ')


def main():
    while True:
        select = ''
        select = create_menu()
        if select == '1':
            add_new_artist()
        if select == '2':
            add_new_artwork()
        #if select == '3':
        #    search()
        #if select == '4':
        #    display_all_Art()
        #if select == '5':
        ##    availability()
        #if select == '6':
        #    delete()
        if select == 'q':
            quit_program()
       
            break 
        else:
            print('please enter a valid choice! ')





if __name__ == "__main__":
    main()