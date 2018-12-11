import time

class Node:


    def __init__(self, G=0, H=0, parent=None, location=None):

        self.G = G
        self.H = H
        self.F = self.G + self.H
        self.parent = parent
        self.location = location

# import numpy as np

class Astar:


    DIR = {
        (-1, 1): 14,
        (0, 1): 10,
        (1, 1): 14,
        (1, 0): 10,
        (1, -1): 14,
        (0, -1): 10,
        (-1, -1): 14,
        (-1, 0):10
    }


    def __init__(self, maze_map, start, goal):
        self.maze_dict = dict()
        self.maze_map = maze_map
        self.opened_list = list()
        self.closed_list = list()
        self.barrier_list = list()
        self.START = Node(location=start)
        self.GOAL = Node(location=goal)
        self.path = list()
        self.CUR = Node()


    def encode_map(self):
        # 외곽벽 추가
        EXIT_ROW = len(self.maze_map)    # 행의 갯수
        EXIT_COL = len(self.maze_map[0]) # 열의 갯수
        for row in self.maze_map:        # 첫번째열 마지막열 1로 채운다
            row.insert(0, 1)
            row.append(1)
        added_row = [1 for _ in range(EXIT_COL+2)]  # 첫번째행, 마지막행 1로 채운다
        self.maze_map.insert(0, added_row)
        self.maze_map.append(added_row)
        # x,y 좌표 직관적으로 바꾸기
        # maze_dict location node 할당
        for y in range(len(maze_map)-1, -1, -1):
            y_loc = len(maze_map) - (y+2)
            for x, value in enumerate(maze_map[y]):
                x_loc = x - 1
                self.maze_dict[(x_loc,y_loc)] = Node(location =(x_loc,y_loc))
                if value == 1:
                    self.barrier_list.append((x_loc, y_loc))
        self.init_barrier = self.barrier_list


    def start_goal(self):
        start_location = self.START.location
        goal_location = self.GOAL.location
        # START G,H value
        G = 0
        H = abs((goal_location[0]-start_location[0]) + (goal_location[1]-start_location[1])) * 10
        # START NODE H value
        self.START.H = H
        # START NODE and GOAL NODE maze dict에 할당
        self.maze_dict[start_location] = self.START
        self.maze_dict[goal_location] = self.GOAL


    def search_around(self, NODE):
        # 일단 search하는 중심 노드는 closed_list에 추가
        if NODE.location not in self.closed_list:
            self.closed_list.append(NODE.location)
        # 주변 노드 좌표 리스트 생성
        around_nodes = [(i[0][0] + i[1][0], i[0][1] + i[1][1]) for i in zip(self.DIR.keys(), [list(NODE.location) for _ in range(8)])]

        for i in around_nodes:
            if not self.maze_dict[i].parent:
                self.maze_dict[i].parent = NODE.location
