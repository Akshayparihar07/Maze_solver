from maze_generator import generated_maze

maze = generated_maze()
size = len(maze)

for i in range(size):
    for j in range(size):
        print(maze[i][j], end = " ")
    print()
