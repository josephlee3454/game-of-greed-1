from game_of_greed_1 import __version__
from game_of_greed_1.game_of_greed import GameLogic
from game_of_greed_1.game_of_greed import Banker
import pytest

def test_version():
    assert __version__ == '0.1.0'


def test_tuple():
    first_die = GameLogic.roll_dice(1)[0]
    assert 1 <= first_die <= 6

@pytest.mark.parametrize('num_dice', [1,2,3,4,5,6])
def test_dice_numbers(num_dice):
    assert len(GameLogic.roll_dice(num_dice)) == num_dice



def test_lots_of_dice():
    for _ in range(1000):
        first_die = GameLogic.roll_dice(5)[0]
        assert 1 <= first_die <= 6

@pytest.mark.parametrize('numbers,score', [
    # ((3),0),
    ((1,1,1,1,1,1), 4000),
    ((1,1,1,1,1), 3000),
    ((1,1,1,1), 2000),
    ((1,1,1), 1000),
    ((1,1), 200),
    ((1,), 100),
    ((2,2,2,2,2,2), 800),
    ((2,2,2,2,2), 600),
    ((2,2,2,2), 400),
    ((2,2,2), 200),
    ((2,2), 0),
    ((2,), 0),
    ((3,3,3,3,3,3), 1200),
    ((3,3,3,3,3), 900),
    ((3,3,3,3), 600),
    ((3,3,3), 300),
    ((3,3), 0),
    ((3,), 0),
    ((4,4,4,4,4,4), 1600),
    ((4,4,4,4,4), 1200),
    ((4,4,4,4), 800),
    ((4,4,4), 400),
    ((4,4), 0),
    ((4,), 0),
    ((5,5,5,5,5,5), 2000),
    ((5,5,5,5,5), 1500),
    ((5,5,5,5), 1000),
    ((5,5,5), 500),
    ((5,5), 100),
    ((5,), 50),
    (5, 50),
    ((6,6,6,6,6,6), 2400),
    ((6,6,6,6,6), 1800),
    ((6,6,6,6), 1200),
    ((6,6,6), 600),
    ((6,6), 0),
    ((6,), 0),
    ((1,2,3,4,5,6), 1500),#straight
    ((1,2,2,3,3,1), 1500),#three pairs
    ((4,4,4,5,5,5), 900),#two sets of three 
    ((4,4,4,1,1), 600),#leftover ones 
    ((4,4,4,5,5), 500)#leftover fives
    ])


def test_score(numbers, score):
    assert GameLogic.calculat_score(numbers) == score

def test_banker_all():
    bank = Banker()
    bank.shelf(50)
    assert bank.shelf_storage == 50
    bank.clear_shelf()
    bank.shelf(50)
    bank.bank()
    assert bank.banked_points == 50

def test_banker_storage():
    bank = Banker()
    bank.banked_points = 50
    assert  bank.banked_points == 50

def test_shelf():
    bank = Banker()
    bank.shelf(100)
    assert bank.shelf_storage == 100

def test_banked_point():
    bank = Banker()
    bank.banked_points = 100
    bank.shelf_storage = 50
    actual = bank.bank()
    expected = 50
    assert actual == expected

def test_clear_shelf():
    bank = Banker()
    bank.shelf_storage = 100
    bank.clear_shelf()
    assert bank.shelf_storage == 0

def test_bank_clear_shelf_no_touching():
    bank = Banker()
    bank.shelf_storage = 50
    bank.bank()
    bank.clear_shelf()
    assert bank.banked_points == 50 and bank.shelf_storage == 0


