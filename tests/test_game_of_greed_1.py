from game_of_greed_1 import __version__
import pytest

def test_version():
    assert __version__ == '0.1.0'

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

@pytest.mark.parametrize('numbers,score', [
    ((1,2,2,3,3,1), 1500),
    ((1,2,3,4,5,6), 1500),
    ((4,4,4,5,5,5), 900),
    ((3,3,3,3,2,4), 600),
    ((3,3,3,3), 600),
    ((4,4,4,1,1), 600),
    ((1,1,1,1,1,1), 4000)])
def test_score(numbers, score):
    assert GameLogic.calculat_score(numbers) == score
