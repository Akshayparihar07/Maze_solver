import random 
import time

def generate_maze(n):
    maze = [["🔹 |"]*n for _ in range(n)]
    for _ in range(n):
        i, j = random.randint(0, n-1), random.randint(0, n-1)
        if (i==0 and j==0) or (i==n-1 and j==n-1): 
            continue
        else: 
            maze[i][j] = "🧱 |" 
        i, j = random.randint(0, n-1), random.randint(0, n-1)
        if (i==0 and j==0) or (i==n-1 and j==n-1): 
            continue
        else: 
            maze[i][j] = "🧱 |" 
        i, j = random.randint(0, n-1), random.randint(0, n-1)
        if (i==0 and j==0) or (i==n-1 and j==n-1): 
            continue
        else: 
            maze[i][j] = "🧱 |" 
        i, j = random.randint(0, n-1), random.randint(0, n-1)
        if (i==0 and j==0) or (i==n-1 and j==n-1): 
            continue
        else: 
            maze[i][j] = "🧱 |" 
        i, j = random.randint(0, n-1), random.randint(0, n-1)
        if (i==0 and j==0) or (i==n-1 and j==n-1): 
            continue
        else: 
            maze[i][j] = "🧱 |" 
    return maze

def print_maze(grid, n):
    grid[0][0], grid[n-1][n-1] = ' S |', ' E |'
    for i in range(n):
        print('-+'*(n*2))
        for j in range(n):
            print(grid[i][j], end = '')
        print()
    print('-+'*(n*2))

def find_path(i, j, n, maze):
    if i == n-1 and j == n-1:
        return True
    if maze[i][j] == "🔹 |" or maze[i][j] == " S |" or maze[i][j] == " E |":
        maze[i][j] = "🟢 |"
        if j + 1 < n and find_path(i, j + 1, n, maze):
            return True
        elif i + 1 < n and find_path(i + 1, j, n, maze):
            return True
        elif j - 1 >= 0 and find_path(i, j-1, n, maze):
            return True
        elif i - 1 >= 0 and find_path(i, j-1, n, maze):
            return True
        maze[i][j] = "🔹 |"
    return False

def print_path(path,n):
    path[0][0], path[n-1][n-1] = "🎌 |", "🚩 |"
    for i in range(n):
        print('-+'*(n*2))
        for j in range(n):
            print(path[i][j], end = '')
        print()
    print('-+'*(n*2))
    

if __name__=="__main__":
    print('WELCOME, YOU HAVE THE FOLLOWING OPTIONS')
    print('\nOPTION 1 : GENERATE A MAZE AND START FINDING A PATH')
    print('OPTION 2 : EXIT THE PROGRAM!')
    choice = int(input("\nHOW WOULD YOU LIKE TO PROCEED? (1/2): "))

    if choice == 1:
        n = int(input('\nEnter Maze Size: '))
        maze = generate_maze(n)
        print_maze(maze, n)
        if find_path(0, 0, n, maze):
            print("\nWAIT, FINDING PATH....")
            time.sleep(2)
            print("\nPATH EXIST, SOLUTION: ")
            print_path(maze, n)
        else:
            print("\nSORRY, NO PTH EXIST!")
    else:
        print('\nOKAY, BYE!')







