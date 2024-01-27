import random 
import time

OPEN = "🔹 |"
VISITED = "🟢 |"
WALL = "🧱 |"
START = " S |"
END = " E |"

def generate_maze(n, wall_percentage):
    maze = [[OPEN]*n for _ in range(n)]
    num_walls = int(n*n*wall_percentage/100)
    for _ in range(num_walls):
            i, j = random.randint(0, n-1), random.randint(0, n-1)
            if (i==0 and j==0) or (i==n-1 and j==n-1): 
                continue
            else: 
                maze[i][j] = WALL 
    return maze

def print_maze(maze, n):
    maze[0][0], maze[n-1][n-1] = START, END
    for i in range(n):
        print('-+'*(n*2))
        for j in range(n):
            print(maze[i][j], end = '')
        print()
    print('-+'*(n*2))

def find_path(i, j, n, maze):
    if i == n-1 and j == n-1:
        maze[i][j] = VISITED
        return True
    if maze[i][j] == OPEN or maze[i][j] == START or maze[i][j] == END:
        maze[i][j] = VISITED
        if i+1 < n and find_path(i+1, j, n, maze):
            return True
        elif j+1 < n and find_path(i, j+1, n, maze):
            return True
        elif i-1 >= 0 and find_path(i-1, j, n, maze):
            return True
        elif j-1 >= 0 and find_path(i, j-1, n, maze):
            return True
        maze[i][j] = OPEN
    return False

def print_path(path,n):
    for i in range(n):
        print('-+'*(n*2))
        for j in range(n):
            print(path[i][j], end = '')
        print()
    print('-+'*(n*2))
    
def main():
    n = int(input('\nWHAT SIZE OF MAZE DO YOU WANT TO GENERATE(NxN): '))
    wall_percentage = int(input('\nHOW MANY HURDLES DO YOU WANT IN YOUR MAZE:(IN %): '))
    if wall_percentage > 25: wall_percentage = 25
    maze = generate_maze(n, wall_percentage)
    print_maze(maze, n)
    keypress = input('\nPRESS ENTER TO GENERATE MAZE')
    if keypress == '':
        if find_path(0, 0, n, maze):
            print("\nWAIT, FINDING PATH....")
            time.sleep(2)
            print("\nPATH FOUND✅")
            print_path(maze, n)
        else:
            print("\nSORRY, NO PATH EXIST!")
    else:
        print('\nTHANKS FOR PLAYING🫂')

if __name__=="__main__":
        main()
        while True:
            print('\nWHAT DO YOU WANNA DO NEXT?')
            print('\nOPTION 1 : GENERATE A MAZE AND START FINDING A PATH')
            print('OPTION 2 : EXIT THE PROGRAM!')
            choice = int(input("\nHOW WOULD YOU LIKE TO PROCEED? (1/2): "))
            if choice == 1:
                main()
            else:
                print('\nOKAY, BYE!')
                break







