
from collections import namedtuple
import random
import sys

Eventtuple = namedtuple('Eventtuple', ['EventList', 'AssociatedPointList'])

def VineyardEvents(grapes):
    VineyardEvent = Eventtuple([
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
        ],
        # Example fixed weights: balanced for +/- events, total length = 60 (same as events)
        [-2, +5, +3, +2, +1, -2, -3, 0, +6, -2, -4, +10, -1, 0, 0,
        -3, 0, +2, +5, -1, -2, -2, +1, 0, -1, +2, -3, -2, 0, +1,
        -1, +1, -2, +3, 0, -1, -3, +2, -2, 0, +1, -1, +2, +3, -1,
        0, +2, -2, 0, -1, +1, +3, -1, 0, +2, +3, -1, 0, +2, -2])
    for i in range(5):
        x = random.randint(0, len(VineyardEvent.EventList)-1)
        print(VineyardEvent.EventList[x])
        print(f'Result of this event: {VineyardEvent.AssociatedPointList[x]}')
        grapes = max(0, grapes + VineyardEvent.AssociatedPointList[x])
        print(f'Current grape total: {grapes}\n')
    
    return grapes

def MarketEvents():
    MarketEvent = Eventtuple()
def TownEvents():
    print("town")
def BarEvents():
    print("bar")
