from .functions_astar import *

def A_star():
    try:
        maze = readMaze()
        first_node = findPosition(maze, 4)
        last_node = findPosition(maze, 5)
        cost = 1
        flag,path = solveMaze_astar(maze,cost,first_node,last_node)
        os.system('cls')
        print("A* algorithm")
        printMaze(maze)
        if flag == True:
            print("The maze was completed successfully")
            print("Number of steps taken: ", path)
        else:
            print("The path could not be found")
            print("Number of steps taken: ", path)
    except TypeError:
        print("The path could not be found")
        return 'Type'



