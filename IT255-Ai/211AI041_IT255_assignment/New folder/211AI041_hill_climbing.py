import random

# Define the initial state of the puzzle
initial_state = ['tiger', 'monkey', 'lion', 'kangroo', 'rat', 'horse', 'elephant', 'bee']

# Define a function to evaluate the fitness of a state (lower is better)
def evaluate(state):
    fitness = 0
    for i in range(len(state)-1):
        # Compare the last letter of the first word with the first letter of the second word
        if state[i][-1] == state[i+1][0]:
            fitness += 1
    return fitness

# Define a function to generate a neighbor state
def generate_neighbor(state):
    # Swap two random adjacent words in the state
    i = random.randint(0, len(state)-2)
    state[i], state[i+1] = state[i+1], state[i]
    return state

# Define the main function to perform the Hill Climbing algorithm
def hill_climbing(initial_state):
    current_state = initial_state
    current_fitness = evaluate(current_state)
    while True:
        # Generate a random neighbor state
        neighbor_state = generate_neighbor(current_state)
        neighbor_fitness = evaluate(neighbor_state)
        # If the neighbor state is fitter, move to it
        if neighbor_fitness < current_fitness:
            current_state = neighbor_state
            current_fitness = neighbor_fitness
        # If the neighbor state is not fitter, terminate
        else:
            return current_state

# Run the algorithm and print the solution
solution = hill_climbing(initial_state)
print(solution)
