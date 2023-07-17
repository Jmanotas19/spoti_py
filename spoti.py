from my_music_list import my_list


# Definición de la clase Spotipy
class Spotipy:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def play_music(self):
        print(f"\n⏯️  now playing\n🎶 {self.title}\n🎤 {self.artist}")


# Función para obtener información de my_list y crear una instancia de Spotipy
def find_track(artist_name, track_title):
    for artist_info in my_list:
        if artist_info["name"].lower() == artist_name.lower():
            for track_info in artist_info["popular"]:
                if track_info["track"].lower() == track_title.lower():
                    return Spotipy(track_info["track"], artist_info["name"])


# Función para mostrar el menú interactivo
def interactive_menu():
    while True:
        print("\nchoose an artist from the list:")
        for index, artist_info in enumerate(my_list, 1):
            print(f"{index}. {artist_info['name']}")

        try:
            artist_choice = int(input("\nenter the number of the artist: "))
            if 1 <= artist_choice <= len(my_list):
                selected_artist = my_list[artist_choice - 1]["name"]
            else:
                print("invalid artist number. try again.")
                continue

            print("\npopular tracks by this artist:")
            for index, track_info in enumerate(my_list[artist_choice - 1]["popular"], 1):
                print(f"{index}. {track_info['track']}")

            track_choice = int(input("\nenter the number of the track: "))
            if 1 <= track_choice <= len(my_list[artist_choice - 1]["popular"]):
                selected_track = my_list[artist_choice - 1]["popular"][track_choice - 1]["track"]
                spotipy_instance = find_track(selected_artist, selected_track)
                if spotipy_instance:
                    spotipy_instance.play_music()
            else:
                print("invalid track number. try again.")
                continue
        except ValueError:
            print("invalid input. please enter a number.")
        else:
            continue_option = input("\ndo you want to play another track? (y/n): ")
            if continue_option.lower() != "y":
                break


# Ejecutar el menú interactivo
# interactive_menu()
