# Main file

# Here, set up the main framework, the AI, and the test case
# Then, run it and communicate with the user

import case1
import minimax

base_state = case1.set_up()
for n in range(1, 7):
    result = minimax.expand_state(base_state, n)
    print("Optimal move for prediction of {}:".format(n))
    result[1].print(base_state.agent1, base_state.boardstate)

