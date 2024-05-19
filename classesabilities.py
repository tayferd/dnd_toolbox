races = ["Human", "Elf", "Dwarf", "Halfling", "Gnome", "Orc", "Tiefling", "Dragonborn", "Half-Elf", "Half-Orc",
         "Aarakocra", "Genasi", "Goliath", "Aasimar", "Firbolg", "Kenku", "Tabaxi", "Triton", "Bugbear", "Goblin",
         "Hobgoblin", "Kobold", "Yuan-Ti Pureblood", "Lizardfolk", "Tortle", "Changeling", "Kalashtar", "Shifter",
         "Warforged", "Gith", "Centaur", "Loxodon", "Minotaur", "Simic Hybrid", "Vedalken", "Verdan", "Locathah",
         "Leonin", "Satyr", "Abyssal Tiefling", "Dhampir", "Hexblood", "Reborn"]

melee_classes = ["Barbarian", "Bard", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Cleric", "Artificer"]
spellcasting_classes = ["Bard", "Cleric", "Druid", "Sorcerer", "Warlock", "Paladin", "Ranger", "Wizard", "Artificer", "Blood Hunter"]
classes = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer",
           "Warlock", "Wizard", "Artificer", "Blood Hunter"]

weapons = ["Axe", "Hammer", "Short Sword", "Bow", "Spear"]
armor_list = ["Chain Mail", "Leather", "Scalemail"]
fighter_abilities = ["Riposte", "Precision Attack", "Menacing Attack", "Trip Attack"]


# ... Rest of your code above ...

spells = {
    "Bard": {
        "Damage": ["Dissonant Whispers", "Vicious Mockery", "Thunderwave", "Heat Metal"],
        "Support": ["Hypnotic Pattern", "Invisibility", "Faerie Fire", "Heroism"],
        "Healing": ["Cure Wounds", "Healing Word", "Lesser Restoration", "Song of Rest"]
    },
    "Cleric": {
        "Damage": ["Inflict Wounds", "Sacred Flame", "Guiding Bolt", "Spiritual Weapon"],
        "Support": ["Bless", "Shield of Faith", "Protection from Evil and Good", "Sanctuary"],
        "Healing": ["Cure Wounds", "Healing Word", "Prayer of Healing", "Lesser Restoration"]
    },
    "Druid": {
        "Damage": ["Moonbeam", "Flame Blade", "Thorn Whip", "Call Lightning"],
        "Support": ["Barkskin", "Summon Fey", "Entangle", "Faerie Fire"],
        "Healing": ["Cure Wounds", "Healing Word", "Lesser Restoration", "Healing Spirit"]
    },
    "Paladin": {
        "Damage": ["Sacred Flame", "Bless", "Flame Blade", "Booming Blade"],
        "Support": ["Bless", "Shield of Faith", "Protection from Evil and Good", "Divine Favor"],
        "Healing": ["Cure Wounds", "Lay on Hands", "Lesser Restoration", "Aura of Vitality"]
    },
    "Ranger": {
        "Damage": ["Hail of Thorns", "Hunter's Mark", "Ensnaring Strike", "Conjure Barrage"],
        "Support": ["Barkskin", "Longstrider", "Pass without Trace", "Web"],
        "Healing": ["Cure Wounds", "Healing Spirit", "Lesser Restoration", "Goodberry"]
    },
    "Sorcerer": {
        "Damage": ["Chaos Bolt", "Chromatic Orb", "Burning Hands", "Lightning Bolt"],
        "Support": ["Wall of Fire", "Watery Sphere", "Control Person", "Haste", "Animate Objects", "Telekinesis", "Invisibility", "Polymorph"],
        "Healing": ["Cure Wounds", "Healing Word", "Lesser Restoration", "Revivify"]
    },
    "Warlock": {
        "Damage": ["Eldritch Blast", "Witch Bolt", "", "Arms of Hadar"],
        "Support": ["fear", "Hex", "Invisibility", "Fly"],
        "Healing": ["Cure Wounds", "Healing Word", "Lesser Restoration", "Whispers of the Grave"]
    },
    "Wizard": {
        "Damage": ["Magic Missile", "Fire Bolt", "Burning Hands", "Ray of Sickness"],
        "Support": ["Haste", "Shield", "Raise Undead", "telekenisis", "Invisibility", "Animate Objects", "Polymorph"],
        "Healing": [ "Lesser Restoration", "Falselife", "Vampiric Touch"]
    },
    "Artificer": {
        "Damage": ["Acid Arrow", "Explosive Cannon", "Magic Missle", "Ray of Enfeeblement"],
        "Support": ["Detect Magic", "Invisibility", "Arcane Lock", "Magic Mouth"],
        "Healing": ["Cure Wounds", "Healing Word", "Lesser Restoration", "Aura of Vitality"]
    },
    "Blood Hunter": {
        "Damage": ["Crimson Rite", "Blood Curse", "Vampiric Touch", "Wrathful Smite"],
        "Support": ["Blood Maledict", "Grim Psychometry", "Protection from Evil and Good", "Zone of Truth"],
        "Healing": ["Cure Wounds", "Healing Word", "Lesser Restoration", "Aura of Vitality"]
    },
}

