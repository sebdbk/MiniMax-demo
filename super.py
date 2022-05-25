# Contains Super classes that will be used in different case files
class EnvState:
    # A state of the environment
    # Contains two agents and a board_state
    def __init__(self):
        self.agent1 = Agent("Player 1")
        self.agent2 = Agent("Player 2")


class Agent:
    def __init__(self, name):
        self.name = name


class BoardState:
    # An abstract method for the various shared environments in the test cases
    # Represents the "board" in front of the agents
    def __init__(self):
        pass

    def get_reward(self):
        # gets the estimated 'reward' of the current state
        # positive rewards benefit Player 1, negative benefit Player 2
        pass


class Action:
    # An action that can be taken by the Agent.
    # It can be conditional and usually impacts the BoardState
    def __init__(self):
        pass

    def can_be_performed(self, agent, boardstate):
        return True

    def perform(self, agent, boardstate):
        pass
