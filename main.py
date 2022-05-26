# Main file

# Here, set up the main framework, the AI, and the test case
# Then, run it and communicate with the user

import case1
import minimax
import time

current_state = case1.set_up()
print("Processing optimal game of 10 moves")
t = time.process_time()
while not current_state.is_finished():
    next_move = minimax.expand_state_not_optimised(current_state)
    next_agent = current_state.next_turn()
    next_move[1].perform(next_agent, current_state.boardstate)
    # next_move[1].print(next_agent, current_state.boardstate)
    # print("Score is now " + str(current_state.boardstate.score))
print("Unoptimised: Time taken: " + str(time.process_time() - t) + "s")

# Re-attempt with Alfa Beta Pruning
current_state = case1.set_up()
t = time.process_time()
while not current_state.is_finished():
    next_move = minimax.expand_state_a_b_pruned(current_state)
    next_agent = current_state.next_turn()
    next_move[1].perform(next_agent, current_state.boardstate)
    # next_move[1].print(next_agent, current_state.boardstate)
    # print("Score is now " + str(current_state.boardstate.score))
print("Optimised: Time taken: " + str(time.process_time() - t) + "s")
