#
#  ! Start display
format_output = "\033[34m"
format_output2 = "\033[31m"
format_reset = "\033[0m"

print(f"\n {format_output}---Playlist App - Do you like cool music? Let's find out!---{format_reset}")

#! using my actual playlist to start
playlist = {
    "Lithium": {"artist": "Evanescence", "genre": "alt-rock"},
    "Emily": {"artist": "Bowling for Soup", "genre": "alt-rock"},
    "Jesus of Suburbia": {"artist": "Greenday", "genre": "punk rock"},
    "My Happy Ending": {"artist": "Avril Lavigne", "genre": "alt-rock"},
    "Call Me When You're Sober": {"artist": "Evanescence", "genre": "alt-rock"},
    "Pon Pon Pon": {"artist": "Kyary Pamyu Pamyu", "genre": "J-pop"},
    "Black Lip": {"artist": "Tokyo Gegegay", "genre": "J-electropop"},
    "Gimme Chocolate!!": {"artist": "Baby Metal", "genre": "J-metal"},
    "The Beginning": {"artist": "ONE OK ROCK", "genre": "J-rock"},
}


#! Main menu
def start_app():
    while True:
        print("\nPlaylist Menu:")
        print("1. Add a new song")
        print("2. Update song, artist and genre")
        print("3. Take a look at your full playlist")
        print("4. Delete a song because it's trash")
        print("5. Exit")

        option = input("Type 1, 2, 3, 4 or 5 only: ").lower()
        if option == "1":
            add_song()
        elif option == "2":
            update_song()
        elif option == "3":
            view_playlist()
        elif option == "4":
            delete_song()
        elif option == "5":
            print("Thanks for checking out and/or adding to the playlist! See ya!")
            break
        else:
            print("Maybe that was a mistake... Please select 1, 2, 3, 4 or 5.")

#! add a new song
def add_song():
    print("\n--- Add a Song ---")
    title = input("Enter the song's title: ").lower()
    if not title:
        print("Oops... The title cannot be empty! Please enter a valid title.")
        return add_song()  
    if title in playlist:
        print(f"Looks like '{title}' is already on the playlist. Maybe you forgot?")
        print("No worries, though. You can update it if needed from menu '2'.")
        return
    artist = input("Who's the artist (or band)? ").lower()
    if not artist:
        artist = "Unknown Artist"  
        print("Set as 'Unknown Artist' for now. You can update this later.")
    genre = input("What genre does it belong to? ").lower()
    if not genre:
        genre = "Misc" 
        print("Genre set to 'Misc' ... because I have no idea.")
    try:
        if title == "":
            raise ValueError("The song title needs something entered.")
        playlist[title] = {"artist": artist, "genre": genre}
        print("\nNice! Added this to your playlist:")
        print(f"Title: {title.title()}")
        print(f"Artist: {artist.title()}")
        print(f"Genre: {genre.title()}")
        
    except ValueError as error1:
        print(f"\n {error1}")
        return

#! show the current playlist
class PlaylistEmpty(Exception):
    pass
def view_playlist():
        print("\n--- Your Playlist ---")
    
        try:
            if not playlist:
                raise PlaylistEmpty("Oh no! EMPTY??? No music = No good vibes!")
            print("\nHere’s what you’ve got so far:")
            for title, details in playlist.items():
                artist = details.get("artist", "Unknown Artist")
                genre = details.get("genre", "Misc")
                print(f"{format_output}{title.title()} by {artist.title()} [{genre.title()}]{format_reset}")
            print("\nAre we considered cool yet? Add more songs if you want!")
        except PlaylistEmpty as error3:
            print(error3)
            print("Get to adding some new songs!")

#! update a song
def update_song():
    print("\n--- Update a Song ---")
    title = input("What song are we updating? ").lower()
    try:
        if title not in playlist:
            raise KeyError(f"Uhhhhh... '{title}' isn't on your playlist.")
        current_details = playlist[title]
        print("\nHere’s the song details:")
        print(f"Title: {title.title()}")
        print(f"Artist: {current_details.get('artist', 'Unknown Artist').title()}")
        print(f"Genre: {current_details.get('genre', 'Uncategorized').title()}")
        print("\nAlright! Let’s update it!")
        new_title = input("New song title (leave blank if no change): ").lower() or title
        new_artist = input("New artist (or band) name (leave blank if no change): ").lower() or current_details["artist"]
        new_genre = input("New genre (leave blank if no change): ").lower() or current_details["genre"]
        if new_title != title:
            del playlist[title]  
        playlist[new_title] = {"artist": new_artist, "genre": new_genre}
        print("\nGreat! Here’s the updated song info:")
        print(f"Title: {new_title.title()}")
        print(f"Artist: {new_artist.title()}")
        print(f"Genre: {new_genre.title()}")
    except KeyError as error2:
        print(f"\n {error2}")
        view_playlist() 
        return

#! This deletes the song
def delete_song():
    print("\n--- Let's Remove a Song ---")
    try:
        title = input("Which song do you want to get rid of? ").lower()
        if title not in playlist:
            raise KeyError(f"Oops! '{title}' isn’t on your playlist. Spelling?")
        del playlist[title]
        print(f"\n{title.title()} has been removed. Hope you won’t miss it too much... or maybe you will?")
    except KeyError as error4:
        print(f"\n{error4} No worries. Try again or just do it later.")

start_app()
