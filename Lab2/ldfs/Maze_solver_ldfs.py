from .functions_ldfs import *
def LDFS():
    try:
        maze = readMaze()
        first_node = findPosition(maze, 4)
        last_node = findPosition(maze, 5)
        flag, path=solveMaze_ldfs(maze,first_node,last_node)
        if(flag==True):
            os.system("cls")
            print("LDFS:")
            printMaze(maze,first_node,last_node)
            print("Лабіринт пройдено успішно")
            print("Кількість пройдених кроків: ", path);
        else:
            printMaze(maze,first_node,last_node)
            print("Не вдалося знайти шлях")
            print("Кількість пройдених кроків: ", path);
    except TypeError:
        print("Не вдалося знайти шлях")
        return 'Type'
    
