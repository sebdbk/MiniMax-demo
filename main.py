# Main file

# Here, set up the main framework, the AI, and the test case
# Then, run it and communicate with the user

import case1
import minimax

current_state = case1.set_up()
print("Score starts at " + str(current_state.boardstate.score))
while not current_state.is_finished():
    next_move = minimax.expand_state(current_state)
    next_agent = current_state.next_turn()
    next_move[1].perform(next_agent, current_state.boardstate)
    next_move[1].print(next_agent, current_state.boardstate)
    print("Score is now " + str(current_state.boardstate.score))

