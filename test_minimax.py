import minimax
import test_case
import unittest


class TestMiniMax(unittest.TestCase):
    def setUp(self):
        self.base_state = test_case.set_up()

    def test_base_state(self):
        self.assertEqual(self.base_state.boardstate.get_reward(), 0)
        self.assertEqual(self.base_state.is_finished(), False)

    def test_no_possible_actions_returns_same_reward_and_no_action(self):
        self.base_state.action_list = []
        self.base_state.boardstate.score = 1234
        res = minimax.expand_state(self.base_state)
        self.assertEqual(res[0], 1234)
        self.assertEqual(res[1], None)

    def test_minimax_one_iteration(self):
        res = minimax.expand_state(self.base_state, 1)
        self.assertEqual(res[0], 3)
        self.assertIsInstance(res[1], test_case.AcAddThree)

    def test_minimax_two_iterations(self):
        res = minimax.expand_state(self.base_state, 2)
        self.assertEqual(res[0], 0)
        self.assertIsInstance(res[1], test_case.AcMultiplyMinusOne)

    def test_minimax_no_iteration_limit(self):
        res = minimax.expand_state(self.base_state)
        self.assertEqual(res[0], 0)
        self.assertIsInstance(res[1], test_case.AcMultiplyMinusOne)


if __name__ == '__main__':
    unittest.main()
