"""
Problem Statement: Monty Hall Problem

You are a contestant on a game show where there are three doors. Behind one door is a car, and behind the other two doors are goats. 
You must choose one door initially. After you make your choice, the host, who knows what's behind each door, opens one of the other two doors to reveal a goat. 
At this point, you are given the option to switch your choice to the other unopened door. 
Write a program to simulate this scenario and determine whether it's advantageous for you to switch doors.

Optimal Strategy:
The optimal strategy in the Monty Hall problem is to always switch doors after the host reveals a goat behind one of the other doors. 
This strategy maximizes the probability of winning the car, as counterintuitive as it may seem.
"""

import random

def monty_hall_simulation(num_trials):
    """
    Simulate the Monty Hall problem for a given number of trials and determine the success rate.
    """
    switch_wins = 0
    stay_wins = 0
    
    for _ in range(num_trials):
        doors = ['goat', 'goat', 'car']
        random.shuffle(doors)
        
        # Contestant's initial choice
        initial_choice = random.choice([0, 1, 2])
        
        # Host reveals a goat behind one of the other doors
        for door in range(3):
            if door != initial_choice and doors[door] == 'goat':
                revealed_goat = door
                break
        
        # Contestant switches their choice
        switched_choice = [x for x in range(3) if x != initial_choice and x != revealed_goat][0]
        
        # Check if the switched choice wins
        if doors[switched_choice] == 'car':
            switch_wins += 1
        
        # Check if the initial choice wins
        if doors[initial_choice] == 'car':
            stay_wins += 1
    
    # Calculate success rates
    switch_success_rate = switch_wins / num_trials
    stay_success_rate = stay_wins / num_trials
    
    return switch_success_rate, stay_success_rate

# Number of trials
num_trials = 10000

# Run simulation
switch_success_rate, stay_success_rate = monty_hall_simulation(num_trials)

# Print results
print(f"Success rate with switching doors: {switch_success_rate * 100:.2f}%")
print(f"Success rate without switching doors: {stay_success_rate * 100:.2f}%")
