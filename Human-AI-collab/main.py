"""
Main Game Module: Grape Odyssey
Handles the main game loop, user menus, and minigames (Gambling/Coin Flip).
"""

import events
from events import type_print  # <-- Imports the retro typing effect for narrative beats
import sys
import random

# Global state variables for the player's progress
grapes = 0
day = 1

class Options:
    """
    A class to manage and display numbered menu options to the user.
    """
    def __init__(self, array):
        """
        Initializes the Options object.
        WHY: Encapsulating the list inside an object allows us to easily build
        reusable menu behaviors (like dynamic lengths) without rewriting loop logic.
        """
        self.array = array

    def display_options(self):
        """
        Prints the available options to the terminal sequentially.
        WHY: Provides a clean, standardized UI format every time the user needs to make a choice.
        NOTE: This uses standard print() so the UI renders instantly without the typing delay.
        """
        print(f'Please pick an option from 1 to {len(self.array)}')
        for item in self.array:
            print(item)
        print()

    def length(self):
        """
        Returns the total number of options available.
        WHY: Used by the input validator to ensure the user doesn't pick a number out of bounds.
        """
        return len(self.array)


# Execution mapping table
# WHY: A dictionary mapping replaces massive 'if/elif/else' blocks. It allows O(1) 
# instantaneous lookup to execute the correct event function based on user input.
ACTIONS = {
    1: events.VineyardEvents,
    2: events.MarketEvents,
    3: events.TownEvents,
    4: events.BarEvents,
    5: events.MountainEvents
}

def selection_loop(options_obj):
    """
    Handles user input for the main menu, ensuring valid selection.
    
    Args:
        options_obj (Options): The initialized menu object.
        
    Returns:
        int: A valid integer representing the user's choice.
    """
    options_obj.display_options()
    limit = options_obj.length()
    
    while True:
        x = input("Your selection: ")
        try:
            x = int(x) # Attempt to cast string to integer
            
            # Check if the selection is within valid menu boundaries
            if 1 <= x <= limit:
                # Temporary guardrail for unfinished features
                if 1 < x < 5:
                    print("Not yet implemented, please pick 1 or 5")
                    continue
                return x # Return valid selection to the main loop
            
            print("Invalid selection")
        except ValueError:
            # Catches cases where the user types letters instead of numbers
            print("Invalid selection")

def gambling(current_grapes):
    """
    A casino minigame allowing the player to risk grapes for a chance to multiply them.
    
    Args:
        current_grapes (int): The player's current grape count.
        
    Returns:
        int: The updated grape count after winning/losing.
    """
    type_print("💰 Welcome to the Vineyard Casino!")
    
    # Keep gambling as long as they have grapes to bet (minimum 2 to make a meaningful bet)
    while current_grapes > 1:
        type_print(f"\nYou currently have {current_grapes} grapes.")
        
        # Ask if they want to continue
        cont = input("Do you want to gamble? (yes/no): ").strip().lower()
        if cont not in ("yes", "y"):
            type_print("You leave the casino with your grapes safe.")
            break # Exit the casino loop
        
        # Get a valid bet from the user
        while True:
            try:
                bet = int(input(f"How many grapes do you want to bet? (1-{current_grapes}): "))
                if 1 <= bet <= current_grapes:
                    break # Valid bet secured, exit validation loop
                print(f"Invalid bet! Enter a number between 1 and {current_grapes}.")
            except ValueError:
                print("Please enter a valid integer.")
        
        # Establish casino weights: 40% win, 50% lose, 10% jackpot
        # WHY: random.choices allows us to skew probabilities easily without complex math.
        outcome = random.choices(["win", "lose", "jackpot"], weights=[40,50,10], k=1)
        outcome = outcome[0]
        # Apply the randomized outcome to the player's wallet using the typing effect
        if outcome == "win":
            current_grapes += bet
            type_print(f"🎉 You win! You gain {bet} grapes. Total: {current_grapes}")
        elif outcome == "lose":
            current_grapes -= bet
            type_print(f"😢 You lose {bet} grapes. Total: {current_grapes}")
        else: # jackpot condition
            jackpot = bet * 5
            current_grapes += jackpot
            type_print(f"💥 JACKPOT! You win {jackpot} grapes! Total: {current_grapes}")
            
    if current_grapes <= 1:
        type_print("🍇 Casino closed for you.")
        
    # WHY: We must return the local variable back to the main loop to overwrite the global state.
    return current_grapes

def starter(current_grapes):
    """
    A 50/50 coin flip minigame triggered when the player hits 0 grapes.
    
    Args:
        current_grapes (int): The player's grape count (usually 0).
        
    Returns:
        int: The updated grape count.
    """
    while True:
        guess = input("Enter 'heads' or 'tails': ").strip().lower()
        if guess in ("heads", "tails"):
            break
        print("Invalid input.")

    # Flip the coin natively using random.choice
    flip = random.choice(["heads", "tails"])
    type_print(f"The coin landed on {flip}!")

    # Determine result
    if guess == flip:
        current_grapes += 10
        type_print("Winner! Here are 10 grapes.")
    else:
        type_print("Better luck next time.")
        
    return current_grapes

if __name__ == "__main__":
    # Boot sequence and introduction (Uses narrative typing effect)
    type_print("Welcome to Grape Odyssey! Collect 30 grapes before day 7!")
    type_print(f'You currently have {grapes} grapes\n')
    
    # Initialize the main menu object
    menu = Options(["(1) Pick Grapes in Vineyard", "(2) Travel to the Market", "(3) Travel to Town", "(4) Travel to the Bar", "(5) Travel to the Mountains"])

    # Core Game Loop: Runs until the time limit (day 8) is reached
    while day < 8:
        type_print(f'\nIt is currently day {day}')
        
        # Retrieve the user's destination
        selection = selection_loop(menu)
        
        # Pull execution tracking pointers safely from configuration dict
        # WHY: .get() prevents KeyError crashes if something unexpected slips through.
        action_func = ACTIONS.get(selection)
        if action_func:
            # Execute the targeted location function, passing and updating the grape count
            grapes = action_func(grapes)
            
        type_print(f'You ended day {day} with {grapes} grapes')
        
        # --- Pity Mechanic (Coin Flip) ---
        if grapes == 0:
            type_print("A strange man approaches you with a basket of grapes")
            type_print("Strange Man: You're looking like you could use some help. Let's play a game.")
            type_print("I'll flip this here coin, if you call it correctly I'll give you these grapes")
            
            w = input("Sound like a deal? (yes/no): ").strip().lower()
            while w not in ("yes", "no"):
                w = input("Sound like a deal? (yes/no): ").strip().lower()
            
            if w == "yes":
                grapes = starter(grapes) # Update grapes with winnings
            elif w == "no":
                type_print("You decided to not risk getting into risky business")

        # --- Casino Trigger ---
        if grapes > 9:
            type_print("Looking at your sizable harvest you think you can try your luck")
            w = input("Head to the grape casino? (yes/no): ").strip().lower()
            while w not in ("yes", "no"):
                w = input("Head to the grape casino? (yes/no): ").strip().lower()
            
            if w == "yes":
                grapes = gambling(grapes) # Update grapes with winnings/losses
            else:
                type_print("You decided you weren't on a hot streak today and headed home")

        # Wait for the user to acknowledge the day's end before clearing the terminal conceptually
        input("\nPress enter to continue to the next day")
        print("--------------------------------------------------------------")
        day += 1

    # End condition evaluation
    type_print("Congrats" if grapes >= 30 else "You have failed to gain the required amount of grapes in the allotted time.")