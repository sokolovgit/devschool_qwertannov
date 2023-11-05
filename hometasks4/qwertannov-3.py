class Warrior:

    ranks = ["Pushover", "Novice", "Fighter", "Warrior",
             "Veteran", "Sage", "Elite", "Conqueror",
             "Champion", "Master", "Greatest"]

    def __init__(self):
        self.experience = 100
        self.level = 1
        self.rank = "Pushover"
        self.achievements = []

    def set_stats(self, gained_experience):
        new_experience = self.experience + gained_experience

        if new_experience >= 10000:
            self.experience = 10000
        else:
            self.experience = new_experience

        self.level = self.experience // 100
        self.rank = self.ranks[self.experience // 1000]

    def battle(self, opponent_level):

        if not 1 <= opponent_level <= 100:
            return "Invalid level"

        self_rank = self.level // 10
        opponent_rank = opponent_level // 10

        if self.level == opponent_level:
            self.set_stats(10)
            return "A good fight"
        elif self.level - opponent_level == 1:
            self.set_stats(5)
            return "A good fight"
        elif self.level - opponent_level >= 2:
            return "Easy fight"
        elif self_rank < opponent_rank and opponent_level - self.level >= 5:
            return "You've been defeated"
        else:
            self.set_stats(20 * (opponent_level - self.level) ** 2)
            return "An intense fight"

    def training(self, achievement_description):
        achievement = achievement_description[0]
        experience = achievement_description[1]
        required_level = achievement_description[2]

        if self.level < required_level:
            return "Not strong enough"
        else:
            self.achievements.append(achievement)
            self.set_stats(experience)
            return achievement