#             print("i", i, "cur", self.CUR.location, "parent", self.maze_dict[i].parent)
            #self.calculate(self.maze_dict[i])

        return around_nodes


    def astar_algorithm(self, cur_around):
        for i in cur_around:
            if i in self.opened_list:
                new_G = self.CUR.G + self.DIR[(self.maze_dict[i].location[0]\
                        - self.CUR.location[0], self.maze_dict[i].location[1] - self.CUR.location[1])]
                old_G = self.maze_dict[i].G
                if new_G >= old_G:
                    continue
                else:
                    self.maze_dict[i].parent = self.CUR.location
                    self.calculate(self.maze_dict[i])
            elif (i in self.closed_list) | (i in self.barrier_list):
                continue
            else:
                self.calculate(self.maze_dict[i])
                self.push_open(i)


    def calculate(self, NODE):
        '''
        parameter : NODE - Node() 자료구조
        return : 없음 - NODE 객체 안에 data (F, G, H)를 변경
        NODE 가 들어왔을 때, 그 G, H, F 를 계산하여, 다시 해당 NODE.G, NODE.H, NODE.F에
        할당해 줍니다.
        NODE.G 의 경우, 부모로부터 온 방향을 찾아 DIR dictionary 에서 10 혹은 14 값을 받아, 부모의 G 값에서 더합니다.
        NODE.H 의 경우, self.GOAL 까지의 거리 입니다. 이 거리는 Manhattan Path Scoring 방법을 사용합니다.
        NODE.F 의 경우, NODE.G와 NODE.H를 더합니다.
        '''
        #Testing 을 클래스 밖에서 간단하게 해서 잘 돌아갔으나, class 안에서 다시한번 해볼 필요가 있습니다.
        #NODE 가 부모로부터 어느 방향으로부터 왔는가
        #이것을 알아야 10을 더할지 14를 더할지 DIR 에서 선택할 수 있다.
        direction = NODE.location[0] - NODE.parent[0], NODE.location[1] - NODE.parent[1]
        #G 값계산
        NODE.G = self.maze_dict[NODE.parent].G + self.DIR[direction]
        #H 값계산
        NODE.H = (abs(self.GOAL.location[0] - NODE.location[0]) + \
        abs(self.GOAL.location[1] - NODE.location[1])) * 10
        #F 값계산
        NODE.F = NODE.G + NODE.H


    def push_open(self, my_location):
        self.opened_list.append(my_location)

    def sorting_open(self):
        self.opened_list = sorted(self.opened_list, key=lambda x: self.maze_dict[x].F, reverse=True)


    def maze_solver(self):
        self.encode_map()  # self.maze_map 생성
        self.start_goal()  # start, goal 노드 생성 완료
        self.CUR = self.START   # CUR를 START 노드로 설정 완료
        cur_around = self.search_around(self.CUR) # start의 search_around
        while self.GOAL.location not in cur_around:
            self.astar_algorithm(cur_around)
            self.sorting_open()

            if len(self.opened_list) != 0:
                self.CUR = self.maze_dict[self.opened_list.pop()]
                cur_around = self.search_around(self.CUR)


        self.GOAL.G = self.CUR.G + self.DIR[self.GOAL.location[0] - self.CUR.location[0],\
                                            self.GOAL.location[1] - self.CUR.location[1]]
        self.GOAL.parent = self.CUR.location

        self.path.append(self.GOAL.location)

        while self.CUR.location != self.START.location:
            self.path.append(self.maze_dict[self.path[-1]].parent)
            self.CUR = self.maze_dict[self.CUR.parent]

        self.path.reverse()

        self.path.insert(0, self.START.location)
        return self.path, self.GOAL.G

x = 6
y = 8

# maze_map = [[0 for _ in range(x)] for _ in range(y)] # list comprehension
# maze_map = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0],
#             [0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
#             [0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0],
#             [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
#             [0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0],
#             [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#             [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],]
maze_map = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0],
            [0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0],
            [0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0],
            [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0],
            [0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0],
            [0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0],
            [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],]
init_maze_map_x = len(maze_map[0])
init_maze_map_y = len(maze_map)

start = (0, 0)
goal = (17, 20)

maze = Astar(maze_map, start, goal)
paths, G = maze.maze_solver()

w = 30 # width of each cell


def setup():
    size(w * init_maze_map_x, w * init_maze_map_y)

# def mousePressed():
#     maze_map[mouseY/w][mouseX/w] = -1 * maze_map[mouseY/w][mouseX/w]
#     # integer division is good here!

def draw():
    vv_start_x = init_maze_map_y - start[1]
    vv_start_y = start[0] + 1
    vv_goal_x = init_maze_map_y - goal[1]
    vv_goal_y = goal[0] + 1
    maze.maze_map[vv_start_x][vv_start_y] = -1
    maze.maze_map[vv_goal_x][vv_goal_y] = -1


    # if mousePressed:
    #     fill(0)

    x, y = 0, 0 # starting position

    for path in paths[1:-1]:
        vv_path_x = init_maze_map_y - path[1]
        vv_path_y = path[0] + 1
        maze.maze_map[vv_path_x][vv_path_y] = 2

    for row_idx in range(1, init_maze_map_y + 1):
        for col_idx in range(1, init_maze_map_x + 1):
            if maze.maze_map[row_idx][col_idx] == 1:
                fill(250,0,0)
                rect(x, y, w, w)
            elif maze.maze_map[row_idx][col_idx] == -1:
                fill(0, 250, 0)
                rect(x, y, w, w)
            elif maze.maze_map[row_idx][col_idx] == 2:
                fill(0, 0, 250)
                rect(x, y, w, w)
            else:
                fill(255)
                rect(x, y, w, w)
            x = x + w  # move right
        y = y + w # move down
        x = 0 # rest to left edge
