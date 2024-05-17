import os
from utils.user import User

class UserManager:
    def __init__(self):
        self.users = []
        self.data_directory = "data"
        self.database_file = os.path.join(self.data_directory, "databaseUsers.txt")
        self.load_users()

    def register(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Register an Account (Leave inputs empty to return.)")
            username = input("Username (4 characters minimum): ")
            if not username:
                return
            if not self.is_valid_username(username):
                continue

            password = input("Password (8 characters minimum): ")
            if not password:
                continue
            if not self.is_valid_password(password):
                continue

            if self.username_exists(username):
                input("Username already exists. Try another. Press Enter to try again...")
            else:
                self.users.append(User(username, password))
                self.save_users()
                input("Account Registered! Press Enter to return to main menu...")
                break

    def is_valid_username(self, username):
        if len(username) < 4:
            input("Username must be at least 4 characters. Press Enter to try again...")
            return False
        return True

    def is_valid_password(self, password):
        if len(password) < 8:
            input("Password must be at least 8 characters. Press Enter to try again...")
            return False
        return True

    def username_exists(self, username):
        return any(user.username == username for user in self.users)

    def save_users(self):
        if not os.path.exists(self.data_directory):
            os.makedirs(self.data_directory)
        with open(self.database_file, "w") as file:
            for user in self.users:
                file.write(f"{user.username},{user.password}\n")

    def load_users(self):
        if os.path.exists(self.database_file):
            with open(self.database_file, "r") as file:
                for line in file:
                    username, password = line.strip().split(',')
                    self.users.append(User(username, password))

    def login(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Log In (Leave inputs empty to return.)")
            username = input("Username: ")
            if not username:
                return

            password = input("Password: ")
            if not password:
                continue

            for user in self.users:
                if user.username == username and user.password == password:
                    input("Login Successful! Press Enter to proceed to game menu...")
                    return user

            input("Invalid username or password. Press Enter to try again...")
