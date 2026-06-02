import tkinter as tk
import random

WIDTH = 800
HEIGHT = 600
BASKET_WIDTH = 120
BASKET_HEIGHT = 25
GRAPE_SIZE = 24
START_SPEED = 4
SPAWN_RATE = 1200
GAME_TIME = 60


class Grape:
    def __init__(self, canvas):
        self.canvas = canvas
        self.x = random.randint(20, WIDTH - 20)
        self.y = -20
        self.speed = random.randint(START_SPEED, START_SPEED + 3)
        self.id = canvas.create_oval(
            self.x,
            self.y,
            self.x + GRAPE_SIZE,
            self.y + GRAPE_SIZE,
            fill="purple",
            outline="dark violet",
            width=2,
        )

    def move(self):
        self.canvas.move(self.id, 0, self.speed)
        self.y += self.speed

    def get_position(self):
        return self.canvas.coords(self.id)

    def delete(self):
        self.canvas.delete(self.id)


class GoldenGrape:
    def __init__(self, canvas):
        self.canvas = canvas
        self.x = random.randint(20, WIDTH - 20)
        self.y = -20
        self.speed = random.randint(6, 9)
        self.id = canvas.create_oval(
            self.x,
            self.y,
            self.x + GRAPE_SIZE,
            self.y + GRAPE_SIZE,
            fill="gold",
            outline="orange",
            width=3,
        )

    def move(self):
        self.canvas.move(self.id, 0, self.speed)
        self.y += self.speed

    def get_position(self):
        return self.canvas.coords(self.id)

    def delete(self):
        self.canvas.delete(self.id)


class Basket:
    def __init__(self, canvas):
        self.canvas = canvas
        self.x = WIDTH // 2
        self.y = HEIGHT - 60
        self.id = canvas.create_rectangle(
            self.x,
            self.y,
            self.x + BASKET_WIDTH,
            self.y + BASKET_HEIGHT,
            fill="saddlebrown",
            outline="black",
            width=3,
        )

    def move_left(self, event=None):
        pos = self.canvas.coords(self.id)
        if pos[0] > 0:
            self.canvas.move(self.id, -30, 0)

    def move_right(self, event=None):
        pos = self.canvas.coords(self.id)
        if pos[2] < WIDTH:
            self.canvas.move(self.id, 30, 0)

    def get_position(self):
        return self.canvas.coords(self.id)


class GrapePickingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Grape Picking Adventure")
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="light sky blue")
        self.canvas.pack()

        self.canvas.create_rectangle(0, HEIGHT - 40, WIDTH, HEIGHT, fill="forest green")

        self.basket = Basket(self.canvas)
        self.grapes = []

        self.score = 0
        self.missed = 0
        self.time_left = GAME_TIME
        self.game_running = True

        self.score_text = self.canvas.create_text(
            90,
            30,
            text=f"Score: {self.score}",
            font=("Arial", 20, "bold"),
            fill="black",
        )

        self.missed_text = self.canvas.create_text(
            110,
            60,
            text=f"Missed: {self.missed}",
            font=("Arial", 16),
            fill="dark red",
        )

        self.timer_text = self.canvas.create_text(
            WIDTH - 100,
            30,
            text=f"Time: {self.time_left}",
            font=("Arial", 20, "bold"),
            fill="black",
        )

        self.instructions = self.canvas.create_text(
            WIDTH // 2,
            30,
            text="Use Left and Right Arrow Keys to Catch Grapes!",
            font=("Arial", 16, "bold"),
            fill="navy",
        )

        root.bind("<Left>", self.basket.move_left)
        root.bind("<Right>", self.basket.move_right)
        root.bind("a", self.basket.move_left)
        root.bind("d", self.basket.move_right)

        self.spawn_grape()
        self.update_game()
        self.countdown()

    def spawn_grape(self):
        if not self.game_running:
            return

        chance = random.randint(1, 10)
        if chance == 10:
            self.grapes.append(GoldenGrape(self.canvas))
        else:
            self.grapes.append(Grape(self.canvas))

        self.root.after(SPAWN_RATE, self.spawn_grape)

    def update_game(self):
        if not self.game_running:
            return

        basket_pos = self.basket.get_position()

        for grape in self.grapes[:]:
            grape.move()
            grape_pos = grape.get_position()

            if self.check_collision(basket_pos, grape_pos):
                if isinstance(grape, GoldenGrape):
                    self.score += 5
                else:
                    self.score += 1

                self.canvas.itemconfig(self.score_text, text=f"Score: {self.score}")
                grape.delete()
                self.grapes.remove(grape)

            elif grape_pos[3] > HEIGHT:
                self.missed += 1
                self.canvas.itemconfig(self.missed_text, text=f"Missed: {self.missed}")
                grape.delete()
                self.grapes.remove(grape)

        self.root.after(20, self.update_game)

    def check_collision(self, basket, grape):
        return (
            grape[2] > basket[0]
            and grape[0] < basket[2]
            and grape[3] > basket[1]
            and grape[1] < basket[3]
        )

    def countdown(self):
        if not self.game_running:
            return

        self.time_left -= 1
        self.canvas.itemconfig(self.timer_text, text=f"Time: {self.time_left}")

        if self.time_left <= 0:
            self.end_game()
        else:
            self.root.after(1000, self.countdown)

    def end_game(self):
        self.game_running = False

        self.canvas.create_rectangle(180, 180, 620, 420, fill="white", outline="black", width=4)

        self.canvas.create_text(
            WIDTH // 2,
            240,
            text="Harvest Complete!",
            font=("Arial", 30, "bold"),
            fill="purple",
        )

        self.canvas.create_text(
            WIDTH // 2,
            300,
            text=f"Final Score: {self.score}",
            font=("Arial", 24),
            fill="black",
        )

        self.canvas.create_text(
            WIDTH // 2,
            340,
            text=f"Grapes Missed: {self.missed}",
            font=("Arial", 20),
            fill="dark red",
        )

        if self.score >= 40:
            message = "Amazing Vineyard Skills!"
        elif self.score >= 20:
            message = "Great Job Picking Grapes!"
        else:
            message = "Keep Practicing Your Harvest!"

        self.canvas.create_text(
            WIDTH // 2,
            380,
            text=message,
            font=("Arial", 18, "italic"),
            fill="forest green",
        )


if __name__ == "__main__":
    root = tk.Tk()
    game = GrapePickingGame(root)
    root.mainloop()
