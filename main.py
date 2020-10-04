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
    except Exception as e:  # avoid plain except statements 
        # this is not the only reason something can go wrong. you are hiding a lot of potential errors
        # with a blank except statement. If you catch an exception it's helpful to know 
        # what type, what the error message is 

        # This is the error you are actually getting, it's not an integrity error at all, it's a coding error 
        # 'Artwork' object has no attribute 'name'
        print(e)
        ui.message('\nArtwork already in the database. \n')


def quit_program():
    ui.message('Thanks! Adios ')


def main():
    while True:
        select = ''
        select = create_menu()
        if select == '1':
            add_new_artist()

        # use if, elif, elif ...... else 
        # elif select == '2':   # this matches your menu's choices?
        #    search() 
        elif select == '3':       # option 3 for add new artwork?
            add_new_artwork() 
        #if select == '4':
        #    display_all_Art()
        #if select == '5':
        ##    availability()
        #if select == '6':
        #    delete()
        elif select == 'q':
            quit_program()
       
            break 
        else:
            print('please enter a valid choice! ')





if __name__ == "__main__":
    main()