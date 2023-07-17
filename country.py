import random
from my_music_list import my_list


class Country:
    country_list = ["colombia", "usa", "spain", "france"]

    def __init__(self):
        self.track_list = [(song["track"], e["name"]) for e in my_list for song in e["popular"]]

    def get_top_songs(self):
        country = input("enter the country >>> ")
        if country.lower() in self.country_list:
            random.shuffle(self.track_list)
            top_songs = self.track_list[:10]
            print(f"top 10 {country.upper()}")
            for i, j in enumerate(top_songs, 1):
                print(f"[{i}] {j[0]} - {j[1]}")
        else:
            print(f"sorry - '{country}' is not available, perhaps in future updates it will be")


# country_obj = Country()
# country_obj.get_top_songs()
