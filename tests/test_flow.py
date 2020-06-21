from tests.flow.flo import Flo

def test_flow():
  assert Flo

  Flo.test('tests/flow/wanna_play.txt')

def test_flow_bank_one():
  Flo.test('tests/flow/bank_one_roll_then_quit.txt')