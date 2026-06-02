import random

class Story:
    def __init__(self):
        self.reset_game()

    def reset_game(self):
        """Reset game to initial state"""
        self.day = 0
        self.grapes = 0
        self.state = "intro"
        self.text = ""
        self.choices = []
        self.get_scene(increment_day=False)

    def get_scene(self, increment_day=True):
        """Set text and choices depending on current state."""
        
        # Check win/lose condition at Day 7
        if self.day > 7:
            if self.grapes >= 20:
                self.state = "win"
            else:
                self.state = "lose"

        # --- INTRO ---
        if self.state == "intro":
            self.text = (
                "Welcome to the Grape Odyssey!\n\n"
                "You’ve arrived at Grape Valley Vineyard. "
                "Your goal is to collect 20 grapes by Day 7.\n"
                "Beware of squirrels, mysterious traders, and bizarre events!"
            )
            self.choices = [
                ("Start Picking Grapes", "vineyard", True),
                ("Visit Market", "market", True),
                ("Take a Nap", "nap", True),
                ("Quit / Restart", "restart", False)
            ]

        # --- VINEYARD ---
        elif self.state == "vineyard":
            gain = random.randint(1, 4)
            event = random.choice([
                "A squirrel steals a grape from your basket.",
                "You find a tiny golden grape!",
                "You sing the Grape Anthem while harvesting.",
                "A vine tickles your nose. You sneeze but pick more grapes.",
                "A grape rolls down a hill and you chase it.",
                "A mischievous crow snatches a grape mid-air!",
                "You accidentally step on grapes and get colorful socks."
            ])
            self.grapes += gain
            self.text = (
                f"Day {self.day} - Vineyard\n"
                f"You pick {gain} grapes. {event}\n"
                f"Total grapes: {self.grapes}"
            )
            self.choices = [
                ("Keep Picking", "vineyard", True),
                ("Go to Market", "market", True),
                ("Explore Woods", "woods", True),
                ("Take a Nap", "nap", True)
            ]

        # --- MARKET ---
        elif self.state == "market":
            suspicious = random.choice([
                "A hooded man offers 10 grapes for a 'mystery potion'.",
                "A child offers you a magic grape in exchange for a secret.",
                "A merchant sells 'grape insurance' for your basket.",
                "Someone whispers: 'Don’t eat that purple grape!'",
                "A shady trader asks if you want 'enchanted grape juice'."
            ])
            self.text = f"Day {self.day} - Market\n{suspicious}"
            self.choices = [
                ("Trade 5 Grapes", "trade", False),  # dialogue, no day increment
                ("Eat Free Samples", "samples", False),
                ("Return to Vineyard", "vineyard", True),
                ("Visit Town", "town", True)
            ]

        # --- TRADE ---
        elif self.state == "trade":
            if self.grapes >= 5:
                self.grapes -= 5
                reward = random.choice([
                    "a shiny amulet", 
                    "a cursed grape", 
                    "a small pouch of grapes", 
                    "a map to a hidden vineyard", 
                    "a sparkling grape necklace"
                ])
                if reward in ["a small pouch of grapes", "a map to a hidden vineyard"]:
                    self.grapes += 3
                self.text = f"You trade 5 grapes and receive {reward}.\nTotal grapes: {self.grapes}"
            else:
                self.text = "Not enough grapes! The merchant frowns."
            self.choices = [
                ("Ask more questions", "trade_dialogue", False),
                ("Return to Market", "market", False),
                ("Return to Vineyard", "vineyard", True),
                ("Visit Town", "town", True)
            ]

        # --- TRADE DIALOGUE ---
        elif self.state == "trade_dialogue":
            self.text = random.choice([
                "Trader whispers: 'The secret grape is in the forest.'",
                "Trader winks and disappears into the crowd.",
                "You hear gossip about a haunted orchard nearby."
            ])
            self.choices = [
                ("Return to Market", "market", False),
                ("Return to Vineyard", "vineyard", True),
                ("Explore Woods", "woods", True),
                ("Take a Nap", "nap", True)
            ]

        # --- SAMPLES ---
        elif self.state == "samples":
            outcome = random.choice(["gain", "lose", "chaos"])
            if outcome == "gain":
                self.grapes += 3
                result = "You eat free samples and feel energized! +3 grapes."
            elif outcome == "lose":
                self.grapes = max(0, self.grapes - 2)
                result = "Samples were rotten! You drop 2 grapes."
            else:
                self.grapes += 1
                result = "Samples whisper secrets to you. +1 grape gained."
            self.text = f"{result}\nTotal grapes: {self.grapes}"
            self.choices = [
                ("Return to Market", "market", False),
                ("Return to Vineyard", "vineyard", True),
                ("Explore Woods", "woods", True),
                ("Take a Nap", "nap", True)
            ]

        # --- WOODS ---
        elif self.state == "woods":
            event = random.choice([
                "You find wild grapes +4 grapes.",
                "Raccoons chase you! Lose 2 grapes.",
                "A mystical bush grants +2 grapes.",
                "A rabbit offers you a secret grape stash.",
                "A strange fog confuses you. Lose 1 grape.",
                "A hidden vine gives you +5 grapes."
            ])
            if "+" in event:
                added = int(event.split("+")[1].split()[0])
                self.grapes += added
            elif "Lose" in event:
                lost = int(event.split()[2])
                self.grapes = max(0, self.grapes - lost)
            self.text = f"Day {self.day} - Woods\n{event}\nTotal grapes: {self.grapes}"
            self.choices = [
                ("Return to Vineyard", "vineyard", True),
                ("Go to Market", "market", True),
                ("Take a Nap", "nap", True),
                ("Explore Deeper", "deep_woods", True)
            ]

        # --- DEEP WOODS ---
        elif self.state == "deep_woods":
            self.text = (
                "A strange vine altar appears.\n"
                "Inscription: 'Offer 5 grapes to the Harvest Spirit.'"
            )
            self.choices = [
                ("Offer 5 Grapes", "offer", False),
                ("Run Away", "woods", True),
                ("Take a Nap", "nap", True),
                ("Return to Vineyard", "vineyard", True)
            ]

        # --- OFFER ---
        elif self.state == "offer":
            if self.grapes >= 5:
                self.grapes -= 5
                self.grapes += 8
                self.text = "The spirit blesses you! +8 grapes gained."
            else:
                self.text = "You don't have enough grapes! The vines frown."
            self.choices = [
                ("Return to Vineyard", "vineyard", True),
                ("Go to Market", "market", True),
                ("Explore Woods", "woods", True),
                ("Take a Nap", "nap", True)
            ]

        # --- NAP ---
        elif self.state == "nap":
            self.text = "You nap under a grape tree. Refreshed!"
            self.choices = [
                ("Return to Vineyard", "vineyard", True),
                ("Visit Market", "market", True),
                ("Explore Woods", "woods", True),
                ("Go to Town", "town", True)
            ]

        # --- TOWN ---
        elif self.state == "town":
            self.text = "Town is bustling! Buy snacks, dance, or eavesdrop on grape gossip."
            self.choices = [
                ("Buy Snacks (+2 Grapes)", "snack", False),
                ("Dance in Square", "dance", False),
                ("Return to Vineyard", "vineyard", True),
                ("Take a Nap", "nap", True)
            ]

        # --- SNACK ---
        elif self.state == "snack":
            self.grapes += 2
            self.text = "Grape chips found! +2 grapes."
            self.choices = [
                ("Return to Vineyard", "vineyard", True),
                ("Go to Market", "market", True),
                ("Explore Woods", "woods", True),
                ("Take a Nap", "nap", True)
            ]

        # --- DANCE ---
        elif self.state == "dance":
            self.grapes += 1
            self.text = "You dance with grapes! +1 grape magically appears."
            self.choices = [
                ("Return to Vineyard", "vineyard", True),
                ("Visit Town", "town", True),
                ("Go to Market", "market", True),
                ("Take a Nap", "nap", True)
            ]

        # --- WIN ---
        elif self.state == "win":
            self.text = f"Victory! {self.grapes} grapes collected by Day 7!\nCelebrate your grape glory!"
            self.choices = [
                ("Play Again", "restart", False),
                ("Cry of Joy", "cry", False),
                ("Celebrate in Town", "town", True),
                ("Dance with Grapes", "dance", True)
            ]

        # --- LOSE ---
        elif self.state == "lose":
            self.text = f"Too bad! Only {self.grapes} grapes collected by Day 7.\nThe harvest ends."
            self.choices = [
                ("Restart Game", "restart", False),
                ("Cry Sadly", "cry", False),
                ("Visit Market Anyway", "market", True),
                ("Take a Nap", "nap", True)
            ]

        # --- CRY ---
        elif self.state == "cry":
            lost = random.randint(1, 3)
            self.grapes = max(0, self.grapes - lost)
            self.text = f"You cry dramatically. {lost} grapes lost in tears!"
            self.choices = [
                ("Return to Vineyard", "vineyard", True),
                ("Visit Town", "town", True),
                ("Take a Nap", "nap", True),
                ("Restart Game", "restart", False)
            ]

        # --- RESTART ---
        elif self.state == "restart":
            self.reset_game()
            return  # Skip incrementing the day

        # Increment day only if this action consumes a day
        if increment_day:
            self.day += 1

    def choose(self, new_state, increment_day=True):
        """Advance state. increment_day controls if day increases."""
        self.state = new_state
        self.get_scene(increment_day=increment_day)