from src.modules.dice_roller import DiceRoller

INITIAL_TEXT = (
    "Please insert what will be your roll"
    + " something like 5d4, the first number is the number of dices,"
    + " and the second the number of sides in the dice! \n"
)

FIRST_INPUT_TEXT = "### Insert the number of dices: "
SECOND_INPUT_TEXT = "### Insert the sides of these dices: "


def main():
    print(INITIAL_TEXT)

    number_of_dices = int(input(FIRST_INPUT_TEXT))
    dice_sides = int(input(SECOND_INPUT_TEXT))

    result = DiceRoller(
        number_of_dices=number_of_dices,
        dice_sides=dice_sides
    ).run()

    print(result['text_representation'])


if __name__ == '__main__':
    main()