import copy

import super

# Case for Testing

# Rules: Score starts at 0. Players can either add 1, add 3, or multiply by -1.
# Player 1 needs to make the score as high as possible
# Player 2 needs to make the score as low as possible
# Each player will go once

# This case can test the algorithm - for immediate gain, Player 1 would add 3
# However, with predicting the moves of Player 2, the best move is to multiply


class TestGameState(super.EnvState):
    action_list = []

    def possible_actions(self, agent):
        return self.action_list

    def next_turn(self):
        # Players alternate, so Player 1 acts with even actions remaining
        if self.boardstate.actions_remaining == 2:
            return self.agent1
        else:
            return self.agent2

    def copy(self):
        new_state = TestGameState()
        new_state.agent1 = self.agent1
        new_state.agent2 = self.agent2
        new_state.boardstate = copy.deepcopy(self.boardstate)
        new_state.action_list = self.action_list
        return new_state

    def start_clean(self):
        self.agent1 = super.Agent("Player 1", True)
        self.agent2 = super.Agent("Player 2", False)
        self.boardstate = TestGameBoard()


class TestGameBoard(super.BoardState):
    def __init__(self):
        self.score = 0
        self.actions_remaining = 2

    def get_reward(self):
        # In this simple example, reward is the same as current score
        return self.score

    def is_finished(self):
        return self.actions_remaining <= 0


class AcAddOne(super.Action):
    # Action - adds 1 to the score
    def perform(self, agent, boardstate):
        boardstate.score += 1
        boardstate.actions_remaining -= 1

    def print(self, agent, boardstate):
        print(agent.name + " added 1 to the score.")


class AcAddThree(super.Action):
    # Action - adds 3 to the score
    def perform(self, agent, boardstate):
        boardstate.score += 3
        boardstate.actions_remaining -= 1

    def print(self, agent, boardstate):
        print(agent.name + " added 3 to the score.")


class AcMultiplyMinusOne(super.Action):
    # Action - multiplies score by -2
    def perform(self, agent, boardstate):
        boardstate.score *= -1
        boardstate.actions_remaining -= 1

    def print(self, agent, boardstate):
        print(agent.name + " multiplied score by -1.")


def set_up():
    # Create base state
    base_state = TestGameState()
    base_state.start_clean()
    # Construct list of possible actions
    TestGameState.action_list.append(AcAddOne())
    TestGameState.action_list.append(AcAddThree())
    TestGameState.action_list.append(AcMultiplyMinusOne())
    # Return base state
    return base_state
