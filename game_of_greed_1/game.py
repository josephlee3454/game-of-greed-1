from game_of_greed_1.game_of_greed import GameLogic
from game_of_greed_1.game_of_greed import Banker
import sys

def turn(num_dice,roll_dice,turn_count,bank):
      print(f"Starting round {str(turn_count)}") 
      print(f"Rolling {str(num_dice)} dice...")
      dice = roll_dice(num_dice)#dice rolling function is passed in
      while num_dice:
        # if turn_count != 1:
          # print(f"Starting round {str(turn_count)}")
        # if GameLogic.hot_dice(dice,bank):
        #   dice = (1,1,2,2,4,5)
        # else:
          pretty_print_dice(dice)
          zilch_out(dice)
          user_input = input("Enter dice to keep (no spaces), or (q)uit: ")
          if user_input == "q":
            print(f"Total score is {bank.banked_points} points")
            print(f"Thanks for playing. You earned {bank.banked_points} points")
            system_exit()
          user_input_list = [int(num) for num in user_input]
          if GameLogic.is_cheating(user_input_list, dice):
            print("cheater") 
          else: 
            num_dice, remaining_dice = GameLogic.dice_handler(user_input_list, dice)
            current_score = GameLogic.calculat_score(remaining_dice)
            zilch_out(remaining_dice)
            print(f"You have {current_score} unbanked points and {num_dice} dice remaining")
            bank.shelf(current_score)
            play_again(bank, turn_count,num_dice, roll_dice)
            dice = roll_dice(num_dice)

def zilch_out(dice):
  if not GameLogic.calculat_score(dice):
    print("zilch")
    print("game is over!")
    system_exit()


def system_exit():
  GameLogic.roll_dice = saved_roller
  sys.exit()


 

def play_again(bank, turn_count,num_dice, roll_dice):
  bank_user_input = input("(r)oll again, (b)ank your points or (q)uit ")
  while bank_user_input != "r" or bank_user_input != "b" or bank_user_input != "q":
    if bank_user_input == "q":
      bank.bank()
      print(f"Total score is {bank.banked_points} points")
      system_exit()
    
    elif bank_user_input == "y":
      print("this is what is on your shelf  " + str(bank.shelf_storage))

    elif bank_user_input == "b":
      round_points = bank.bank()
      print(f"You banked {round_points} points in round {turn_count}")
      print(f"Total score is {bank.banked_points} points")
      turn_count += 1 
      num_dice = 6
      turn(num_dice, roll_dice, turn_count,bank)
    ## TODO: we need this to prevent infinite loop but its fundamentally wrong 
    else: 
      bank_user_input = input("Roll again y/n ? : ")


saved_roller = GameLogic.roll_dice

def Game(mock_roller = None,bank=Banker()): 
  turn_count = 1
  roll_dice = mock_roller or GameLogic.roll_dice
  print("Welcome to Game of Greed")
  user_game_prompt = input("Wanna play?")
  if user_game_prompt == 'y':
    turn(6, roll_dice, turn_count,bank)
  else:
    print("OK. Maybe another time")
       
  system_exit()

def pretty_print_dice(dice):
  output = ""
  for die in dice:
    output += f"{die},"
  output = output[:-1]
  print(output)


if __name__ == "__main__":
  Game()