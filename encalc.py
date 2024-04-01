def calculate_encounter_xp(party_level, num_players, difficulty):
    # XP thresholds by character level and difficulty (easy, medium, hard, deadly)
    xp_thresholds = {
        1: {"easy": 25, "medium": 50, "hard": 75, "deadly": 100},
        2: {"easy": 50, "medium": 100, "hard": 150, "deadly": 200},
        3: {"easy": 75, "medium": 150, "hard": 225, "deadly": 400},
        4: {"easy": 125, "medium": 250, "hard": 375, "deadly": 500},
        # Continue adding levels up to 20...
    }

    # Ensure party_level and num_players are integers
    party_level = int(party_level)
    num_players = int(num_players)

    # Determine adjustment strategy based on party size
    if num_players < 4:
        size_modifier = "reduce"  # Encounters should be easier for smaller parties
    elif num_players > 5:
        size_modifier = "increase"  # Encounters should be harder for larger parties
    else:
        size_modifier = "none"  # No adjustment needed for standard party sizes

    # Calculate XP threshold based on party level, difficulty, and size
    if party_level in xp_thresholds:
        base_xp_per_player = xp_thresholds[party_level][difficulty]

        # Adjust the base XP per player based on the adjustment strategy
        if size_modifier == "reduce":
            total_xp = base_xp_per_player * num_players * 0.75  # Example modifier to reduce difficulty
        elif size_modifier == "increase":
            total_xp = base_xp_per_player * num_players * 1.25  # Example modifier to increase difficulty
        else:
            total_xp = base_xp_per_player * num_players  # No modification

        return total_xp
    else:
        return "Level out of range. Please add XP thresholds for this level."

# Example usage
party_level = input("Enter party level: ")
num_players = input("Enter number of players: ")
difficulty = input("Enter difficulty (easy, medium, hard, deadly): ")
print(calculate_encounter_xp(party_level, num_players, difficulty))
