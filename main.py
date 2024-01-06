# main.py

import maze_generator
import path_finder
import time

if __name__ == "__main__":
    while True:
        print('Hey there! How would you like to proceed further?')
        print('1. Generate a Maze 🐀 and Start Finding Path 🛣️')
        print('2. Exit the Program 🥲')

        choice = int(input('Choose an Option (1 or 2): '))

        if choice == 1:
            maze_size = int(input('Enter the size of the Maze: '))
            maze = maze_generator.generate_maze(maze_size)

            print('\nGenerated Maze:')
            for row in maze:
                print(" ".join(row))

            print('\nWait! Generating Path ⌛')
            time.sleep(3)

            path = path_finder.find_path(maze)

            if path:
                print('\nFound Path:')
                for row in path:
                    print(" ".join(row))
            else:
                print('\nNo Valid Path Found. Please Try Again 😓')
        
        elif choice == 2:
            print('\nBye Bye 👋🏻')
            break

        else:
            print('\nInvalid Input. Please Choose Among the Given Options 🤷🏻‍♂️')
