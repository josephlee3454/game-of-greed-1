from tests.flow.flo import Flo

def test_flow():
  Flo.test('tests/flow/wanna_play.txt')

def test_bank_one_roll_then_quit():
    Flo.test('tests/flow/bank_one_roll_then_quit.txt')

def test_flow_do_wanna_play_then_quit():
  Flo.test('tests/flow/do_wanna_play_then_quit.txt')
