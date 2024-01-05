if __name__=="__main__":
    while True:
        print('Hey there! How would you like to proceed furhter?')
        print('1. Genrate a New Maze🐀')
        print('2. Print the Path🛣️')
        print('3. Exit the game!🥲')
        choice = int(input('Choose one Option: 1 / 2 / 3: '))

        if choice == 1 :
            import maze_printer
            maze_printer.print_maze()

        elif choice == 2:
            import path_printer
            path_printer.print_path()

        elif choice == 3:
            break


