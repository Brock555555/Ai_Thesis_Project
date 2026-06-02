story_nodes = {

    "start": {
        "text": (
            "You arrive at the legendary Sunhill Vineyard just before the "
            "annual grape harvest festival. The vineyard owner says strange "
            "things have been happening at night. Workers keep disappearing "
            "near the old wine cellar."
        ),

        "choices": [
            ("Start picking grapes", "field"),
            ("Investigate the wine cellar", "cellar"),
            ("Talk to the old farmer", "farmer")
        ]
    },

    "field": {
        "text": (
            "You begin picking grapes under the hot afternoon sun. "
            "After several hours, you discover a hidden trail behind the vines."
        ),

        "choices": [
            ("Follow the hidden trail", "forest"),
            ("Ignore it and keep working", "snake"),
            ("Return to the main barn", "barn")
        ]
    },

    "cellar": {
        "text": (
            "The cellar smells of ancient wine and wet stone. "
            "You hear strange whispering from deeper underground."
        ),

        "choices": [
            ("Explore deeper", "monster"),
            ("Run back upstairs", "barn")
        ]
    },
    "farmer": {
        "text": (
            "The old farmer warns you about the 'Grape Beast,' "
            "a creature that guards the sacred vines at night."
        ),

        "choices": [
            ("Ask where the beast lives", "forest"),
            ("Ignore the warning", "field")
        ]
    },

    "forest": {
        "text": (
            "The trail leads into a dark forest behind the vineyard. "
            "You discover glowing purple grapes hanging from twisted vines."
        ),

        "choices": [
            ("Eat a glowing grape", "magic"),
            ("Collect the grapes carefully", "treasure"),
            ("Leave immediately", "barn")
        ]
    },

    "snake": {
        "text": (
            "While reaching into a vine, you disturb a sleeping snake. "
            "It bites your hand. You become dizzy and collapse."
        ),

        "choices": [
            ("Restart Adventure", "start")
        ]
    },
    "barn": {
        "text": (
            "You return safely to the vineyard barn where workers prepare "
            "for the evening feast. The owner offers you a place to stay."
        ),

        "choices": [
            ("Sleep for the night", "good_ending"),
            ("Sneak out after dark", "cellar")
        ]
    },

    "monster": {
        "text": (
            "Deep underground you discover the legendary Grape Beast — "
            "a giant creature made entirely of vines and grapes."
        ),

        "choices": [
            ("Fight the beast", "bad_ending"),
            ("Offer it grapes", "secret_ending")
        ]
    },

    "magic": {
        "text": (
            "The glowing grape grants you strange visions of hidden treasure "
            "buried beneath the vineyard."
        ),

        "choices": [
            ("Search for the treasure", "treasure"),
            ("Ignore the vision", "barn")
        ]
    },
    "treasure": {
        "text": (
            "Beneath the roots of the ancient vines you uncover a chest filled "
            "with gold coins and rare grape seeds worth a fortune."
        ),

        "choices": [
            ("Take the treasure home", "good_ending"),
            ("Share it with the vineyard", "best_ending")
        ]
    },

    "good_ending": {
        "text": (
            "You survive the grape harvest and leave the vineyard with a "
            "new appreciation for grape picking and adventure."
        ),

        "choices": [
            ("Play Again", "start")
        ]
    },

    "best_ending": {
        "text": (
            "By sharing the treasure, you become a hero of Sunhill Vineyard. "
            "The annual grape festival is renamed in your honor."
        ),

        "choices": [
            ("Play Again", "start")
        ]
    },
    "bad_ending": {
        "text": (
            "The Grape Beast proves too powerful. The vineyard becomes your "
            "permanent resting place."
        ),

        "choices": [
            ("Try Again", "start")
        ]
    },

    "secret_ending": {
        "text": (
            "The Grape Beast accepts your offering and reveals itself to be "
            "the ancient guardian of the vineyard. You are granted eternal "
            "access to the magical grape fields."
        ),

        "choices": [
            ("Play Again", "start")
        ]
    }
}