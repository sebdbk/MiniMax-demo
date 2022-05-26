import super
import copy


def expand_state(state, it_left=-1):
    # RETURNS: [int, Action] - the predicted reward of the state and the Action that leads to it
    # MiniMax with a limit on the number of moves in the future it can 'look at'
    # it_left - int, decreases with every recursion
    acting_agent = state.next_turn()
    actions = state.possible_actions(acting_agent)
    if it_left == 0 or state.is_finished() or len(actions) == 0:
        # No further actions allowed - return the current reward
        return [state.boardstate.get_reward(), None]
    else:
        # Apply all possible actions and get a list of possible next states
        child_state_rewards = []
        for a in actions:
            new_state = state.copy()
            a.perform(acting_agent, new_state.boardstate)
            # Decrease iterations left, but only if it is a positive value
            # it_left=-1 means unlimited iterations, so in that case leave it as it
            if it_left > 0:
                new_it = it_left - 1
            else:
                new_it = -1
            expanded_result = expand_state(new_state, new_it)
            child_state_rewards.append([expanded_result[0], a])
        # All child states have been expanded, their rewards collected in a list
        # Find the optimal next action
        opt_action = child_state_rewards[0]
        for res in child_state_rewards:
            if acting_agent.plays_for_max:
                # Search for max
                if res[0] > opt_action[0]:
                    opt_action = res
            else:
                # Search for min
                if res[0] < opt_action[0]:
                    opt_action = res
        return opt_action

