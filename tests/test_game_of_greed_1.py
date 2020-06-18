from game_of_greed_1 import __version__
from game_of_greed_1.game_of_greed import GameLogic


def test_version():
    assert __version__ == '0.1.0'


def test_tuple():
    first_die = GameLogic.roll_dice(1)[0]
    assert 1 <= first_die <= 6

def test_lots_of_dice():
    for _ in range(1000):
        first_die = GameLogic.roll_dice(5)[0]
        assert 1 <= first_die <= 6

def test_three_pairs_scoring():
    the_function = GameLogic.calculat_score((1,2,2,3,3,1))
    assert the_function == 1500


def test_straight_scoring():
    the_function = GameLogic.calculat_score((1,2,3,4,5,6))
    assert the_function == 1500

def test_mutiples_scoring():
    the_function = GameLogic.calculat_score((4,4,4,5,5,5))
    assert the_function == 900

def test_four_three_mutiple():
    the_function = GameLogic.calculat_score((3,3,3,3,2,4))
    assert the_function == 600

def test_with_less():
    the_function = GameLogic.calculat_score((3,3,3,3))
    assert the_function == 600

def test_44411():
    the_function = GameLogic.calculat_score((4,4,4,1,1))
    assert the_function == 600