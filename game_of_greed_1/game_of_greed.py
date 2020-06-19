import random
from collections import Counter
class GameLogic:
  
  @staticmethod

  def roll_dice(count):
    random.randint(1,6)
    output = tuple()
    for i in range(count):
      pass
    return tuple(random.randint(1,6) for _ in range(count))



    

  @staticmethod
  def calculat_score(dice):
    total = 0
    current_dice = Counter(dice)
    # if len(dice) == 6:
    if len(current_dice) == 6:
      return 1500##straight
    elif list(current_dice.values()).count(2) == 3:
      return 1500##pair

    total = GameLogic.score_triples(total, current_dice)
    total = GameLogic.score_singles(total, current_dice)
    return total
  
  
  @staticmethod
  def score_triples(total, current_dice):
   
    for i in range(len(current_dice)):
      current_keys = list(current_dice.keys())
      key1 = current_keys[i]
      key_value = current_dice[current_keys[i]]

      if key_value >= 3:
        if key1 == 1:
          key1 = 10
        total += (key1*100) + (key_value -3) * key1 * 100
    return total

  @staticmethod
  def score_singles(total, current_dice):

    for i in range(len(current_dice)):
      current_keys = list(current_dice.keys())
      key1 = current_keys[i]
      key_value = current_dice[current_keys[i]]
    
      if key_value <= 2 and key_value >= 0:
        if key1 == 1:
          total += key_value*100  
        if key1 == 5:
          total += key_value*50
    return total 





# class Banker:

#   def shelf():
#     pass

#   def bank():
#     pass

#   def clear_shelf():
#     pass
