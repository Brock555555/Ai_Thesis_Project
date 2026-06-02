import random


class NPC:
    def __init__(self, name, archetype):
        self.name = name
        self.archetype = archetype

        self.trust = 50
        self.stress = 0
        self.mood = "neutral"

    def daily_update(self):
        self.stress += random.randint(-5, 10)

        if self.stress < 20:
            self.mood = "calm"

        elif self.stress < 50:
            self.mood = "uneasy"

        else:
            self.mood = "angry"