import copy
# Contains Super classes that will be used in different case files


class EnvState:
    # A state of the environment
    # Contains two agents and a board_state
    def __init__(self):
        self.agent1 = None
        self.agent2 = None
        self.boardstate = None

    def possible_actions(self, agent):
        return []

    def next_turn(self):
        return self.agent1

    def start_clean(self):
        self.agent1 = Agent("Player 1", True)
        self.agent2 = Agent("Player 2", False)
        self.boardstate = BoardState()

    def copy(self):
        return EnvState()

    def is_finished(self):
        return self.boardstate.is_finished()


class Agent:
    # Has a name and a boolean that determines if the Agent works for Max or Min reward
    def __init__(self, name, if_max):
        self.name = name
        self.plays_for_max = if_max


class BoardState:
    # An abstract method for the various shared environments in the test cases
    # Represents the "board" in front of the agents
    def __init__(self):
        pass

    def get_reward(self):
        # gets the estimated 'reward' of the current state
        # positive rewards benefit Player 1, negative benefit Player 2
        return 0

    def is_finished(self):
        # tells whether any further moves can be made
        return True


class Action:
    # An action that can be taken by the Agent.
    # It can be conditional and usually impacts the BoardState
    def __init__(self):
        pass

    def can_be_performed(self, agent, boardstate):
        return True

    def perform(self, agent, boardstate):
        pass
