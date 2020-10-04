import sqlite3
import os 


db = os.path.join('artworkStore.db')

class Artist:

    def __init__(self, name, email, id = None):
        self.name = name
        self.email = email
        self.id = id

        self.artworkStore = ArtworkArtistDB()

    def save(self):
        self.artworkStore.add_artist(self)


    def __str__(self):
        return f'ID: {self.id}, Name{self.name}, Email{self.name}'

    def __repr__(self):
        return f'ID: {self.id}, Name{self.name}, Email{self.name}'



class Artwork:

    def __init__(self, artistname, artname, price, availability, id = None):
        self.artistname = artistname
        self.artname = artname
        self.price = price
        self.availability = availability
        self.id = id

        self.artworkStore = ArtworkArtistDB()

    def save(self):
        self.artworkStore.add_artwork(self)


    def __str__(self):
        return f'ID: {self.id}, Name {self.artistname}, Artwork Name:{self.artname}, Price{self.price}, Available{self.availability}'

    def __repr__(self):
        return f'ID: {self.id}, Name {self.artistname}, Artwork Name{self.artname}, Price{self.price}, Available{self.availability}'

    

class ArtworkArtistDB:

    def __init__(self):
        with sqlite3.connect(db) as conn:
            conn.execute('CREATE TABLE IF NOT EXISTS Artist(ArtistName TEXT UNIQUE, Email TEXT)')
            conn.execute('CREATE TABLE IF NOT EXISTS Artwork(ArtistName TEXT UNIQUE, ArtworkName TEXT UNIQUE, Price REAL, Available TEXT)')
            # conn.commit()  # not needed. Using the with structure will commit changes 
        
        conn.close()

            


    def add_artist(self, artist):

        insert_sql = 'INSERT INTO Artist(ArtistName , Email) VALUES(?,?)'
        
        

        try:
            with sqlite3.connect(db) as conn:
                rows_modified = conn.execute(insert_sql,(artist.name, artist.email))
           
            return rows_modified
        except sqlite3.IntegrityError as e:
            raise ArtistError(f'Error adding {artist.name}') from e
        finally:
        
            conn.close()


    def add_artwork(self, artworks):
        #insert_sql =  'INSERT INTO Artwork'

        # also make sure column names are correct
        insert_sql = 'INSERT INTO Artwork(ArtistName, ArtworkName, Price, Available) VALUES (?,?,?,?)'
        

        try:
            with sqlite3.connect(db) as conn:
                # be careful with attributes 
                rows_modified = conn.execute(insert_sql, (artworks.artistname, artworks.artname, artworks.price, artworks.availability))
            return rows_modified
        except sqlite3.IntegrityError as e:
            print(e)
            # this is not the only reason you can get an intergiry error. 
            raise ArtworkError(f'Error - this artwork is already in the database. {artworks.name}') from e
        finally:
            
            #conn.commit()
            conn.close()


class ArtistError(Exception):
    pass

class ArtworkError(Exception):
    pass

