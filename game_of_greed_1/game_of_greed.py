import random, itertools
from collections import Counter
class GameLogic:
  """
  Gamelogic class
  
  """
  
  def __str__(self):
    return "gamelogic static methods"

  @staticmethod
  def roll_dice(count):
    """
    generates random integer for our dice roll


    Returns:
        integer
    """
    random.randint(1,6)
    output = tuple()
    for i in range(count):
      pass
  
    return tuple(random.randint(1,6) for _ in range(count))

  @staticmethod
  def calculat_score_and_scored_dice(dice: tuple) -> int:
    """
    calculates score

    Args:
        dice (tuple): [description]

    Returns:
        int: [description]
    """

    total = 0
    num_of_scored_dice = 0
    if isinstance(dice,int):
      dice = tuple([dice])
    current_dice = Counter(dice)
    # if len(dice) == 6:
    if len(current_dice) == 6:
      return 1500, 6##straight

    elif list(current_dice.values()).count(2) == 3:
      return 1500, 6##pair
    
    total, num_of_scored_dice = GameLogic.score_triples(total, current_dice, num_of_scored_dice)
    total, num_of_scored_dice = GameLogic.score_singles(total, current_dice, num_of_scored_dice)
    return total, num_of_scored_dice
    
  @staticmethod
  def calculat_score(dice: tuple) -> int:
    score, scored_dice = GameLogic.calculat_score_and_scored_dice(dice)
      
    return score

  
  
  @staticmethod
  def score_triples(total:int, current_dice:tuple, num_of_scored_dice:int) -> int:
    """ scores the triple dice values 

    Args:
        total (int): [description]
        current_dice (tuple): [description]

    Returns:
        int: [description]
    """
   
    for i in range(len(current_dice)):
      current_keys = list(current_dice.keys())
      key1 = current_keys[i]
      key_value = current_dice[current_keys[i]]
      
      if key_value >= 3:
      
        if key1 == 1:
          key1 = 10
        total += (key1*100) + (key_value -3) * key1 * 100
        num_of_scored_dice += key_value
    return total, num_of_scored_dice

  @staticmethod
  def score_singles(total: int, current_dice: tuple, num_of_scored_dice: int) -> int:
    """ scores our single dice values

    Args:
        total (int): [description]
        current_dice (tuple): [description]

    Returns:
        int: [description]
    """

    for i in range(len(current_dice)):
      current_keys = list(current_dice.keys())
      key1 = current_keys[i]
      key_value = current_dice[current_keys[i]]
    
      if key_value <= 2 and key_value >= 0:
        
        if key1 == 1:
          total += key_value*100  
          num_of_scored_dice += key_value 
          
        if key1 == 5:
          total += key_value*50
          num_of_scored_dice += key_value 

    return total, num_of_scored_dice
  @staticmethod
  def dice_handler(int_list:[int],dice:(int)) -> (int,(int)):
    """accepts list of dice indexes to keep and tuple of current dice
    returns number dice-roll quanity and remaining dice. 

    Args:
        int_list ([type]): [description]

    Returns:
        [type]: [description]
    """
    ## TODO : input validation unique and within range
    fresh_dice = len(dice) - len(int_list)
    new_dice = []
    for num in int_list:
      if num in dice:
        new_dice.append(num)
        
    new_dice = tuple(new_dice)
    return (fresh_dice, new_dice)
  @staticmethod
  def is_cheating(int_list:[int],dice:(int))->bool:
    """
    checks for cheaters
    
    """
    if len(int_list) < 1:
      return True
    counted_choices = Counter(int_list)
    counted_dice = Counter(dice)
    for choice in counted_choices:
      real_dice_available = counted_dice[choice]
      dice_requested = counted_choices[choice]
      if real_dice_available < dice_requested:
        print("you are a filthy cheater!")
        return True 
    
    return False 

  @staticmethod
  def hot_dice(dice,bank):
    """
    checks for hot dice
    
    """
    score, scored_dice = GameLogic.calculat_score_and_scored_dice(dice)
    if scored_dice == 6:
      bank.shelf(score)
      bank.bank()
      print(f"Hot dice {dice} banked, {score} points")
      return True
    return False

  @staticmethod
  def get_scorers(dice):
    list_of_possibilities = GameLogic.permutate_dice(dice)
    highest_tuple = tuple()
    highest_score = 0
    for selection in list_of_possibilities:
      score = GameLogic.calculat_score(selection)
      if score > highest_score:
        highest_score = score
        highest_tuple = selection
    return highest_tuple
    
  @staticmethod
  def permutate_dice(dice: tuple) -> list:
    all_possible_dice = set()
    for i in range(1,len(dice) +1):
      for perm in itertools.permutations(dice,i):
        all_possible_dice.add(tuple(sorted(list(perm))))
    return all_possible_dice


    
## check if 6 dice are  scored *
## if 6 dice are scored we need to shelf points*
## print out what ht dice were with a note this is hot dice* 
## if it is hot dice it needs to go back to the loop 


    

  


    





class Banker:
  """
  banker class
  
  """
  def __init__(self):
    """
    initilaizes banker class

    """
    self.shelf_storage = 0
    self.banked_points = 0

  def __str__(self):
    return f"{self.shelf_storage}:{self.banked_points}"

  def __repr__(self):
    return f"{self.shelf_storage}:{self.banked_points}"
 
  def shelf(self,value:int) -> None:
    """
    shelfs the points

    """
    self.shelf_storage += value
    

  def bank(self):
    """ 
    clears the shelf after you adde the banked points

    """
    self.banked_points += self.shelf_storage
    self.clear_shelf()
    return self.banked_points


  def clear_shelf(self):
    """
    clears the shelf 
    """
    self.shelf_storage = 0

