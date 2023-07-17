from user import User
from playlist import view_playlist
from country import Country
from music_info import display_music_info
from spoti import interactive_menu


def main():
    while True:
        print(
            """ ________  ________  ________  _________  ___  ________  ___    ___ 
|\   ____\|\   __  \|\   __  \|\___   ___\\  \|\   __  \|\  \  /  /|
\ \  \___|\ \  \|\  \ \  \|\  \|___ \  \_\ \  \ \  \|\  \ \  \/  / /
 \ \_____  \ \   ____\ \  \\\  \   \ \  \ \ \  \ \   ____\ \    / / 
  \|____|\  \ \  \___|\ \  \\\  \   \ \  \ \ \  \ \  \___|\/  /  /  
    ____\_\  \ \__\    \ \_______\   \ \__\ \ \__\ \__\ __/  / /    
   |\_________\|__|     \|_______|    \|__|  \|__|\|__||\___/ /     
   \|_________|                                        \|___|/      
                                                                    
                                                                    """
        )
        print("1. sign up")
        print("2. log in")
        print("3. show artist")
        print("4. listen music")
        print("5. listen playlist")
        print("6. search for countries")
        print("7. exit")

        option = int(input("choose an option: "))
        if option == 1:
            User.create_user()
        elif option == 2:
            User.login()
        elif option == 3:
            display_music_info()
        elif option == 4:
            interactive_menu()
        elif option == 5:
            view_playlist()
        elif option == 6:
            country_obj = Country()
            country_obj.get_top_songs()
        elif option == 7:
            break
        else:
            print("invalid option, please try again")


if __name__ == "__main__":
    main()
