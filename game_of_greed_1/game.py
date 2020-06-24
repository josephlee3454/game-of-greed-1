from game_of_greed_1.game_of_greed import GameLogic
from game_of_greed_1.game_of_greed import Banker
import sys

def turn(num_dice, roll_dice):
      bank = Banker()
      while num_dice:
        dice = roll_dice(num_dice) # dice rolling function is passed in
        print(",".join([str(d) for d in dice]))
        zilch_out(dice)
        user_input = input("what dice do you want: ")
        user_input_list = [int(num) for num in user_input]
        num_dice, remaining_dice = GameLogic.dice_handler(user_input_list, dice)
        current_score = GameLogic.calculat_score(remaining_dice)
        zilch_out(remaining_dice)
        print(f"current_score ,  {current_score}")
        bank.shelf(current_score)
        play_again(bank)


def zilch_out(dice):
  if not GameLogic.calculat_score(dice):
    print("zilch")
    # system_exit()

def system_exit():
  sys.exit()




def play_again(bank):
  bank_user_input = input("Roll again y/n ? : ")
  while bank_user_input != "y" or bank_user_input != "n":
    if bank_user_input == "n":
      bank.bank()
      print("your banked points " + str(bank.banked_points))
      system_exit()

    elif bank_user_input == "y":
      print("this is what is on your shelf  " + str(bank.shelf_storage))
      break
    ## TODO: we need this to prevent infinite loop but its fundamentally wrong
    else:
      bank_user_input = input("Roll again y/n ? : ")


def Game(mock_roller = None):

  # use a mock dice roller if provided
  # otherwise use default
  roll_dice = mock_roller or GameLogic.roll_dice

  print("Welcome to Game of Greed")
  user_game_prompt = input("Wanna play?")
  if user_game_prompt == 'y':
    turn(6, roll_dice)
  else:
    print("OK. Maybe another time")

  system_exit()


if __name__ == "__main__":
  Game()
