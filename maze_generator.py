import random

def User_Input():
    num = int(input("Enter the Size of the Maze you Want to Generate: "))
    return num

maze_size = User_Input()

def insert_walls(maze_size, maze):
    # Inserting Walls by choosing random column number in each row one by one
    for _ in range(maze_size):
        for _ in range(maze_size):
            row, col = random.randint(0, maze_size-1), random.randint(0, maze_size-1)
            if (row == 0 and col == 0) or (row == maze_size-1 and col == maze_size-1): continue
            else:
                maze[row][col] = ' 🧱  |'
                
# Generating Initial Maze
def generated_maze():
    # Declaring the global variable to get the size of the maze
    global maze_size

    maze = [[' 🔵  |' for i in range(maze_size)] for _ in range(maze_size)]

    insert_walls(maze_size, maze)

    # Initializing the Satarting and the ending point
    maze[0][0], maze[maze_size-1][maze_size-1] = ' 🐭  |', ' 🏁  |'
    
    return maze
