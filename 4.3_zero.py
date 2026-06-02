import random
import time


# Game settings
VINEYARD_SIZE = 5  # 5x5 grid
BASKET_CAPACITY = 10
TIME_LIMIT = 30  # seconds


# Initialize vineyard with random number of grapes per cell
vineyard = [[random.randint(0, 3) for _ in range(VINEYARD_SIZE)] for _ in range(VINEYARD_SIZE)]


# Player starting position
player_pos = [0, 0]
basket = 0
start_time = time.time()


def print_vineyard():
    for i in range(VINEYARD_SIZE):
        row = ""
        for j in range(VINEYARD_SIZE):
            if player_pos == [i, j]:
                row += " P "
            else:
                row += f" {vineyard[i][j]} "
        print(row)
    print(f"Basket: {basket}/{BASKET_CAPACITY}")
    print(f"Time left: {max(0, int(TIME_LIMIT - (time.time() - start_time)))}s\n")


def move_player(direction):
    if direction == "w" and player_pos[0] > 0:
        player_pos[0] -= 1
    elif direction == "s" and player_pos[0] < VINEYARD_SIZE - 1:
        player_pos[0] += 1
    elif direction == "a" and player_pos[1] > 0:
        player_pos[1] -= 1
    elif direction == "d" and player_pos[1] < VINEYARD_SIZE - 1:
        player_pos[1] += 1
    else:
        print("Can't move in that direction!")


def pick_grapes():
    global basket
    x, y = player_pos
    if vineyard[x][y] > 0:
        can_pick = min(vineyard[x][y], BASKET_CAPACITY - basket)
        basket += can_pick
        vineyard[x][y] -= can_pick
        print(f"You picked {can_pick} grapes!")
    else:
        print("No grapes here!")


# Game loop
print("Welcome to the Grape Picking Game!")
print("Move with W/A/S/D, pick grapes with 'p'. Fill your basket before time runs out!\n")


while time.time() - start_time < TIME_LIMIT and basket < BASKET_CAPACITY:
    print_vineyard()
    action = input("Action (w/a/s/d/p): ").lower()
    if action in ["w", "a", "s", "d"]:
        move_player(action)
    elif action == "p":
        pick_grapes()
    else:
        print("Invalid action!")


# Game over
print("\nGame Over!")
print(f"You collected {basket} grapes.")
if basket >= BASKET_CAPACITY:
    print("Congratulations! Your basket is full!")
else:
    print("Better luck next time!")
