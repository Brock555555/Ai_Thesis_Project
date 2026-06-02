import events
import sys, time, builtins
import random


grapes = 0
day = 1

original_print = builtins.print
def slow_print(*args, sep=' ', end='\n', delay=0.03):
    text = sep.join(str(a) for a in args) + end
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)

builtins.print = slow_print


class options:
    def __init__(self, array):
        self.array = array

    def displayoptions(self):
        print(f'Please pick an option from 1 to {len(self.array)}')
        for i in self.array:
            print(i)
        print()

    def length(self):
        return len(self.array)
    
    def append(self, value):
        self.array.append(f'({self.length() + 1}) {value}')


actions = {
    1: events.VineyardEvents,
    2: events.MarketEvents,
    3: events.TownEvents,
    4: events.BarEvents,
    5: events.MountainEvents
}

def selectionloop(array):
    array.displayoptions()

    while True:
        x = input("Your selection: ")
        try:
            x = int(x)
            if(x > Array.length()):
                print("Invalid selection")
                continue
            return x
        except:
            print("Invalid selection")

def gambling():
    global grapes
    print("💰 Welcome to the Vineyard Casino! Time to gamble your grapes.")
    
    while grapes > 1:  # keep gambling as long as they have grapes
        print(f"\nYou currently have {grapes} grapes.")
        
        # Ask if they want to continue
        cont = input("Do you want to gamble? (yes/no): ").strip().lower()
        if cont not in ["yes", "y"]:
            print("You leave the casino with your grapes safe... for now.")
            break
        
        # Get a valid bet from the user
        while True:
            try:
                max_bet = grapes
                bet = int(input(f"How many grapes do you want to bet? (1-{max_bet}): "))
                if 1 <= bet <= max_bet:
                    break
                else:
                    print(f"Invalid bet! Enter a number between 1 and {max_bet}.")
            except ValueError:
                print("Please enter a valid integer.")
        
        # Random outcome
        outcome = random.choices(
            ["win", "lose", "jackpot"], 
            weights=[50, 40, 10],  # 50% win, 40% lose, 10% jackpot
            k=1
        )[0]
        
        # Apply outcome
        if outcome == "win":
            grapes += bet
            print(f"🎉 You win! You gain {bet} grapes. Total grapes: {grapes}")
        elif outcome == "lose":
            grapes -= bet
            print(f"😢 You lose {bet} grapes. Total grapes: {grapes}")
        else:  # jackpot
            jackpot = bet * 5
            grapes += jackpot
            print(f"💥 JACKPOT! You win {jackpot} grapes! Total grapes: {grapes}")
    
    if grapes <= 1:
        print("🍇 You don’t have enough grapes to gamble anymore. Casino closed for you.")

def starter():
    global grapes
    while True:
        guess = input("Enter 'heads' or 'tails': ").strip().lower()
        if guess in ["heads", "tails"]:
            break
        print("Invalid input. Please enter 'heads' or 'tails'.")

    # Flip the coin
    flip = random.choice(["heads", "tails"])
    print(f"The coin landed on {flip}!")

    # Determine result
    if guess == flip:
        grapes += 10
        print("Looks like we got a winner, heres 10 grapes")
    else:
        print("Looks like youll have to try again the next time I see ya.")

if __name__ == "__main__":
    print("Welcome to Grape Odyssey! Your goal is to collect 30 grapes before day 7! What will happen, Noone knows!")
    print(f'You currently have {grapes} grapes\n')
    Array = options(["(1) Pick Grapes in Vineyard", "(2) Travel to the Market", "(3) Travel to Town", "(4) Travel to the Bar", "(5) Travel to the Mountains"])

    while day < 8:
        print(f'It is currently day {day}')
        selection = selectionloop(Array)
        grapes = actions[selection](grapes)
        print(f'You ended day {day} with {grapes} grapes')
        if grapes == 0:
            print("A strange man approaches you with a basket of grapes")
            print("Strange Man: Your looking like you could use some help. Lets play a game.")
            print("Ill flip this here coin, if you call it correctly ill give you these grapes")
            w = input("Sound like a deal? (yes/no): ").strip().lower()
            while w not in ["yes", "no"]:
                print("Invalid input. Please enter 'yes' or 'no'.")
                w = input("Sound like a deal? (yes/no): ").strip().lower()

            # Take action based on choice
            if w == "yes":
                starter()
                print(f'You ended day {day} with {grapes} grapes after gambling')
            elif w == "no":
                print("You decided to not risk getting into risky business")
        if grapes > 9:#gambling

            print("Looking at your sizable harvest you think you can try your luck")
            w = input("Head to the grape casino? (yes/no): ").strip().lower()
            while w not in ["yes", "no"]:
                print("Invalid input. Please enter 'yes' or 'no'.")
                w = input("Head to the grape casino? (yes/no): ").strip().lower()
            if(w == "yes"):
                gambling()
                print(f'You ended day {day} with {grapes} grapes after gambling')
            else:
                print("You decided you werent on a hot streak today and headed home")

        w = input("Press enter to continue to the next day")
        original_print("--------------------------------------------------------------")
        day = day + 1

    if grapes >= 30:
        print("congrats")
    else:
        print("You have failed to gaing the required amount of grapes in the alloted time")
