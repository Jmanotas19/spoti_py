from my_music_list import my_list
from spoti import Spotipy


class Artist(Spotipy):
    def __init__(self):
        pass

    def list_artists(self):
        artists = [entry["name"] for entry in my_list]
        print("Artists available:")
        for i, artist in enumerate(artists):
            print(f"{i+1}. {artist}")
        return artists

    def get_music_info(self):
        artists = self.list_artists()
        while True:
            artist_choice = input(" enter the number of the artist you want to listen to: ")
            if artist_choice.isdigit() and int(artist_choice) in range(1, len(artists) + 1):
                artist_choice = int(artist_choice)
                break
            print("invalid choice. Please enter a valid number.")

        chosen_artist = artists[artist_choice - 1]
        chosen_artist_songs = [
            entry["popular"] for entry in my_list if entry["name"] == chosen_artist
        ][0]

        print(f"{'='*30}\n{chosen_artist} songs available:")
        for i, song in enumerate(chosen_artist_songs):
            print(f"{i+1}. {song['track']}")

        while True:
            song_choice = input("   enter the number of the song you want to play: ")
            if song_choice.isdigit() and int(song_choice) in range(1, len(chosen_artist_songs) + 1):
                song_choice = int(song_choice)
                break
            print("invalid choice. Please enter a valid number.")

        chosen_song = chosen_artist_songs[song_choice - 1]["track"]
        super().play_music(chosen_artist, chosen_song)


# Ejemplo de reproducción de canción
mml = Artist()
mml.get_music_info()
