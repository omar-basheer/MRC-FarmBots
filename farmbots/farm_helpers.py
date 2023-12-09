def initialize__server_world(fruit_map, grid_size):
    """
    Initializes the world grid for the server based on a provided fruit map.

    Parameters:
    - fruit_map (dict): A dictionary mapping fruit locations to their colors.
    - grid_size (int): The size of the grid.

    Returns:
    list: 2D list representing the initial state of the world for the server.
    """
    world_grid = [['empty' for _ in range(grid_size)] for _ in range(grid_size)]
    # Place fruits in the grid based on the provided fruit map
    for fruit_location, fruit_color in fruit_map.items():
        row, col = fruit_location
        # Check if the provided location is within the grid boundaries
        if 0 <= row < grid_size and 0 <= col < grid_size:
            world_grid[row][col] = "f_"+fruit_color

    return world_grid


def initialize_client_world(grid_size):
    """
    Initialize a grid representing the world for a client.

    Returns:
    - client_world (list): 2D list representing the initial state of the world for a client.
    """
    # Initialize a grid with all cells initially marked as unknown
    client_world = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
    
    return client_world

# def initialize_fruit_state(farm_space):
#     """
#     Initializes the state of fruits in the farm space.

#     Parameters:
#     - farm_space (list): 2D list representing the farm space with cell contents.

#     Returns:
#     int: The count of initialized fruits.
#     """
#     fruit_count = 0 

#     for row in range(len(farm_space)):
#         for col in range(len(farm_space[row])):
#             cell_content = farm_space[row][col]
#             if 'f' in cell_content:
#                 fruit_state[(row, col)] = {'color': cell_content.split('_')[1], 'picked': False, 'assigned_agent': None}
#                 fruit_count += 1  

#     return fruit_count

# def print_world(farm_space):
#     for row in farm_space:
#         print(" ".join(map(str, row)))

# def print_fruit_state():
#     """
#     Prints the fruit state in key-value pairs line by line.
#     """
#     print("Fruit State:")
#     for location, state in fruit_state.items():
#         print("Location: {}, Color: {}, Picked: {}, Assigned Agent: {}".format(
#             location, state['color'], state['picked'], state['assigned_agent']
#         ))