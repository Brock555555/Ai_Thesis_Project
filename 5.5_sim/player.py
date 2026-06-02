class Player:
    def __init__(self):
        self.health = 100
        self.stamina = 100
        self.money = 20
        self.reputation = 0

        self.inventory = []

    def clamp_stats(self):
        self.health = max(0, min(100, self.health))
        self.stamina = max(0, min(100, self.stamina))