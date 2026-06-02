# events.py
import random

def random_event(location):
    vineyard_events = [
        ("A bee lands on your nose. You stay perfectly still... it leaves peacefully.", +0),
        ("You pick the juiciest bunch ever. A true masterpiece.", +3),
        ("A bird swoops down and steals some grapes. Rude!", -2),
        ("You slip in grape juice. The grapes are fine, but your pride is bruised.", +0),
        ("You find a golden grape! It hums softly. Weird.", +5)
    ]

    town_events = [
        ("You try to sell grapes but accidentally join a grape-eating contest.", -3),
        ("A merchant offers to trade grapes for socks. You decline... mostly.", 0),
        ("You sell grapes to a fancy chef who calls you 'Monsieur du Raisin'.", +4),
        ("You drop your grapes while waving at a stranger. Smooth move.", -2),
        ("You meet a talking dog who loves grapes. You share some.", -1)
    ]

    mountains_events = [
        ("You climb the hill and find wild grapes — bonus harvest!", +5),
        ("A raccoon steals your grapes and your hat.", -3),
        ("The mountain air fills you with vigor. You pick faster!", +2),
        ("You see the ghost of a legendary picker whisper 'ferment wisely...'", +0),
        ("You find a secret spring of grape soda.", +3)
    ]

    tavern_events = [
        ("You challenge the barkeep to a grape-stomping duel. You lose gracefully.", -2),
        ("You meet an old picker who gifts you a lucky stem.", +1),
        ("You tell tall tales of your harvest and everyone buys you drinks.", +2),
        ("You mistake a raisin for a grape. Existential crisis ensues.", +0),
        ("You drop your grapes in a barrel. They start fermenting!", +4)
    ]

    all_events = {
        "vineyard": vineyard_events,
        "town": town_events,
        "mountains": mountains_events,
        "tavern": tavern_events
    }

    return random.choice(all_events.get(location, vineyard_events))
