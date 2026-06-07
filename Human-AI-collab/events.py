"""
Events Module: Grape Odyssey
Contains all the location-based narrative encounters, probability tables, and typing effects.
"""

from collections import namedtuple
import random
import sys
import time

# Create a structured data type to lock text strings and their point values together
Eventtuple = namedtuple('Eventtuple', ['EventList', 'AssociatedPointList'])

# WHY: By defining this massive block of text outside of the function, Python compiles 
# and stores these strings in memory exactly ONE time when the game boots up. If this was 
# inside the function, the CPU would waste time rebuilding this entire 60-item list from 
# scratch every single time the player picked Option 1.
VINEYARD_DATA = Eventtuple([
    "A squirrel makes aggressive eye contact and steals a grape. This is personal now.",
    "You find a tiny golden grape! It whispers, 'Invest wisely.'",
    "You sing the Grape Anthem. The vines harmonize. It gets weirdly emotional.",
    "A vine tickles your nose. You sneeze so hard three grapes achieve orbit.",
    "A grape rolls down a hill. You chase it. The grape wins.",
    "A mischievous crow snatches a grape mid-air and caws, 'Skill issue.'",
    "You step on grapes and invent modern art. Your socks are a masterpiece.",
    "A bee lands on your nose. You freeze. The bee judges you... then leaves.",
    "You harvest the juiciest bunch ever. Somewhere, a sommelier sheds a tear.",
    "A bird steals grapes and drops one just to flex.",
    "You slip in grape juice. The grapes are fine. Your dignity is not.",
    "You discover a large golden grape. It hums ominously. You pretend not to notice.",
    "A grape explodes dramatically for no reason. The others look nervous.",
    "You accidentally name one grape and now you can’t harvest it.",
    "The vineyard goes silent. Too silent. Even the grapes are watching.",
    "A rogue grape rolls off the table and starts a rebellion. You negotiate peace.",
    "A butterfly lands on your harvest basket. It seems disappointed in your life choices.",
    "You accidentally juggle grapes. One escapes and becomes a local legend.",
    "A grape develops sentience and gives you stock tips. You ignore it. Regret follows.",
    "The wind gusts. Grapes fly in slow motion. Dramatic music plays in your mind.",
    "A goat sneaks in and critiques your pruning technique. You take notes.",
    "You try to stomp grapes. They resist. It’s like wrestling tiny squishy ninjas.",
    "A mysterious fog rolls in. Suddenly, all grapes taste like blueberries. Nobody knows why.",
    "You find a grape wearing a tiny hat. It tips it politely before rolling away.",
    "A vine whispers secrets about the vineyard. Mostly about the squirrels.",
    "You sneeze and a grape becomes airborne. It performs an elegant somersault. Applause.",
    "A bat swoops in. It’s only interested in grapes. You silently question your life choices.",
    "A grape splits in half mid-air. Physics applauds. You cry.",
    "You hear ominous laughter from the barrels. The grapes are clearly plotting something.",
    "A vine grows a perfect grape-shaped emoji. You post it online. Instant fame.",
    "You attempt to taste-test all grapes at once. The grapes retaliate with sticky justice.",
    "A grape rolls off your hand and becomes a motivational speaker for lost fruits.",
    "You try to stomp grapes. One bounces back and hits your forehead. Respect earned.",
    "A snail starts a marathon across the vineyard. You cheer it on. It wins.",
    "A vine sprouts sunglasses. It looks cooler than you. You feel inadequate.",
    "You smell a grape. It smells exactly like regret. Weirdly accurate.",
    "A squirrel declares itself mayor of the vineyard. Campaign promises: nuts only.",
    "Grapes start forming a conga line. You are now their audience.",
    "A rogue vine entangles your boots. Fashion statement or mild hazard? You decide.",
    "You whisper to a grape. It whispers back. Mostly complaints about sunlight.",
    "A crow delivers a grape with a tiny note: 'Thanks for last Tuesday.'",
    "You trip over a vine and accidentally invent grape yoga. Everyone’s confused.",
    "A grape rolls into a puddle. It emerges wearing a tiny crown. Royalty confirmed.",
    "You try to taste a grape. It tastes like tiny fireworks. Your mouth applauds.",
    "A butterfly lands on your nose. You sneeze. It applauds politely.",
    "The wind rearranges grapes into your face on the ground. Portrait mode engaged.",
    "You find a grape wearing a mustache. It tips it like a true gentleman.",
    "A bat swoops down. It only wants one grape. You negotiate terms.",
    "You sing to the grapes. They respond with awkward silence. Emotional trauma ensues.",
    "A grape explodes in slow motion. Nearby grapes look shocked but supportive.",
    "You step on a grape. It bounces off like a tiny trampoline. Physics is weird.",
    "A mysterious fog covers the vineyard. Suddenly all grapes taste like bubblegum.",
    "You discover a secret grape society. Membership requires awkward small talk.",
    "A vine grows a tiny slide. Grapes use it constantly. You watch, mesmerized.",
    "You sneeze mid-harvest. One grape achieves orbit. NASA is impressed.",
    "A rainbow appears over the vineyard. Only one grape reflects it perfectly. Fame awaits.",
    "You accidentally name a grape. It now demands royalties.",
    "A rogue vine twirls around your ankle. Dance-off initiated.",
    "You try to juggle grapes. One escapes. It’s now a local legend.",
    "The sun glares at you. Grapes glare back. Tense standoff ensues.",
    "A mysterious grape rolls past you whispering, 'I’ve seen things.' You nod solemnly."
], [
    -2, 5, 3, 2, 1, -2, -3, 0, 6, -2, -4, 10, -1, 0, 0,
    -3, 0, 2, 5, -1, -2, -2, 1, 0, -1, 2, -3, -2, 0, 1,
    -1, 1, -2, 3, 0, -1, -3, 2, -2, 0, 1, -1, 2, 3, -1,
    0, 2, -2, 0, -1, 1, 3, -1, 0, 2, 3, -1, 0, 2, -2, 0
])


