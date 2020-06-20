from game_of_greed import GameLogic
from game_of_greed import Banker
import sys

def turn(num_dice):
      bank = Banker()
      while num_dice:
        dice = GameLogic.roll_dice(num_dice)
        print(dice)
        zilch_out(dice)
        user_input = input("what dice do you want: ")
        user_input_list = [int(num) for num in user_input] 
        num_dice, remaining_dice = GameLogic.dice_handler(user_input_list, dice)
        current_score = GameLogic.calculat_score(remaining_dice)
        zilch_out(remaining_dice)
        print("current_score , ", current_score)
        bank.shelf(current_score)
        play_again(bank)


def zilch_out(dice):
  if not GameLogic.calculat_score(dice):
    print("zilch")
    sys.exit()

  

def play_again(bank):
  bank_user_input = input("Roll again y/n ? : ")
  while bank_user_input != "y" or bank_user_input != "n":
    if bank_user_input == "n":
      bank.bank()
      print("your banked points " + str(bank.banked_points))
      sys.exit()
    
    elif bank_user_input == "y":
      print("this is what is on your shelf  " + str(bank.shelf_storage))
      break 
    ## TODO: we need this to prevent infinite loop but its fundamentally wrong 
    else: 
      bank_user_input = input("Roll again y/n ? : ")
          
if __name__ == "__main__":
    
  turn(6)