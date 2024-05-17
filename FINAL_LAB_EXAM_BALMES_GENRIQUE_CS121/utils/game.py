import random
import os
from datetime import datetime
from utils.score import ScoreSystem

class DiceGame:
    def __init__(self):
        self.total_rounds = 3

    def play(self, user):
        total_score = 0
        total_wins = 0
        stage = 1

        while True:
            stage_score, stage_wins = self.play_stage(user, stage)
            total_score += stage_score
            total_wins += stage_wins

            if stage_wins == 0:
                input("Game Over. You lost every round. Press Enter to return to the game menu...")
                break

            if total_wins == 3:
                total_score += 3
                print(f"You won all rounds and earned 3 bonus points! Total points: {total_score}")

            if not self.prompt_continue():
                break

            stage += 1

        self.save_game_result(user, total_score, total_wins)

    def play_stage(self, user, stage):
        stage_score = 0
        stage_wins = 0
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"---- STAGE {stage} ----")

        for _ in range(self.total_rounds):
            user_roll, cpu_roll = self.roll_dice(user)
            if user_roll > cpu_roll:
                print(f"{user.username} wins this round.")
                stage_score += 1
                stage_wins += 1
            else:
                print(f"{user.username} loses this round.")

        print(f"Points this stage: {stage_score}")
        print(f"Total points: {stage_score}")
        return stage_score, stage_wins

    def roll_dice(self, user):
        user_roll = random.randint(1, 6)
        cpu_roll = random.randint(1, 6)
        print(f"{user.username} rolled: {user_roll}, CPU rolled: {cpu_roll}")

        while user_roll == cpu_roll:
            print("It's a draw! Rolling again...")
            user_roll = random.randint(1, 6)
            cpu_roll = random.randint(1, 6)
            print(f"{user.username} rolled: {user_roll}, CPU rolled: {cpu_roll}")

        return user_roll, cpu_roll

    def prompt_continue(self):
        while True:
            choice = input("Continue to next stage? (1 for yes, 0 for no): ")
            if choice in ('1', '0'):
                return choice == '1'
            print("Invalid choice. Please enter 1 or 0.")

    def save_game_result(self, user, total_score, total_wins):
        os.system('cls' if os.name == 'nt' else 'clear')
        score_manager = ScoreSystem()
        score_manager.save_scores(user.username, total_score, total_wins, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def show_leaderboard(self):
        score_manager = ScoreSystem()
        scores = score_manager.load_scores()

        os.system('cls')
        print("==== Top 10 Leading Scores ====")
        if scores:
            scores.sort(key=lambda x: x['score'], reverse=True)
            for i, score in enumerate(scores[:10], 1):
                print(f"{i}. {score['username']} - Score: {score['score']}, Wins: {score['wins']}, Date: {score['date_achieved']}")
        else:
            print("No scores recorded yet.")

        input("Press Enter to return to the game menu...")

    def logout(self):
        pass

    def game_menu(self, user):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Hello, {user.username}! Welcome to the DICE GAME!")
            print("[1] Play Dice Game")
            print("[2] Leaderboards")
            print("[3] Log Out")

            choice = input("Please select an option: ")
            if choice == "1":
                self.play(user)
            elif choice == "2":
                self.show_leaderboard()
            elif choice == "3":
                self.logout()
                break
            else:
                input("Invalid input. Press Enter to try again.")
