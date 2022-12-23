import time
import os

class node:
    def __init__(self, parent=None, position=None):
        self.G = 0
        self.H = 0
        self.F = 0
        self.parent = parent
        self.pos = position

    def __eq__(self, other):
        return self.pos == other.pos

def solveMaze_astar(maze, cost, start, end):
    first_node = node(None, tuple(start))
    last_node = node(None, tuple(end))
    first_node.G = first_node.H = first_node.F = 0
    last_node.G = last_node.H = last_node.F = 0
    left_to_visit = []
    visited_nodes = []
    left_to_visit.append(first_node)
    iter = 0
    max_iter = (len(maze) // 2) ** 10
    step  =  [[-1, 0 ], 
              [ 0, -1], 
              [ 1, 0 ],
              [ 0, 1 ]] 
    height, width = len(maze), len(maze[0])
    while len(left_to_visit) > 0 :
        iter += 1
        cur_node = left_to_visit[0]
        cur_index = 0
        for i, j in enumerate(left_to_visit):
            if j.F < cur_node.F:
                cur_node = j
                cur_index = i
        if cur_node.pos == end:
            return True, len(visited_nodes)
        if iter > max_iter:
            return False, len(visited_nodes)
        left_to_visit.pop(cur_index)
        visited_nodes.append(cur_node)
        if maze[cur_node.pos[0]][cur_node.pos[1]] != 4 and maze[cur_node.pos[0]][cur_node.pos[1]] !=5:
            maze[cur_node.pos[0]][cur_node.pos[1]] = 8
            time.sleep(0.04)
            os.system('cls')
            printMaze(maze)
        children_list = []
        for new_pos in step:
            node_pos = (cur_node.pos[0] + new_pos[0], cur_node.pos[1] + new_pos[1])
            if (node_pos[0] > (height - 1) or
                node_pos[0] < 0 or
                node_pos[1] > (width -1) or
                node_pos[1] < 0):
                continue
            if maze[node_pos[0]][node_pos[1]] != 0 and maze[node_pos[0]][node_pos[1]] != 4 and maze[node_pos[0]][node_pos[1]] != 5:
                continue
            temp_node = node(cur_node, node_pos)
            children_list.append(temp_node)
        for child_node in children_list:
            if len([child_visited for child_visited in visited_nodes if child_visited == child_node]) > 0:
                continue
            child_node.H = (abs((child_node.pos[0] - last_node.pos[0])) +
                            abs((child_node.pos[1] - last_node.pos[1])))
            child_node.G = cur_node.G + cost
            child_node.F = child_node.G + child_node.H
            if len([k for k in left_to_visit if child_node == k and child_node.G > k.G]) > 0:
                continue
            left_to_visit.append(child_node)

def readMaze():
    with open('astar/Maze.txt') as file:
        maze_txt = file.read()
    maze_lines = maze_txt.split('\n')
    maze_array = []
    for i in maze_lines:
        maze_array.append([int(item) for item in i])
    return maze_array

def printMaze(maze):
    print("# - пройдений шлях")
    for lines in maze:
        for ch in lines:
            if ch == 4:
                print('S', end =''),
            elif ch == 5:
                print('E', end =''),
            elif ch == 8 :
                print('#', end =''),
            elif ch == 1:
                print('|', end =''),
            else:
                print(' ', end =''),
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