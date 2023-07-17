from my_music_list import my_list


def display_music_info():
    """Displays information about artists, albums, and songs in the music list.

    - Iterate through the music list and display the names of the artists.
    - Ask the user to input the name of an artist.
    - If the artist's name is in the list, show information about the artist, including:
    * Artist's name.
    * Number of listeners.
    * Most popular songs and their number of listeners.
    * Albums and their release years.
    - If the artist's name is not in the list, prompt the user to try again.

    Returns:
    - Does not return anything.
    - Prints information about artists and their albums and songs in the music list."""

    for artist in my_list:
        print(f"• {artist['name']}")
    print()
    while True:
        artist_name = input("type the artist name: ").lower()
        for artist in my_list:
            if artist_name == artist["name"].lower():
                print(f"\nName\t\t🎙️  {artist['name']}")
                print(f"Listeners\t🎧 {artist['listeners']:,}")
                print("Popular tracks")
                for track in artist["popular"]:
                    print(f"  • {track['track']} - {track['listeners']:,}")
                print("Albums")
                for album in artist["albums"]:
                    print(f"  • {album['title']} ({album['year']})")
                print()
                return
        print("the artist searched for was not found. please try again.\n")
