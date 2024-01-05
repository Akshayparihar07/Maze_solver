import path_finder
import maze_generator

maze = maze_generator.generated_maze()
path = path_finder.find_path(maze)

def print_path():
    nonlocal path
    result = find_path(matrix)
    if result:
        for row in result:
            print(" ".join(row))
    else:
        print("No path available.")
    
