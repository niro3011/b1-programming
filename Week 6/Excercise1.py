# Exercise 1: Music Library Manager

# 1. Initialize Data Structures
# TODO: Create an empty list or dictionary to store your music library.
# Each music entry could be a dictionary with keys like 'title', 'artist', 'genre', 'duration'.

music_library = []


# 2. Function to Add Music
# TODO: Define a function that takes music details (title, artist, genre, duration)
# and adds it to your music_library.
# Consider adding validation for input.
def add_song(music_library):
    
    title = input("Please Enter the Title of the Song:")
    artist = input("Please Enter the artist of the Song:")
    genre = input("Please Enter the genre of the Song:")
    duration = input("Please Enter the duration of the Song (MM:SS):")

    song = {
        "title": title,
        "artist": artist,
        "genre": genre,
        "duration": duration
    }
    music_library.append(song)
    print("Song added!")
    return song, title, artist, genre, duration

# 3. Function to Display Music Library
# TODO: Define a function that prints all songs in the library in a formatted way.
# Include options for filtering by artist or genre.
def display_library(music_library):

    print("Your Song Library:")
    for song in music_library:
        print("Title:", song["title"])
        print("By:", song["artist"])
        print("Genre:", song["genre"])
        print("Length: ", song["duration"])
        print(" ")                          #Just for a better overview
#Filtering
def filterby_artist(music_library):
    selected_artist = input("Select the Artist you want to filter: ")
    filter_artist = [song for song in music_library if song["artist"] == selected_artist]
    display_library(music_library, filter_artist)

def filterby_genre(music_library):
    selected_genre = input("Select the Genre you want to filter: ")
    filter_genre = [song for song in music_library if song["genre"] == selected_genre]
    display_library(music_library, filter_genre)



#while True:
#    add_song(music_library)    
#    display_library(music_library)
#    anothersong = input("Do you want to add another Song? (Y/N):")
#    if anothersong != "Y" and anothersong != "y":
#        break

# 4. Main Program Loop
# TODO: Implement a loop that allows the user to:
# - Add new songs
# - View the entire library
# - View songs by a specific artist or genre
# - Exit the program
# Use clear prompts and messages.
# Example usage (after implementing functions):
while True:
    print("\nMusic Library Menu:")
    print("1. Add a new song")
    print("2. View all songs")
    print("3. Filter songs by artist")
    print("4. Filter songs by genre")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        add_song(music_library) 
    if choice == '2':
        display_library(music_library)
    if choice == '3':
        filterby_artist(music_library)
    if choice == '4':
        filterby_genre(music_library)
    elif choice == '5':
        break
# # ... collect input and call add_song ...
# pass

# ... other choices ..