def type_print(*args, sep=' ', end='\n', delay=0.03):
    """
    Simulates a retro typewriter effect by printing characters one by one.
    
    Args:
        args: The text strings to print.
        sep: Character to place between multiple args (default: space).
        end: Character to append at the end of the line (default: newline).
        delay: Time in seconds to sleep between characters (default: 0.03).
    """
    text = sep.join(str(a) for a in args) + end
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()  # Forces the terminal to display the character immediately
        time.sleep(delay)   # Restored: The actual typing delay!


def VineyardEvents(grapes):
    """
    Generates 5 random narrative events from the vineyard data and modifies the player's grapes.
    
    Args:
        grapes (int): The player's current grape count.
        
    Returns:
        int: The modified grape count.
    """
    # Cache the upper boundary of the list to prevent recalculating it inside the loop
    limit = len(VINEYARD_DATA.EventList) - 1
    
    for _ in range(5):
        # Pick a random index corresponding to our global tuple data
        x = random.randint(0, limit)
        type_print(VINEYARD_DATA.EventList[x])
        type_print(f'Result of this event: {VINEYARD_DATA.AssociatedPointList[x]}')
        
        # Prevent grapes from dropping below 0 natively using max()
        grapes = max(0, grapes + VINEYARD_DATA.AssociatedPointList[x])
        type_print(f'Current grape total: {grapes}\n')
        
    return grapes

# Unimplemented placeholder functions to prevent crashes from the main loop dictionary mapping
def MarketEvents(grapes): pass
def TownEvents(grapes): pass
def BarEvents(grapes): pass


