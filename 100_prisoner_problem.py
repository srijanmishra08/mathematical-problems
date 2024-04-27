"""
Problem Statement: 100 Prisoners Problem

You are a prisoner in a jail with a strange but fair warden. The warden decides to give all the prisoners a chance to escape. He places 100 prisoners in 100 numbered drawers in a room and then steps out.

The prisoners are called in one by one into the room with the drawers, but they are not allowed to communicate with each other once they enter the room.

The prisoners must follow this procedure to escape:

1. Each prisoner is assigned a unique drawer number from 1 to 100.
2. The prisoners enter the room one by one, in any order they choose.
3. Upon entering the room, a prisoner is allowed to open and close up to 50 drawers.
4. If a prisoner finds their assigned drawer number during their turn, they must announce it to the warden and leave the room immediately. If they do not find their number, they must exit the room without announcing anything.
5. Once a prisoner exits the room, the warden resets the drawers, and the process continues with the next prisoner.

The prisoners must find all their assigned drawer numbers within 100 iterations of this process, or they will all be executed.

Your task is to write a program that simulates this scenario and determines the success rate of the prisoners' strategy to escape.

"""

import random

def simulate_strategy():
    drawers = list(range(1, 101))  # List of drawer numbers
    random.shuffle(drawers)  # Randomly shuffle the drawer numbers

    for prisoner_number in range(1, 101):
        assigned_number = prisoner_number
        for _ in range(50):
            if assigned_number in drawers:
                drawers.remove(assigned_number)
                break
            assigned_number += 50
        else:
            # Prisoner did not find their number, all prisoners die
            return False
    
    # All prisoners found their number, all prisoners are pardoned
    return True

# Simulate the scenario multiple times to get the success rate of the strategy
num_simulations = 10000
success_count = sum(simulate_strategy() for _ in range(num_simulations))

success_rate = success_count / num_simulations
print(f"Success rate: {success_rate * 100:.2f}%")


"""
Optimal Strategy:

The optimal strategy for the prisoners to escape involves each prisoner checking the drawer corresponding to their assigned number in each iteration.

1. Each prisoner starts by checking the drawer corresponding to their assigned number.
2. If a prisoner finds their assigned number, they announce it to the warden and leave the room immediately.
3. If a prisoner does not find their assigned number, they exit the room without announcing anything.
4. The next prisoner follows the same procedure, checking the drawer corresponding to their assigned number.
5. This process continues until all prisoners find their assigned numbers or until 100 iterations have passed.

By following the optimal strategy, the prisoners maximize their chances of success by systematically checking the drawers in a predetermined order.

"""


def simulate_optimal_strategy():
    drawers = list(range(1, 101))  # List of drawer numbers
    prisoner_number = 1  # Start with the first prisoner

    while drawers:  # Continue until all drawers are checked
        current_drawer = prisoner_number  # Drawer number to check
        
        if current_drawer in drawers:  # If the drawer is still available
            drawers.remove(current_drawer)  # Remove the checked drawer
        else:
            return False  # Prisoner did not find their number, all prisoners die
        
        # Move to the next prisoner according to the optimal strategy
        prisoner_number = current_drawer

    return True  # All prisoners found their number, all prisoners are pardoned

# Simulate the scenario multiple times to get the success rate of the strategy
num_simulations = 10000
success_count = sum(simulate_optimal_strategy() for _ in range(num_simulations))

success_rate = success_count / num_simulations
print(f"Success rate using the optimal strategy: {success_rate * 100:.2f}%")

