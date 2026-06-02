import pygame
import random
import sys

pygame.init()

# Screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Grape Picking Adventure")
clock = pygame.time.Clock()
FPS = 60
font = pygame.font.SysFont("Arial", 24)

# --- Colors ---
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

# --- Placeholder Assets ---
def create_surface(color, size=(50,50), circle=False):
    surf = pygame.Surface(size, pygame.SRCALPHA)
    surf.fill((0,0,0,0))
    if circle:
        pygame.draw.ellipse(surf, color, (0,0,size[0],size[1]))
    else:
        surf.fill(color)
    return surf

player_img = create_surface((0,128,255), (50,50))
grape_img = create_surface((128,0,128), (32,32), circle=True)
basket_img = create_surface((139,69,19), (60,60))
rival_img = create_surface((255,0,0), (50,50))
bird_img = create_surface((255,255,0), (50,50))
mentor_img = create_surface((0,255,0), (50,50))
background_img = create_surface((34,139,34), (WIDTH,HEIGHT))

# --- Game Variables ---
player_pos = [100, HEIGHT-150]
player_speed = 5
basket_capacity = 10
basket_count = 0
score = 0
story_day = 1
dialogue_active = False
current_dialogue = ""
dialogue_queue = []

# --- Grapes ---
num_grapes = 15
grapes = [[random.randint(150, WIDTH-50), random.randint(150, HEIGHT-150), True] for _ in range(num_grapes)]

# --- NPCs ---
class NPC:
    def __init__(self, name, pos, img, dialogues):
        self.name = name
        self.pos = pos
        self.img = img
        self.dialogues = dialogues  # dict day → text

    def get_dialogue(self, day):
        return self.dialogues.get(day, "")

mentor = NPC("Mentor", [WIDTH//2, HEIGHT-200], mentor_img, {
    1: "Welcome to the vineyard! Pick some grapes to fill your basket.",
    2: "Great job yesterday! Try to fill your basket completely today.",
    3: "Watch out for the birds! They love ripe grapes."
})

rival = NPC("Rival", [WIDTH-150, HEIGHT-150], rival_img, {
    1: "Ha! Let's see if you can keep up with me!",
    2: "Not bad, but can you beat my score today?",
    3: "You're getting good, but I won't lose!"
})

# --- Bird NPC ---
bird_pos = [random.randint(50, WIDTH-50), random.randint(50, HEIGHT-200)]
bird_direction = 1

# --- Helper Functions ---
def check_collision(pos1, size1, pos2, size2):
    rect1 = pygame.Rect(pos1[0], pos1[1], size1[0], size1[1])
    rect2 = pygame.Rect(pos2[0], pos2[1], size2[0], size2[1])
    return rect1.colliderect(rect2)

def start_dialogue(npc):
    global dialogue_active, dialogue_queue
    dialogue_active = True
    dialogue_queue = [npc.get_dialogue(story_day)]

def draw_dialogue_box():
    if dialogue_active and dialogue_queue:
        pygame.draw.rect(screen, BLACK, (50, HEIGHT-150, WIDTH-100, 100))
        pygame.draw.rect(screen, WHITE, (55, HEIGHT-145, WIDTH-110, 90))
        text_surface = font.render(dialogue_queue[0], True, BLACK)
        screen.blit(text_surface, (60, HEIGHT-120))

# --- Main Game Loop ---
running = True
while running:
    clock.tick(FPS)
    screen.blit(background_img, (0,0))

    # --- Event Handling ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if dialogue_active and event.key == pygame.K_SPACE:
                dialogue_queue.pop(0)
                if not dialogue_queue:
                    dialogue_active = False

    keys = pygame.key.get_pressed()
    if not dialogue_active:  # Disable movement during dialogue
        if keys[pygame.K_LEFT]: player_pos[0] -= player_speed
        if keys[pygame.K_RIGHT]: player_pos[0] += player_speed
        if keys[pygame.K_UP]: player_pos[1] -= player_speed
        if keys[pygame.K_DOWN]: player_pos[1] += player_speed

    player_rect = pygame.Rect(player_pos[0], player_pos[1], 50, 50)

    # --- Interactions with NPCs ---
    if check_collision(player_pos, (50,50), mentor.pos, (50,50)):
        if not dialogue_active:
            start_dialogue(mentor)
    if check_collision(player_pos, (50,50), rival.pos, (50,50)):
        if not dialogue_active:
            start_dialogue(rival)

    # --- Player grape picking ---
    for grape in grapes:
        if grape[2] and check_collision(player_pos, (50,50), grape[:2], (32,32)):
            if basket_count < basket_capacity:
                basket_count += 1
                score += 10
                grape[2] = False

    # --- Rival AI ---
    target_grape = next((g for g in grapes if g[2]), None)
    if target_grape:
        rival_speed = 3
        if rival.pos[0] < target_grape[0]: rival.pos[0] += rival_speed
        if rival.pos[0] > target_grape[0]: rival.pos[0] -= rival_speed
        if rival.pos[1] < target_grape[1]: rival.pos[1] += rival_speed
        if rival.pos[1] > target_grape[1]: rival.pos[1] -= rival_speed
        if check_collision(rival.pos, (50,50), target_grape[:2], (32,32)):
            target_grape[2] = False
            score -= 5

    # --- Bird movement ---
    bird_pos[0] += bird_direction * 2
    if bird_pos[0] > WIDTH-50 or bird_pos[0] < 0:
        bird_direction *= -1

    # --- Draw Grapes ---
    for grape in grapes:
        if grape[2]:
            screen.blit(grape_img, (grape[0], grape[1]))

    # --- Draw NPCs ---
    screen.blit(mentor.img, mentor.pos)
    screen.blit(rival.img, rival.pos)
    screen.blit(bird_img, bird_pos)
    screen.blit(player_img, player_pos)

    # --- Draw UI ---
    screen.blit(basket_img, (10,10))
    basket_text = font.render(f"{basket_count}/{basket_capacity}", True, WHITE)
    screen.blit(basket_text, (70,20))
    score_text = font.render(f"Score: {score}", True, YELLOW)
    screen.blit(score_text, (WIDTH-150,10))

    # --- Draw Dialogue ---
    draw_dialogue_box()

    pygame.display.flip()

pygame.quit()
sys.exit()