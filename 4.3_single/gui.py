# gui.py
import pygame
from config import *

pygame.font.init()
font = pygame.font.SysFont(FONT_NAME, FONT_SIZE)

class Button:
    def __init__(self, text, x, y, w, h, callback):
        self.text = text
        self.rect = pygame.Rect(x, y, w, h)
        self.callback = callback
        self.color = GRAY
        self.hover_color = LIGHT_GRAY
        self.text_surf = font.render(self.text, True, WHITE)
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)

    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()
        color = self.hover_color if self.rect.collidepoint(mouse_pos) else self.color
        pygame.draw.rect(surface, color, self.rect, border_radius=10)
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)
        surface.blit(self.text_surf, self.text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.callback()

def draw_text(surface, text, margin):
    """Draw wrapped story text without overlapping buttons"""
    # Reserve bottom space for buttons
    max_height = HEIGHT - 200
    lines = []
    for paragraph in text.split("\n"):
        words = paragraph.split(" ")
        line = ""
        for word in words:
            test_line = line + word + " "
            if font.size(test_line)[0] > WIDTH - 2 * margin:
                lines.append(line)
                line = word + " "
            else:
                line = test_line
        lines.append(line)
        lines.append("")  # space between paragraphs

    y = 100
    for line in lines:
        if y > max_height:
            break  # prevent overlapping buttons
        rendered = font.render(line.strip(), True, BLACK)
        surface.blit(rendered, (margin, y))
        y += FONT_SIZE + 5

def draw_status_bar(surface, day, grapes):
    """Draw status bar at top"""
    bar_text = f"Day: {day}   |   Grapes: {grapes}"
    bar_surface = font.render(bar_text, True, WHITE)
    pygame.draw.rect(surface, PURPLE, (0, 0, WIDTH, 40))
    surface.blit(bar_surface, (WIDTH // 2 - bar_surface.get_width() // 2, 8))