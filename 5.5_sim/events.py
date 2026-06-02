import random


def random_event(player, npcs):
    events = [
        snake_event,
        storm_event,
        theft_event,
        bonus_event,
        maria_event
    ]

    chosen = random.choice(events)

    return chosen(player, npcs)



def snake_event(player, npcs):
    player.health -= 10
    return "A snake hidden in the vines bites your arm."



def storm_event(player, npcs):
    player.stamina -= 5
    return "Heavy rain slows the harvest and ruins part of the crop."



def theft_event(player, npcs):
    player.reputation -= 5
    return "Workers accuse each other of stealing supplies."



def bonus_event(player, npcs):
    player.money += 15
    return "The foreman rewards the crew for exceeding quota."



def maria_event(player, npcs):
    maria = None
    for npc in npcs:
        if npc.name == "Maria":
            maria = npc

    if maria:
        maria.trust += 10

    player.reputation += 2

    return "Maria shares food with you beside the campfire."