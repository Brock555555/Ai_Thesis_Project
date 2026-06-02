# main.py
import pygame
from gui import Button, draw_text, draw_status_bar
from config import *
from story import Story

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Grape Odyssey")

clock = pygame.time.Clock()
story = Story()
story.get_scene()
buttons = []

# ----------------------------
# Update Buttons
# ----------------------------
def update_buttons():
    global buttons
    buttons = []
    button_width = WIDTH * 0.6
    total_height = len(story.choices) * (BUTTON_HEIGHT + BUTTON_MARGIN)
    start_y = HEIGHT - total_height - 50

    for i, (label, next_state, increment_day) in enumerate(story.choices):
        x = (WIDTH - button_width) // 2
        y = start_y + i * (BUTTON_HEIGHT + BUTTON_MARGIN)
        # Pass increment_day to choose function
        btn = Button(
            label,
            x,
            y,
            button_width,
            BUTTON_HEIGHT,
            lambda s=next_state, d=increment_day: choose(s, d)
        )
        buttons.append(btn)

# ----------------------------
# Choose Function
# ----------------------------
def choose(state, increment_day=True):
    story.choose(state, increment_day)
    update_buttons()

update_buttons()

# ----------------------------
# Main Game Loop
# ----------------------------
running = True
while running:
    screen.fill(WHITE)
    # Draw grape/day status
    draw_status_bar(screen, story.day, story.grapes)
    # Draw main story text
    draw_text(screen, story.text, 60)

    # Draw all buttons
    for btn in buttons:
        btn.draw(screen)

    pygame.display.flip()

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        for btn in buttons:
            btn.handle_event(event)

    clock.tick(30)

pygame.quit()