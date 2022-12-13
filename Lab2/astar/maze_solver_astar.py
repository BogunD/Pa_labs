from .functions_astar import *

def A_star():
    try:
        maze = readMaze()
        first_node = findPosition(maze, 4)
        last_node = findPosition(maze, 5)
        cost = 1
        flag,path = solveMaze_astar(maze,cost,first_node,last_node)
        os.system('cls')
        print("A* алгоритм")
        printMaze(maze)
        if flag == True:
            print("Лабіринт пройдено успішно")
            print("Кількість пройдених кроків: ", path);
        else:
            print("Не вдалося знайти шлях")
            print("Кількість пройдених кроків: ", path);
    except TypeError:
        print("Не вдалося знайти шлях")
        return 'Type'



