from .functions_ldfs import *
def LDFS():
    try:
        maze = readMaze()
        first_node = findPosition(maze, 4)
        last_node = findPosition(maze, 5)
        flag, path=solveMaze_ldfs(maze,first_node,last_node)
        if(flag==True):
            os.system("cls")
            print("LDFS algorithm:")
            printMaze(maze,first_node,last_node)
            print("The maze was completed successfully")
            print("Number of steps taken: ", path)
        else:
            print("The path could not be found")
            print("Number of steps taken: ", path)
    except TypeError:
        print("The path could not be found")
        return 'Type'
    
