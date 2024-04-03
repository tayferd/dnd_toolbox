from flask import Flask, request, jsonify

app = Flask(__name__)
# Example monster list by XP values
import random


def suggest_monsters(total_xp):
    suggestions = []
    # Copy the monster lists so we can safely modify them in the loop
    available_monsters = {xp: monsters[:] for xp, monsters in monsters_by_xp.items()}

    while total_xp > 0:
        # Filter out monster lists that are too expensive or empty
        affordable_monsters = {xp: monsters for xp, monsters in available_monsters.items() if
                               xp <= total_xp and monsters}
        if not affordable_monsters:
            break  # No more monsters can fit within the budget

        # Randomly select an affordable XP value and then a monster from that list
        xp = random.choice(list(affordable_monsters.keys()))
        monster = random.choice(affordable_monsters[xp])

        # Add the selected monster to the suggestions and adjust the total XP
        suggestions.append(monster)
        total_xp -= xp

        # Optionally, remove the selected monster from future consideration
        available_monsters[xp].remove(monster)

    return suggestions


monsters_by_xp = {
    10: [
        "Baboon", "Cat", "Commoner", "Crab", "Deer", "Eagle", "Frog", "Giant Fire Beetle",
        "Goat", "Hawk", "Homunculus", "Lemure", "Lizard", "Octopus", "Owl", "Quipper",
        "Rat", "Raven", "Scorpion", "Sea Horse", "Shrieker", "Spider", "Vulture", "Weasel"
    ],
    25: [
        "Bandit", "Blood Hawk", "Camel", "Cultist", "Draft Horse", "Dretch", "Flying Snake",
        "Giant Rat", "Giant Weasel", "Guard", "Kobold", "Merfolk", "Mule", "Noble",
        "Poisonous Snake", "Pony", "Riding Horse", "Skeleton", "Sprite", "Steam Mephit",
        "Stirge", "Tribal Warrior", "Troglodyte", "Zombie"
    ],
    50: [
        "Acolyte", "Axe Beak", "Blink Dog", "Boar", "Constrictor Snake", "Elk", "Giant Badger",
        "Giant Bat", "Giant Centipede", "Giant Frog", "Giant Lizard", "Giant Owl",
        "Giant Poisonous Snake", "Giant Wolf Spider", "Goblin", "Jackalwere", "Panther",
        "Pseudodragon", "Sahuagin", "Satyr", "Swarm of Rats", "Swarm of Ravens", "Wolf", "Worg"
    ],
    100: [
        "Black Bear", "Cockatrice", "Crocodile", "Darkmantle", "Dust Mephit", "Gas Spore",
        "Gargoyle", "Gelatinous Cube", "Ghast", "Giant Eagle", "Giant Hyena", "Giant Octopus",
        "Giant Toad", "Giant Vulture", "Gnoll", "Gray Ooze", "Harpy", "Hippogriff", "Imp",
        "Lion", "Mimic", "Minotaur Skeleton", "Orc", "Reef Shark", "Rust Monster", "Shadow",
        "Swarm of Insects", "Warhorse", "Warhorse Skeleton", "Wight", "Will-o'-Wisp"
    ]
    # Note: Add more XP keys and monsters as needed for a complete list
}



def calculate_encounter_xp(party_level, num_players, difficulty):
    # XP thresholds by character level and difficulty (easy, medium, hard, deadly)
    xp_thresholds = {
        1: {"easy": 25, "medium": 50, "hard": 75, "deadly": 100},
        2: {"easy": 50, "medium": 100, "hard": 150, "deadly": 200},
        3: {"easy": 75, "medium": 150, "hard": 225, "deadly": 400},
        4: {"easy": 125, "medium": 250, "hard": 375, "deadly": 500},
        5: {"easy": 250, "medium": 500, "hard": 750, "deadly": 1100},
        6: {"easy": 300, "medium": 600, "hard": 900, "deadly": 1400},
        7: {"easy": 350, "medium": 750, "hard": 1100, "deadly": 1700},
        8: {"easy": 450, "medium": 900, "hard": 1400, "deadly": 2100},
        9: {"easy": 550, "medium": 1100, "hard": 1600, "deadly": 2400},
        10: {"easy": 600, "medium": 1200, "hard": 1900, "deadly": 2800},
        11: {"easy": 800, "medium": 1600, "hard": 2400, "deadly": 3600},
        12: {"easy": 1000, "medium": 2000, "hard": 3000, "deadly": 4500},
        13: {"easy": 1100, "medium": 2200, "hard": 3400, "deadly": 5100},
        14: {"easy": 1250, "medium": 2500, "hard": 3800, "deadly": 5700},
        15: {"easy": 1400, "medium": 2800, "hard": 4300, "deadly": 6400},
        16: {"easy": 1600, "medium": 3200, "hard": 4800, "deadly": 7200},
        17: {"easy": 2000, "medium": 3900, "hard": 5900, "deadly": 8800},
        18: {"easy": 2100, "medium": 4200, "hard": 6300, "deadly": 9500},
        19: {"easy": 2400, "medium": 4900, "hard": 7300, "deadly": 10900},
        20: {"easy": 2800, "medium": 5700, "hard": 8500, "deadly": 12700},
    }



    # Ensure party_level and num_players are integers
    party_level = int(party_level)
    num_players = int(num_players)

    # Determine adjustment strategy based on party size
    if num_players < 4:
        size_modifier = "reduce"
    elif num_players > 5:
        size_modifier = "increase"
    else:
        size_modifier = "none"

    # Calculate XP threshold based on party level, difficulty, and size
    if party_level in xp_thresholds:
        base_xp_per_player = xp_thresholds[party_level][difficulty]

        if size_modifier == "reduce":
            total_xp = base_xp_per_player * num_players * 0.75
        elif size_modifier == "increase":
            total_xp = base_xp_per_player * num_players * 1.25
        else:
            total_xp = base_xp_per_player * num_players

        return total_xp
    else:
        return "Level out of range. Please add XP thresholds for this level."

@app.route('/calculate_xp', methods=['POST'])
def calculate_xp():
    data = request.get_json()

    party_level = data.get('party_level')
    num_players = data.get('num_players')
    difficulty = data.get('difficulty')

    if party_level is None or num_players is None or difficulty is None:
        return jsonify({"error": "Missing data for party_level, num_players, or difficulty"}), 400

    try:
        total_xp = calculate_encounter_xp(party_level, num_players, difficulty)
        suggestions = suggest_monsters(total_xp)
        return jsonify({"total_xp": total_xp, "suggestions": suggestions})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)
