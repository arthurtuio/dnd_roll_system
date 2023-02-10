from random import randint


def roll_dice(dice_sides: int) -> int:
    """
    :param dice_sides: The number of sides of the dice
    :return:
    """
    if not isinstance(dice_sides, int):
        raise Exception("param dice_sides must be an integer!")

    return randint(
        1, dice_sides
    )


def convert_dice_expression_to_dict(dice_expression: str) -> dict:
    """
    :param dice_expression: Must be in the form {int1}D{int2}, where:
        - int1: int containing the quantity of dices
        - int2: int containing the dice sides
    :return: dict contaning
    """
    try:
        content = dice_expression.split("d")

        return {
            "number_of_dices": content[0],
            "dice_sides": content[1],
        }

    except Exception:
        raise Exception("Wrong format of variable dice_expression!")


def roll_summary(dice_sides, dice_result):
    def _is_max_roll_achieved(sides, result):
        return (
            True if sides == result else False
        )

    def _is_min_roll_achieved(result):
        return (
            True if result == 1 else False
        )

    return {
        "dice_sides": dice_sides,
        "dice_result": dice_result,
        "is_max_roll_achieved": _is_max_roll_achieved(dice_sides, dice_result),
        "is_min_roll_achieved": _is_min_roll_achieved(dice_result),
    }






