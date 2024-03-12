from random import randint, random

def construct_highway(number_of_cells, frequency, initial_speed, random_frequency=False, random_speed=False, max_speed=5):
    """
    Constructs the initial state of the highway.
    """
    highway = [-1] * number_of_cells
    position = 0
    while position < number_of_cells:
        speed = randint(0, max_speed) if random_speed else initial_speed
        highway[position] = min(max(speed, 0), max_speed)  # Ensure speed is within bounds
        position += randint(1, frequency) if random_frequency else frequency
    return highway

def get_distance(highway, car_index):
    """
    Calculates the distance to the next car ahead, considering the highway's loop nature.
    """
    distance = 1
    while distance < len(highway):
        if highway[(car_index + distance) % len(highway)] != -1:
            break
        distance += 1
    return distance

def update(highway, probability, max_speed):
    """
    Updates the speed of each car based on the Nagel-Schreckenberg model.
    """
    new_highway = [-1] * len(highway)
    for i, speed in enumerate(highway):
        if speed != -1:
            distance = get_distance(highway, i)
            # Acceleration
            speed = min(speed + 1, max_speed, distance - 1)
            # Random slowing down
            if random() < probability:
                speed = max(speed - 1, 0)
            # Move car to new position
            new_position = (i + speed) % len(highway)
            new_highway[new_position] = speed
    return new_highway

def simulate(initial_highway, number_of_updates, probability, max_speed):
    """
    Simulates the highway traffic for a given number of updates.
    """
    history = [initial_highway]
    for _ in range(number_of_updates):
        new_highway = update(history[-1], probability, max_speed)
        history.append(new_highway)
    return history

# Example usage
if __name__ == "__main__":
    initial_highway = construct_highway(number_of_cells=100, frequency=5, initial_speed=2)
    simulation_history = simulate(initial_highway, number_of_updates=10, probability=0.1, max_speed=5)
    for state in simulation_history:
        print(state)
