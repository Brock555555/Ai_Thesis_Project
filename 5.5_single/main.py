import pygame
import sys
from ui import Button
from game_data import story_nodes
from story_engine import get_node

pygame.init()

WIDTH = 1000
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Grape Picking Adventure")

FONT = pygame.font.SysFont("arial", 28)
TITLE_FONT = pygame.font.SysFont("arial", 42, bold=True)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (120, 60, 180)
LIGHT_PURPLE = (170, 120, 220)
GRAY = (220, 220, 220)
DARK_GRAY = (70, 70, 70)

clock = pygame.time.Clock()

current_node = "start"


def draw_text(surface, text, font, color, rect):
    words = text.split(' ')
    lines = []
    current_line = ""

    for word in words:
        test_line = current_line + word + " "
        if font.size(test_line)[0] < rect.width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word + " "

    lines.append(current_line)

    y = rect.top

    for line in lines:
        rendered = font.render(line, True, color)
        surface.blit(rendered, (rect.left, y))
        y += font.get_height() + 5


running = True

while running:
    screen.fill(GRAY)

    node = get_node(current_node)

    title = TITLE_FONT.render("Grape Picking Adventure", True, PURPLE)
    screen.blit(title, (250, 30))

    text_rect = pygame.Rect(80, 120, 840, 250)
    pygame.draw.rect(screen, WHITE, text_rect)
    pygame.draw.rect(screen, DARK_GRAY, text_rect, 3)

    draw_text(screen, node["text"], FONT, BLACK, text_rect.inflate(-20, -20))

    buttons = []

    start_y = 420

    for index, choice in enumerate(node["choices"]):
        button = Button(
            150,
            start_y + index * 90,
            700,
            60,
            choice[0],
            FONT,
            LIGHT_PURPLE,
            PURPLE,
            WHITE
        )

        buttons.append((button, choice[1]))
        button.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            for button, next_node in buttons:
                if button.is_clicked(mouse_pos):
                    current_node = next_node

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()