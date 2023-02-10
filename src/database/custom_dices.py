"""
Simulates a database table, with the following structure
- name[str]
- dices[str]: In the format {Int1}D{Int2}, Int1 being the number of dices, and Int2 the number of sides
- constant[int]: If adds a constant to the dice
- proficiency_bonus[bool]: If True adds a proficiency bonus
"""


CUSTOM_DICES = [
    {
        "name": "shortsword",
        "dices": "1d8",
        "constant": 0,
        "proficiency_bonus": True,
    },
    {
        "name": "shorbow",
        "dices": "1d8",
        "constant": 2,
        "proficiency_bonus": False,
    },
    {
        "name": "greatsword",
        "dices": "2d6",
        "constant": 0,
        "proficiency_bonus": True,
    },
]
