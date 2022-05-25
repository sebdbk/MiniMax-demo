import super

# MathGame
# First case of an example game

# Rules: Score starts at 0. Players can either add 1, subtract 3, or multiply by -2.
# Player 1 needs to make the score as high as possible
# Player 2 needs to make the score as low as possible


class MathGameState(super.EnvState):
    action_list = []

    def __init__(self):
        super(MathGameState, self).__init__()

    def possible_actions(self, agent):
        return self.action_list


class MathGameBoard(super.BoardState):
    def __init__(self):
        self.score = 0

    def get_reward(self):
        # In this simple example, reward is the same as current score
        return self.score


class AcAddOne(super.Action):
    # Action - adds 1 to the score
    def __init__(self):
        pass

    def perform(self, agent, boardstate):
        boardstate.score += 1


class AcSubtractThree(super.Action):
    # Action - adds 1 to the score
    def __init__(self):
        pass

    def perform(self, agent, boardstate):
        boardstate.score -= 3


class AcMultiplyMinusTwo(super.Action):
    # Action - adds 1 to the score
    def __init__(self):
        pass

    def perform(self, agent, boardstate):
        boardstate.score *= -2


def set_up():
    # Create base state
    base_state = MathGameState()
    # Construct list of possible actions
    MathGameState.action_list.append(AcAddOne())
    MathGameState.action_list.append(AcMultiplyMinusTwo())
    MathGameState.action_list.append(AcSubtractThree())
    # Return base state
    return base_state
