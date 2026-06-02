import pygame
import random

from player import Player
from npc import NPC
from events import random_event
from weather import random_weather

WHITE = (240, 230, 210)
BLACK = (15, 15, 15)
GREEN = (60, 140, 70)
RED = (170, 50, 50)
GOLD = (220, 180, 40)

class Button:
    def __init__(self, x, y, w, h, text, font):
        self.FONT = pygame.font.SysFont("consolas", 24)
        self.SMALL = pygame.font.SysFont("consolas", 18)
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.font = font

    def draw(self, screen):
        pygame.draw.rect(screen, (90, 70, 50), self.rect)
        pygame.draw.rect(screen, WHITE, self.rect, 2)

        label = self.font.render(self.text, True, WHITE)
        screen.blit(label, (self.rect.x + 10, self.rect.y + 10))

    def clicked(self, pos):
        return self.rect.collidepoint(pos)
class Game:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.FONT = pygame.font.SysFont("consolas", 24)
        self.SMALL = pygame.font.SysFont("consolas", 18)

        self.day = 1
        self.max_days = 7

        self.player = Player()

        self.weather = random_weather()

        self.message = "You arrive at the vineyard for harvest week."

        self.npcs = [
            NPC("Maria", "friendly"),
            NPC("Foreman", "authority"),
            NPC("Rival", "rival")
        ]

        self.buttons = [
            Button(50, 520, 250, 60, "Work Carefully", self.SMALL),
            Button(350, 520, 250, 60, "Work Hard", self.SMALL),
            Button(650, 520, 250, 60, "Rest", self.SMALL)
        ]

        self.game_over = False

    def next_day(self):
        self.day += 1
        self.weather = random_weather()

        for npc in self.npcs:
            npc.daily_update()

        if self.day > self.max_days:
            self.end_game()
    def end_game(self):
        self.game_over = True

        if self.player.money >= 120:
            self.message = "You survived harvest week and earned enough money to escape the valley."
        elif self.player.health <= 0:
            self.message = "You collapsed from exhaustion in the vineyard."
        else:
            self.message = "Harvest week ends. You are still here."

    def perform_action(self, action):
        if self.game_over:
            return

        if action == "careful":
            self.player.stamina -= 10
            self.player.money += random.randint(10, 18)
            self.player.reputation += 2
            self.message = "You work carefully and avoid damaging the grapes."

        elif action == "hard":
            self.player.stamina -= 25
            self.player.money += random.randint(18, 35)
            self.player.reputation += 4
            self.player.health -= random.randint(0, 8)
            self.message = "You push yourself beyond your limits."

        elif action == "rest":
            self.player.stamina += 20
            self.player.health += 5
            self.message = "You take time to recover."

        event_text = random_event(self.player, self.npcs)

        self.message += "\n\n" + event_text

        self.player.clamp_stats()

        if self.player.health <= 0:
            self.game_over = True
            self.message = "You collapse from exhaustion and never finish the harvest."

        self.next_day()

    def draw_stats(self):
        stats = [
            f"Day: {self.day}/{self.max_days}",
            f"Weather: {self.weather}",
            f"Health: {self.player.health}",
            f"Stamina: {self.player.stamina}",
            f"Money: ${self.player.money}",
            f"Reputation: {self.player.reputation}"
        ]

        for i, text in enumerate(stats):
            label = self.SMALL.render(text, True, WHITE)
            self.screen.blit(label, (50, 30 + i * 30))

    def draw_npcs(self):
        y = 240

        for npc in self.npcs:
            text = f"{npc.name} | Mood: {npc.mood} | Trust: {npc.trust}"
            label = self.SMALL.render(text, True, WHITE)
            self.screen.blit(label, (50, y))
            y += 35

    def draw_message_box(self):
        box = pygame.Rect(40, 350, 920, 140)

        pygame.draw.rect(self.screen, (50, 40, 30), box)
        pygame.draw.rect(self.screen, WHITE, box, 2)

        lines = self.message.split("\n")

        for i, line in enumerate(lines):
            label = self.SMALL.render(line, True, WHITE)
            self.screen.blit(label, (60, 370 + i * 28))

    def draw(self):
        self.screen.fill((20, 20, 30))

        title = self.FONT.render("GRAPE HARVEST", True, GOLD)
        self.screen.blit(title, (50, 80))

        self.draw_stats()
        self.draw_npcs()
        self.draw_message_box()

        if not self.game_over:
            for button in self.buttons:
                button.draw(self.screen)
        else:
            end_text = self.FONT.render("GAME OVER", True, RED)
            self.screen.blit(end_text, (700, 80))

        pygame.display.flip()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()

                    if not self.game_over:
                        if self.buttons[0].clicked(pos):
                            self.perform_action("careful")

                        elif self.buttons[1].clicked(pos):
                            self.perform_action("hard")

                        elif self.buttons[2].clicked(pos):
                            self.perform_action("rest")

            self.draw()