def MountainEvents(grapes):
    print("\n⛰️ You embark on a daring mountain adventure!")
    print("Your goal: survive the journey, find treasure, and maybe bring back grapes.\n")

    # --- First Fork ---
    print("You reach a fork in the trail:")
    choice1 = input("Go LEFT into the dark forest or RIGHT towards the icy cliffs? (left/right): ").strip().lower()
    while choice1 not in ["left", "right"]:
        choice1 = input("Invalid choice. Go LEFT or RIGHT? ").strip().lower()

    if choice1 == "left":
        print("\nYou venture into the dark forest. Shadows loom between the trees...")
        event = random.choice(["wolf pack", "lost path", "hidden glade", "mysterious hermit"])
        if event == "wolf pack":
            print("A pack of wolves surrounds you!")
            outcome = random.choices(["escape", "death"], weights=[60, 40])[0]
            if outcome == "death":
                print("😭 The wolves overwhelm you. Your adventure ends here.")
                sys.exit("GAME OVER")
            else:
                lost = min(grapes, random.randint(2, 6))
                grapes -= lost
                print(f"You escape, losing {lost} grapes. Grapes remaining: {grapes}")
        elif event == "lost path":
            print("You wander for hours and find nothing. Luckily, no harm done.")
        elif event == "hidden glade":
            gain = random.randint(5, 15)
            grapes += gain
            print(f"You discover a hidden glade full of grapes! +{gain} grapes. Total grapes: {grapes}")
        else:  # mysterious hermit
            print("A mysterious hermit offers you advice and a small bag of grapes.")
            gain = random.randint(3, 10)
            grapes += gain
            print(f"+{gain} grapes. Total grapes: {grapes}")
    else:  # cliffs
        print("\nYou brave the icy cliffs. The wind bites harshly...")
        event = random.choice(["slippery rocks", "avalanche", "hidden cave", "eagle attack"])
        if event == "slippery rocks":
            lost = min(grapes, random.randint(1, 4))
            grapes -= lost
            print(f"You slip but survive, losing {lost} grapes. Grapes remaining: {grapes}")
        elif event == "avalanche":
            outcome = random.choices(["survive", "death"], weights=[50, 50])[0]
            if outcome == "death":
                print("💀 An avalanche crushes you! You perish on the mountain.")
                sys.exit("GAME OVER")
            else:
                gain = 5
                grapes += gain
                print(f"You survive the avalanche and find {gain} grapes under the snow. Total grapes: {grapes}")
        elif event == "hidden cave":
            gain = 20
            grapes += gain
            print(f"You discover a hidden cave full of golden grapes! +{gain} grapes. Total grapes: {grapes}")
        else:  # eagle attack
            outcome = random.choices(["escape", "death"], weights=[70, 30])[0]
            if outcome == "death":
                print("🦅 An eagle snatches you! You fall off the cliff. Game over.")
                sys.exit("GAME OVER")
            else:
                lost = min(grapes, random.randint(1, 3))
                grapes -= lost
                print(f"You narrowly escape the eagle, losing {lost} grapes. Grapes remaining: {grapes}")

    # --- River Crossing ---
    print("\nAfter hours of trekking, a raging river blocks your path.")
    choice2 = input("Do you SWIM across or BUILD a raft? (swim/raft): ").strip().lower()
    while choice2 not in ["swim", "raft"]:
        choice2 = input("Invalid choice. Swim or build a raft? ").strip().lower()

    if choice2 == "swim":
        outcome = random.choices(["success", "death"], weights=[30, 70])[0]
        if outcome == "death":
            print("😭 The current sweeps you away. Adventure ends tragically.")
            sys.exit("GAME OVER")
        else:
            print("💪 You swim across successfully. Your grapes are wet but safe!")
    else:  # raft
        outcome = random.choices(["success", "capsize"], weights=[60, 40])[0]
        if outcome == "capsize":
            lost = min(grapes, random.randint(3, 8))
            grapes -= lost
            print(f"Your raft capsizes! You lose {lost} grapes but survive. Grapes remaining: {grapes}")
        else:
            print("Your raft holds! You cross safely with all grapes intact.")

    # --- Mountain Pass ---
    print("\nYou reach a treacherous mountain pass.")
    event = random.choice(["rockslide", "snowstorm", "friendly trader", "bandit ambush"])
    if event == "rockslide":
        outcome = random.choices(["survive", "death"], weights=[65, 35])[0]
        if outcome == "death":
            print("💀 Rocks fall from above and crush you. Your adventure ends here.")
            sys.exit("GAME OVER")
        else:
            lost = min(grapes, random.randint(2, 5))
            grapes -= lost
            print(f"You survive the rockslide, losing {lost} grapes. Grapes remaining: {grapes}")
    elif event == "snowstorm":
        lost = min(grapes, random.randint(1, 3))
        grapes -= lost
        print(f"A snowstorm slows you down. You lose {lost} grapes to frostbite. Grapes remaining: {grapes}")
    elif event == "friendly trader":
        gain = random.randint(5, 15)
        grapes += gain
        print(f"A friendly trader shares some grapes! +{gain} grapes. Total grapes: {grapes}")
    else:  # bandit ambush
        outcome = random.choices(["escape", "death"], weights=[60, 40])[0]
        if outcome == "death":
            print("🏹 Bandits overwhelm you and steal everything. You die.")
            sys.exit("GAME OVER")
        else:
            lost = min(grapes, random.randint(5, 10))
            grapes -= lost
            print(f"You escape the bandits but lose {lost} grapes. Grapes remaining: {grapes}")

    # --- Treasure Hunt Fork ---
    print("\nAt the peak of the mountain, you spot two paths: a hidden cave or a sparkling waterfall.")
    choice3 = input("Do you explore the CAVE or go to the WATERFALL? (cave/waterfall): ").strip().lower()
    while choice3 not in ["cave", "waterfall"]:
        choice3 = input("Invalid choice. Cave or Waterfall? ").strip().lower()

    if choice3 == "cave":
        event = random.choice(["treasure chest", "trap", "giant bat"])
        if event == "treasure chest":
            gain = 30
            grapes += gain
            print(f"You find a hidden treasure chest filled with golden grapes! +{gain} grapes. Total grapes: {grapes}")
        elif event == "trap":
            print("😱 You trigger a trap and fall into a pit. You die.")
            sys.exit("GAME OVER")
        else:  # giant bat
            outcome = random.choices(["escape", "death"], weights=[70, 30])[0]
            if outcome == "death":
                print("🦇 A giant bat attacks! You perish in the darkness.")
                sys.exit("GAME OVER")
            else:
                lost = min(grapes, random.randint(3, 7))
                grapes -= lost
                print(f"You escape the bat but lose {lost} grapes. Grapes remaining: {grapes}")
    else:  # waterfall
        event = random.choice(["slip on rocks", "hidden grotto", "rainbow treasure"])
        if event == "slip on rocks":
            lost = min(grapes, random.randint(2, 5))
            grapes -= lost
            print(f"You slip near the waterfall, losing {lost} grapes. Grapes remaining: {grapes}")
        elif event == "hidden grotto":
            gain = random.randint(10, 20)
            grapes += gain
            print(f"You discover a hidden grotto full of grapes! +{gain} grapes. Total grapes: {grapes}")
        else:  # rainbow treasure
            gain = 25
            grapes += gain
            print(f"A magical rainbow reveals a stash of golden grapes! +{gain} grapes. Total grapes: {grapes}")

    # --- Adventure Conclusion ---
    print("\n🎉 You descend the mountain and return home safely!")
    return grapes