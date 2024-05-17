import os
from utils.user_manager import UserManager
from utils.game import DiceGame

class MainApp:
    def __init__(self):
        self.user_manager = UserManager()
        self.dice_game = DiceGame()

    def display_menu(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("==== Welcome to Dice x Dice ====")
        print("[1] Register")
        print("[2] Log In")
        print("[3] Exit")

    def main(self):
        while True:
            self.display_menu()
            choice = input("Please select an option: ")
            if choice == "1":
                self.user_manager.register()
            elif choice == "2":
                user = self.user_manager.login()
                if user:
                    self.dice_game.game_menu(user)
            elif choice == "3":
                print("Goodbye!")
                exit()
            else:
                input("Invalid selection. Press Enter to retry...")

if __name__ == "__main__":
    app = MainApp()
    app.main()
