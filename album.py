from spoti import Spotipy


class Album(Spotipy):
    def __init__(self, title, artist, year):
        super().__init__(title, artist)
        self.year = year

    def play_music(self):
        print(f"\n⏯️  now playing\n💽 {self.title} ({self.year})\n🎤 {self.artist} ")


album = Album("Harry's House", "Harry Style", 2022)
album.play_music()
