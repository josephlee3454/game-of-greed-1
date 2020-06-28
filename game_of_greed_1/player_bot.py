from game_of_greed_1.game_of_greed import GameLogic, Banker
from game_of_greed_1.game import Game
import builtins
import re


""""
Create a Game of Greed Player Bots
ONLY use public methods
- Game class constructor and play method
- DO NOT INJECT CUSTOM ROLL FUNCTION
- GameLogic, all methods available
"""


class BasePlayer:
    def __init__(self):
        self.old_print = print
        self.old_input = input
        builtins.print = self._mock_print
        builtins.input = self._mock_input
        self.total_score = 0

    def reset(self):
        builtins.print = self.old_print
        builtins.input = self.old_input

    def _mock_print(self, *args, **kwargs):
        self.old_print(*args, **kwargs)

    def _mock_input(self, *args, **kwargs):
        return self.old_input(*args, **kwargs)

    @classmethod
    def play(cls, num_games=1):

        mega_total = 0

        for i in range(num_games):
            player = cls()
            try:
                Game()
            except SystemExit:
                pass
                # player.old_print('Caught the Exception')
                # commented out to clear up the terminal screen
            # Game()
            mega_total += player.total_score
            player.reset()

        print(
            f"{num_games} games (maybe) played with average score of {mega_total // num_games}"
        )


class Naysayer(BasePlayer):
    def _mock_input(self, *args, **kwargs):
        return "n"

    def _mock_print(self, *args, **kwargs):
        self.old_print(args[0])


class NervousNellie(BasePlayer):
    def __init__(self):
        super().__init__()
        self.roll = None

    def _mock_print(self, *args, **kwargs):
        first_arg = args[0]
        first_char = first_arg[0]
        # self.old_print(*args)
        if first_char.isdigit():
            self.roll = tuple(int(char) for char in first_arg.split(","))
        elif first_arg.startswith("Total score is"):
            # self.old_print(*args)
            self.total_score = int(re.findall(r"\d+", first_arg)[0])
        else:
          pass
            # self.old_print(*args)

    def _mock_input(self, *args, **kwargs):
        prompt = args[0]
        if prompt.startswith("Wanna play?"):
            return "y"
        elif prompt.startswith("Enter dice to keep (no spaces), or (q)uit:"):
            scorers = GameLogic.get_scorers(self.roll)
            keepers = "".join([str(ch) for ch in scorers])
            return keepers
        elif prompt.startswith("(r)oll again, (b)ank your points or (q)uit "):
            return "b"
        else:
            raise ValueError(f"Unrecognized prompt {prompt}")


class UberLeetBot(BasePlayer):
    def __init__(self):
        super().__init__()
        self.roll = None
        self.num_selected_dice = tuple()
    def _mock_input(self, *args, **kwargs):
        prompt = args[0]
        if prompt.startswith("Wanna play?"):
            return "y"

        elif prompt.startswith("Enter dice to keep (no spaces), or (q)uit:"):
            if len(self.roll) >= 3:  # over 400 pts:
                # self.old_print(self.roll)
                scorers = GameLogic.get_scorers(self.roll)
                keepers = "".join([str(ch) for ch in scorers])
                self.num_selected_dice = len(keepers)
                return keepers
            else:
                return "q"

        elif prompt.startswith("(r)oll again, (b)ank your points or (q)uit"):
            remaining_dice = len(self.roll) - self.num_selected_dice
            if self.num_selected_dice == len(self.roll) or  remaining_dice < 3:
              return "q"
            else:
              return "r"

    def _mock_print(self, *args, **kwargs):
        first_arg = args[0]
        first_char = first_arg[0]
        if first_char.isdigit():
            self.roll = tuple(int(char) for char in first_arg.split(","))
        elif first_arg.startswith("Total score is"):
            self.total_score = int(re.findall(r"\d+", first_arg)[0])



def string_dice_tup(dice):
    output = ""
    for die in dice:
        output += f"{die}"
    output = output[:-1]
    return output


if __name__ == "__main__":
    # Naysayer.play(100)
    print("NervousNellie points")
    NervousNellie.play(1000)  # 20 rounds average score 8000

    print("Uberleetbot points")
    UberLeetBot.play(1000)

