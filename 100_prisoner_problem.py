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

