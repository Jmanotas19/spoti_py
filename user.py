import datetime
import json
import getpass
import re


class User:
    def __init__(self, user_name, password, email, birthdate, country):
        self.user_name = user_name
        self.__password = password
        self.email = email
        self.__birthdate = birthdate
        self.__country = country
        self.creation_date = datetime.datetime.now()

    def __str__(self):
        return f"\nUSER DATA\n{'=' * 25}\nuser name\t{self.user_name}\npassword\t{self.__password}\nemail\t\t{self.email}\nregion\t\t{self.__country}\nbirthdate\t{self.__birthdate}\ncreation date\t{self.creation_date.strftime('%Y-%m-%d')}\n{'=' * 25}"

    def verify_email(self):
        while True:
            patron = r"\w+@"
            verificar = re.search(patron, self.email)
            if verificar:
                return True
            print("== sorry, invalid email format ==")
            self.email = input("please enter a valid email address: ")

    @staticmethod
    def login():
        print("\t\tlogin\n")
        # Pedir datos
        while True:
            username = input("enter your username: ")
            password = getpass.getpass("enter your password: ")
            # Buscar usuario en la lista de usuarios
            with open("data.json", "r", encoding="utf-8") as file:
                users_dict = json.load(file)
            if username in users_dict and users_dict[username]["password"] == password:
                user_info = users_dict[username]
                user = User(
                    user_info["user_name"],
                    user_info["password"],
                    user_info["email"],
                    user_info["birthdate"],
                    user_info["country"],
                )
                print(user)
                break
            print("\ninvalid username or password\n")

    @staticmethod
    def create_user():
        while True:
            try:
                with open("data.json", "r", encoding="utf-8") as file:
                    users_dict = json.load(file)
            except FileNotFoundError:
                users_dict = {}

            print("\n\t\t\tcreate a new user\n")
            while True:
                user_name = input("enter username: ")
                if user_name in users_dict:
                    print("this username is already taken")
                else:
                    break
            while True:
                email = input("enter email address: ")
                if email in [user_info["email"] for user_info in users_dict.values()]:
                    print("this email already exists")
                else:
                    break

            password = getpass.getpass("enter password: ")
            birthdate = input("enter birthdate (YYYY-MM-DD): ")
            birthdate_formatted = f"{birthdate[:4]}-{birthdate[4:6]}-{birthdate[6:]}"
            country = input("enter country of residence: ")
            new_user = User(user_name, password, email, birthdate_formatted, country)
            if not new_user.verify_email():
                continue

            user_info = {
                "user_name": user_name,
                "password": password,
                "email": email,
                "birthdate": birthdate_formatted,
                "country": country,
                "creation_date": datetime.datetime.now().strftime("%Y-%m-%d"),
            }

            users_dict[user_name] = user_info
            break

        with open("data.json", "w", encoding="utf-8") as file:
            json.dump(users_dict, file, indent=4)
        print(f"\nuser '{new_user.user_name}' created successfully")


# User.create_user()

# User.login()
