#You are standing in front of a row of 100 closed doors, labeled from 1 to 100. 
#You then proceed to go through a series of 100 iterations, with each iteration representing the action of one person interacting with the doors according to a specific pattern.

#The pattern is as follows:
#The first person opens every door.
#The second person toggles (opens if closed, closes if open) every second door, starting from the second door (i.e., doors 2, 4, 6, ...).
#The third person toggles every third door, starting from the third door (i.e., doors 3, 6, 9, ...).
#This pattern continues with each subsequent person toggling every nth door, starting from the nth door, where n represents the person's number.
#After all 100 iterations, you are interested in determining the final state of each door. 
#If a door is open, it means it was toggled an even number of times, and if it's closed, it means it was toggled an odd number of times.

#Your task is to write a program that simulates the scenario and determines the final state of each door. 
#Once the simulation is complete, print the state of each door, indicating whether it's open or closed.

#solution
def simulate_100_doors():
    doors = [False] * 100  # Initialize all doors as closed (False)
    
    for person_number in range(1, 101):  # Iterate over each person
        for door_number in range(person_number - 1, 100, person_number):  # Iterate over doors according to the person's number
            doors[door_number] = not doors[door_number]  # Toggle the state of the door
    
    return doors

# Simulate the scenario
doors_state = simulate_100_doors()

# Print the state of each door
for i, door in enumerate(doors_state, start=1):
    print(f"Door {i}: {'Open' if door else 'Closed'}")
