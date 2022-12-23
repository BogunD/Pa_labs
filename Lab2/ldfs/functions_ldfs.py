import time
import os
def solveMaze_ldfs(maze,  start, end):
    if start is None or end is None:
        return
    left_to_visit = [start]
    visited_nodes = [start]
    iter = 0
    step  =  [(-1, 0 ), 
              ( 0, -1), 
              ( 1, 0 ), 
              ( 0, 1 )] 
    height, width = len(maze), len(maze[0])
    solution = [start]
    limit = 500
    while len(left_to_visit) > 0 and iter<limit:
        cur_node = left_to_visit.pop()
        if (cur_node == end):
            break
        for new_pos in step:
            node_pos = (cur_node[0] + new_pos[0],cur_node[1] + new_pos[1] )
            if (node_pos[0] > (height ) or
                node_pos[0] < 0 or
                node_pos[1] > (width ) or
                node_pos[1] < 0):
                continue
            if maze[node_pos[0]][node_pos[1]] != 0 and maze[node_pos[0]][node_pos[1]] != 4 and maze[node_pos[0]][node_pos[1]] != 5:
                continue
            if node_pos in visited_nodes:
                continue
            visited_nodes.append(node_pos)
            maze[node_pos[0]][node_pos[1]] = 8
            printMaze(maze, start, end)
            time.sleep(0.04)
            os.system("cls")
            left_to_visit.append(node_pos)
            solution.append(node_pos)
    if(end not in visited_nodes):
        return False, len(visited_nodes)
    printMaze(maze, start, end)
    return True, len(visited_nodes)

def readMaze():
    with open('ldfs\Maze.txt') as file:
        maze_txt = file.read()
    maze_lines = maze_txt.split('\n')
    maze_array = []
    for i in maze_lines:
        maze_array.append([int(item) for item in i])
    return maze_array

def printMaze(maze, start, end):
    i = 0
    j = 0
    for lines in maze:
        for ch in lines:
            if (i,j) == start:
                print('S', end =''),
            elif (i,j) == end:
                print('E', end =''),
            elif ch == 8 :
                print('#', end =''),
            elif ch == 1:
                print('|', end =''),
            else:
                print(' ', end =''),
            j+=1
        i+=1
        j = 0
        print('')

def findPosition(maze, num):
    i = 0
    j = 0
    for lines in maze:
        i+=1
        for ch in lines:
            j+=1
            if ch == num:
                return(i-1, j-1)
        j = 0


