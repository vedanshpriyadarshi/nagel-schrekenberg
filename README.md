### Overview

This code simulates the flow of traffic on a circular highway where each segment of the road can either be empty or occupied by a car with a certain speed. The simulation is based on the Nagel-Schreckenberg model, a cellular automaton model for freeway traffic. It takes into account acceleration, braking due to other cars, and random events such as sudden braking.

### Functions

#### `construct_highway(number_of_cells, frequency, initial_speed, random_frequency=False, random_speed=False, max_speed=5)`

- **Purpose**: Constructs the initial state of the highway.
- **Parameters**:
  - `number_of_cells` (int): The total number of cells (segments) in the highway.
  - `frequency` (int): The initial spacing between cars.
  - `initial_speed` (int): The initial speed of cars.
  - `random_frequency` (bool, optional): If True, cars are placed at random intervals up to `frequency`. Defaults to False.
  - `random_speed` (bool, optional): If True, cars have random initial speeds up to `max_speed`. Defaults to False.
  - `max_speed` (int, optional): The maximum speed a car can have. Defaults to 5.
- **Returns**: A list representing the highway, where `-1` indicates an empty cell and other values (0 to `max_speed`) represent the speeds of cars.

#### `get_distance(highway, car_index)`

- **Purpose**: Calculates the distance to the next car ahead, considering the circular nature of the highway.
- **Parameters**:
  - `highway` (list): The current state of the highway.
  - `car_index` (int): The index of the current car in the highway list.
- **Returns**: The distance (number of cells) to the next car ahead.

#### `update(highway, probability, max_speed)`

- **Purpose**: Updates the speed of each car for a single time step based on the Nagel-Schreckenberg model.
- **Parameters**:
  - `highway` (list): The current state of the highway.
  - `probability` (float): The probability of a car randomly slowing down.
  - `max_speed` (int): The maximum speed cars can reach.
- **Returns**: A new list representing the state of the highway after updating the speeds and positions of cars.

#### `simulate(initial_highway, number_of_updates, probability, max_speed)`

- **Purpose**: Simulates the traffic flow on the highway for a given number of time steps.
- **Parameters**:
  - `initial_highway` (list): The initial state of the highway.
  - `number_of_updates` (int): The number of time steps to simulate.
  - `probability` (float): The probability of a car randomly slowing down.
  - `max_speed` (int): The maximum speed cars can reach.
- **Returns**: A list of lists, where each inner list represents the state of the highway at each time step.

### Example Usage

```python
# Set up the initial conditions
number_of_cells = 100
frequency = 5
initial_speed = 2
max_speed = 5
probability = 0.1
number_of_updates = 10

# Construct the initial highway
initial_highway = construct_highway(number_of_cells, frequency, initial_speed)

# Simulate the traffic flow
simulation_history = simulate(initial_highway, number_of_updates, probability, max_speed)

# Print the simulation results
for step, state in enumerate(simulation_history):
    print(f"Step {step}: {state}")
```
