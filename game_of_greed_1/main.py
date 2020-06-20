from game_of_greed import GameLogic
from game_of_greed import Banker
import sys


if __name__ == "__main__":
    bank = Banker()
    def main(num_dice):
      while num_dice:
        dice = GameLogic.roll_dice(num_dice)
        print(dice)
        if GameLogic.calculat_score(dice) == 0:
          print("zilch")
          sys.exit()
        user_input = input("what dice do you want: ")
        user_input_list = [int(num) for num in user_input] 
      
        num_dice, remaining_dice = GameLogic.dice_handler(user_input_list, dice)
        current_score = GameLogic.calculat_score(remaining_dice)
        if current_score == 0:
          print("zilch")
          sys.exit()
        print("current_score , ", current_score)
        bank.shelf(current_score)
        bank_user_input = input("Roll again ? : ")
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
            bank_user_input = input("Roll again ? : ")
            
          
    main(6)