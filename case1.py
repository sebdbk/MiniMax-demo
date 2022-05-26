import copy

import super

# MathGame
# First case of an example game

# Rules: Score starts at 0. Players can either add 1, subtract 3, or multiply by -2.
# 6 total actions can be made, alternating between players
# Player 1 needs to make the score as high as possible
# Player 2 needs to make the score as low as possible


class MathGameState(super.EnvState):
    action_list = []

    def possible_actions(self, agent):
        return self.action_list

    def next_turn(self):
        # Players alternate, so Player 1 acts with even actions remaining
        if self.boardstate.actions_remaining % 2 == 0:
            return self.agent1
        else:
            return self.agent2

    def copy(self):
        new_state = MathGameState()
        new_state.agent1 = self.agent1
        new_state.agent2 = self.agent2
        new_state.boardstate = copy.deepcopy(self.boardstate)
        new_state.action_list = self.action_list
        return new_state

    def start_clean(self):
        self.agent1 = super.Agent("Player 1", True)
        self.agent2 = super.Agent("Player 2", False)
        self.boardstate = MathGameBoard()


class MathGameBoard(super.BoardState):
    def __init__(self):
        self.score = 0
        self.actions_remaining = 10

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


class AcSubtractThree(super.Action):
    # Action - subtracts 3 from the score
    def perform(self, agent, boardstate):
        boardstate.score -= 3
        boardstate.actions_remaining -= 1

    def print(self, agent, boardstate):
        print(agent.name + " subtracted 3 from the score.")


class AcMultiplyMinusTwo(super.Action):
    # Action - multiplies score by -2
    def perform(self, agent, boardstate):
        boardstate.score *= -2
        boardstate.actions_remaining -= 1

    def print(self, agent, boardstate):
        print(agent.name + " multiplied score by -2.")


def set_up():
    # Create base state
    base_state = MathGameState()
    base_state.start_clean()
    # Construct list of possible actions
    MathGameState.action_list = [AcAddOne(), AcSubtractThree(), AcMultiplyMinusTwo()]
    # Return base state
    return base_state