def MountainEvents(grapes):
    """
    A multi-stage, choose-your-own-adventure logic tree with branching probabilities.
    
    Args:
        grapes (int): The player's current grape count.
        
    Returns:
        int: The modified grape count (if the player survives).
    """
    type_print("\n⛰️ You embark on a daring mountain adventure!")
    type_print("Your goal: survive the journey, find treasure, and maybe bring back grapes.\n")

    # --- FIRST FORK ---
    type_print("You reach a fork in the trail:")
    
    # Input collection loop.
    # WHY: Placing .strip().lower() directly on the input immediately standardizes the data 
    # and prevents needing case checks (e.g., 'Left', 'LEFT', 'left') inside the conditionals.
    choice1 = input("Go LEFT into the dark forest or RIGHT towards the icy cliffs? (left/right): ").strip().lower()
    while choice1 not in ("left", "right"):
        choice1 = input("Invalid choice. Go LEFT or RIGHT? ").strip().lower()

    if choice1 == "left":
        type_print("\nYou venture into the dark forest. Shadows loom between the trees...")
        event = random.choice(["wolf pack", "lost path", "hidden glade", "mysterious hermit"])
        
        if event == "wolf pack":
            type_print("A pack of wolves surrounds you!")
            
            # Determine survival using weighted choices (60% escape, 40% death)
            if random.choices(["escape", "death"], weights=[60,40]) == "death":
                # sys.exit immediately halts the script. Used here as a hard 'Game Over' state.
                sys.exit("😭 The wolves overwhelm you. GAME OVER")
            else:
                # Calculate grape loss based on either a random amount OR the player's total
                # (whichever is lower) to prevent negative grape balances.
                lost = min(grapes, random.randint(2, 6))
                grapes -= lost
                type_print(f"You escape, losing {lost} grapes. Grapes remaining: {grapes}")
                
        elif event == "hidden glade":
            gain = random.randint(5, 15)
            grapes += gain
            type_print(f"You discover a hidden glade full of grapes! +{gain} grapes. Total: {grapes}")
            
        elif event == "mysterious hermit":
            gain = random.randint(3, 10)
            grapes += gain
            type_print(f"A mysterious hermit offers you advice. +{gain} grapes. Total: {grapes}")
            
    else: # Icy cliffs path
        type_print("\nYou brave the icy cliffs. The wind bites harshly...")
        event = random.choice(["slippery rocks", "avalanche", "hidden cave", "eagle attack"])
        
        if event == "slippery rocks":
            lost = min(grapes, random.randint(1, 4))
            grapes -= lost
            type_print(f"You slip but survive, losing {lost} grapes. Remaining: {grapes}")
            
        elif event == "avalanche":
            # 50/50 survival probability
            if random.choices(["survive", "death"], weights=[50,50]) == "death":
                sys.exit("💀 An avalanche crushes you! GAME OVER")
            else:
                grapes += 5
                type_print(f"You find 5 grapes under the snow. Total grapes: {grapes}")
                
        elif event == "hidden cave":
            grapes += 20
            type_print(f"You discover a hidden cave full of golden grapes! +20 grapes. Total: {grapes}")

    # --- RIVER CROSSING ---
    type_print("\nAfter hours of trekking, a raging river blocks your path.")
    choice2 = input("Do you SWIM across or BUILD a raft? (swim/raft): ").strip().lower()
    while choice2 not in ("swim", "raft"):
        choice2 = input("Invalid choice. Swim or build a raft? ").strip().lower()

    if choice2 == "swim":
        # Swimming is highly dangerous: 70% death rate
        if random.choices(["success", "death"], weights=[30,70]) == "death":
            sys.exit("😭 The current sweeps you away. GAME OVER")
        else:
            type_print("💪 You swim across successfully. Your grapes are wet but safe!")
    else:
        # Rafting is safer: 40% capsize rate, but no death penalty
        if random.choices(["success", "capsize"], weights=[60,40]) == "capsize":
            lost = min(grapes, random.randint(3, 8))
            grapes -= lost
            type_print(f"Your raft capsizes! You lose {lost} grapes. Remaining: {grapes}")
        else:
            type_print("Your raft holds! You cross safely with all grapes intact.")

    return grapes