rogue_abilities = [
    "Sneak Attack",
    "Cunning Action",
    "Uncanny Dodge",
    "Evasion",
    "Reliable Talent",
    "Blindsense",
    "Slippery Mind",
    "Elusive",
    "Stroke of Luck"
]
warlock_invocations = [
    "Agonizing Blast",
    "Eldritch Spear",
    "Devil's Sight",
    "Mask of Many Faces",
    "Thirsting Blade",
    "Repelling Blast",
    "Mire the Mind",
    "Bewitching Whispers",
    "Ascendant Step",
    "Lifedrinker",
    "Otherworldly Leap",
    "Whispers of the Grave"
    # Add more invocations as needed
]
monk_abilities = [
    "Unarmored Defense",
    "Martial Arts",
    "Ki",
    "Flurry of Blows",
    "Patient Defense",
    "Step of the Wind",
    "Deflect Missiles",
    "Slow Fall",
    "Stunning Strike",
    "Ki-Empowered Strikes",
    "Evasion",
    "Stillness of Mind",
    "Purity of Body",
    "Tongue of the Sun and Moon",
    "Empty Body",
    "Perfect Self"
    # Add more monk abilities as needed
]

sorcerer_metamagic = [
    "Careful Spell",
    "Distant Spell",
    "Empowered Spell",
    "Extended Spell",
    "Heightened Spell",
    "Quickened Spell",
    "Subtle Spell",
    "Twinned Spell"
]

blood_hunter_abilities = [
    "Crimson Rite",
    "Blood Maledict",
    "Hunter's Bane",
    "Brand of Castigation",
    "Sanguine Mastery",
    "Rite of the Dawn",
    "Brand of Tethering",
    "Rite of the Storm",
    "Brand of the Searing Strike",
    "Rite of the Frozen"
]

paladin_smites = [
    "Divine Smite",
    "Wrathful Smite",
    "Thunderous Smite",
    "Branding Smite",
    "Searing Smite",
    "Blinding Smite",
    "Staggering Smite",
    "Banishing Smite",
    "Crusader's Smite",
    "Eldritch Smite"
]

wizard_spells = [
    "Magic Missile",
    "Fire Bolt",
    "Burning Hands",
    "Ray of Sickness",
    "Thunderwave",
    "Chromatic Orb",
    "Feather Fall",
    "Mage Armor",
    "Shield",
    "Misty Step",
    "Invisibility",
    "Cure Wounds",
    "Healing Word",
    "Lesser Restoration",
    "Revivify",
    "Fly",
    "Counterspell",
    "Fireball",
    "Lightning Bolt",
    "Haste"
]