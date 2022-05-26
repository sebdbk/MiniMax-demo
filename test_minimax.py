import minimax
import case_test
import unittest


class TestMiniMaxNotOptimised(unittest.TestCase):
    def setUp(self):
        self.base_state = case_test.set_up()

    def test_base_state(self):
        self.assertEqual(self.base_state.boardstate.get_reward(), 0)
        self.assertEqual(self.base_state.is_finished(), False)

    def test_no_possible_actions_returns_same_reward_and_no_action(self):
        self.base_state.action_list = []
        self.base_state.boardstate.score = 1234
        res = minimax.expand_state_not_optimised(self.base_state)
        self.assertEqual(res[0], 1234)
        self.assertEqual(res[1], None)

    def test_minimax_one_iteration(self):
        res = minimax.expand_state_not_optimised(self.base_state, 1)
        self.assertEqual(res[0], 3)
        self.assertIsInstance(res[1], case_test.AcAddThree)

    def test_minimax_two_iterations(self):
        res = minimax.expand_state_not_optimised(self.base_state, 2)
        self.assertEqual(res[0], 0)
        self.assertIsInstance(res[1], case_test.AcMultiplyMinusOne)

    def test_minimax_no_iteration_limit(self):
        res = minimax.expand_state_not_optimised(self.base_state)
        self.assertEqual(res[0], 0)
        self.assertIsInstance(res[1], case_test.AcMultiplyMinusOne)


class TestMiniMaxWithPruning(unittest.TestCase):
    def setUp(self):
        self.base_state = case_test.set_up()

# Check basic properties of MiniMax are preserved
    def test_no_possible_actions_returns_same_reward_and_no_action(self):
        self.base_state.action_list = []
        self.base_state.boardstate.score = 1234
        res = minimax.expand_state_a_b_pruned(self.base_state)
        self.assertEqual(res[0], 1234)
        self.assertEqual(res[1], None)

    def test_minimax_no_iteration_limit(self):
        res = minimax.expand_state_a_b_pruned(self.base_state)
        self.assertEqual(res[0], 0)
        self.assertIsInstance(res[1], case_test.AcMultiplyMinusOne)


if __name__ == '__main__':
    unittest.main()
