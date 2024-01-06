import random

def insert_walls(maze_size, maze):
    for _ in range(maze_size):
        for _ in range(maze_size):
            row, col = random.randint(0, maze_size-1), random.randint(0, maze_size-1)
            if (row == 0 and col == 0) or (row == maze_size-1 and col == maze_size-1): continue
            else:
                maze[row][col] = ' 🧱  |'

def generate_maze(maze_size):
    maze = [[' 🔵  |' for i in range(maze_size)] for _ in range(maze_size)]
    insert_walls(maze_size, maze)
    maze[0][0], maze[maze_size-1][maze_size-1] = ' 🐭  |', ' 🏁  |'
    return maze
