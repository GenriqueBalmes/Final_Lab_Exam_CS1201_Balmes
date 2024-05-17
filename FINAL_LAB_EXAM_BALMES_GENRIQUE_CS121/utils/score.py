import os

class ScoreSystem:
    def __init__(self):
        self.data_directory = "data"
        self.scores_file = os.path.join(self.data_directory, "gameScores.txt")
        self.ensure_data_directory()

    def ensure_data_directory(self):
        if not os.path.exists(self.data_directory):
            os.makedirs(self.data_directory)

    def save_scores(self, username, score, wins, date_achieved):
        with open(self.scores_file, "a") as file:
            file.write(f"{username},{score},{wins},{date_achieved}\n")

    def load_scores(self):
        scores = []
        if os.path.exists(self.scores_file):
            with open(self.scores_file, "r") as file:
                for line in file:
                    username, score, wins, date_achieved = line.strip().split(',')
                    scores.append({
                        "username": username,
                        "score": int(score),
                        "wins": int(wins),
                        "date_achieved": date_achieved
                    })
        return scores
