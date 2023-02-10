from src.modules.utils import roll_dice


class DiceRoller:
    """
    Class single responsibility is to roll dices, and return the results.
    Main method is named `run`.
    """
    def __init__(
        self,
        number_of_dices: int,
        dice_sides: int,
    ):
        self.number_of_dices = number_of_dices
        self.dice_sides = dice_sides

    def run(self) -> dict:
        print("Rolling {}d{}...\n".format(self.number_of_dices, self.dice_sides))

        summed_result = 0
        results_list = []

        roll_counter = 0

        while roll_counter < self.number_of_dices:
            roll_counter += 1

            rolled_dice = roll_dice(self.dice_sides)

            results_list.append(rolled_dice)
            summed_result += rolled_dice

        return {
            "summed_result": summed_result,
            "results_list": results_list,
            "dice_sides": self.dice_sides,
            "text_representation": self._create_text_representation(
                results_list, summed_result
            )
        }

    def _create_text_representation(self, results_list, summed_result):
        text = "You rolled {}d{}, the results were `{}`, and the summed_result was: `{}`"

        return text.format(
            self.number_of_dices,
            self.dice_sides,
            results_list,
            summed_result
        )
