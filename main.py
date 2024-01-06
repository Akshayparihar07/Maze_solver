import maze_generator
import path_finder
import time

if __name__ == "__main__":
    while True:
        print('Hey there! How would you like to proceed further?')
        print('1. Generate a Maze🐀 and Start Finding Path🛣️')
        print('2. Exit the Program!🥲')

        choice = int(input('Choose one Option: 1 OR 2 : '))

        if choice == 1:
            maze_size = int(input('How Big do You want the Maze to be?: '))
            maze = maze_generator.generate_maze(maze_size)

            print('Generated Maze:')
            for row in maze:
                print(" ".join(row))
            
            print('Wait! Generating Path⌛')
            time.sleep(3)

            path = path_finder.find_path(maze)

            if path:
                print('Found Path:')
                for row in path:
                    print(" ".join(row))
            else:
                print('No Valid Path Found. Please Try Again😓')
                print()
                print('-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-')
                print()
        
        elif choice == 2:
            print('Bye Bye 👋🏻')
            break

        else:
            print()
            print('Invalid Input. Please Choose among the Given Options 🤷🏻‍♂️')
            print('-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-')
            print()

