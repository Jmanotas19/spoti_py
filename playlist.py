class Playlist:
    def __init__(self, playlist_name, author):
        self.playlist_name = playlist_name
        self.author = author
        self.tracks = []


# List of available playlists
playlists = [
    Playlist("Best of Red Hot Chili Peppers", "jmanotas"),
    Playlist("Greatest Hits of One Direction", "jmanotas"),
    # Add more playlists here
]


def play_song(song, artist):
    print(f"\n⏯️  Now playing\n🎶 {song}\n🎤 {artist}")


def view_playlist():
    print("Available playlists:")
    for i, playlist in enumerate(playlists):
        print(f"{i+1}. {playlist.playlist_name}")
    while True:
        try:
            choice = int(input("Choose a playlist: "))
            selected_playlist = playlists[choice - 1]
            print(f"\nShowing playlist - {selected_playlist.playlist_name} by {selected_playlist.author}")
            for idx, track in enumerate(selected_playlist.tracks, 1):
                print(f"{idx}. {track}")
            while True:
                try:
                    song_choice = int(input("Choose a song to play: "))
                    selected_song = selected_playlist.tracks[song_choice - 1]
                    play_song(selected_song, selected_playlist.playlist_name)
                    break
                except (ValueError, IndexError):
                    print("Invalid song number. Please choose a valid song number.")
            break
        except (ValueError, IndexError):
            print("Invalid playlist number. Please choose a valid playlist number.")


# Add songs to a playlist
playlists[0].tracks.append("Under the Bridge")
playlists[0].tracks.append("Californication")
playlists[0].tracks.append("Otherside")
playlists[0].tracks.append("Dark Necessities")
playlists[0].tracks.append("Snow")
playlists[1].tracks.append("Stockholm Syndrome")
playlists[1].tracks.append("Story of My Life")
playlists[1].tracks.append("18")
playlists[1].tracks.append("Best Song Ever")
playlists[1].tracks.append("Perfect")
# You can add more songs to other playlists here

# Execute the view_playlist() function
# view_playlist()
