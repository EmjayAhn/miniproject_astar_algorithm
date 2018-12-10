from node import Node
import numpy as np


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


    def start_goal(self):
        start_location = self.START.location
        goal_location = self.GOAL.location

        # START G,H value
        G = 0
        H = abs((goal_location[0]-start_location[0]) + (goal_location[1]-start_location[1]))

        # START NODE H value
        self.START.H = H

        # START NODE and GOAL NODE maze dict에 할당
        self.maze_dict[start_location] = self.START
        self.maze_dict[goal_location] = self.GOAL


    def search_around(self, NODE):
        # 일단 search하는 중심 노드는 closed_list에 추가
        self.closed_list.append(NODE.location)
        # 주변 노드 좌표 리스트 생성
        around_nodes = list(map(tuple, np.array(list(Astar.DIR.keys())) + NODE.location))

        return around_nodes


    def astar_algorithm(self, CUR, cur_around):
        for i in cur_around:
            if i in self.opened_list:
                new_G = CUR.G + self.DIR[(self.maze_dict[i].location[0] - CUR.location[0], self.maze_dict[i].location[1] - CUR.location[1])]
                old_G = self.maze_dict[i].G
                if new_G >= old_G:
                    continue
                else:
                    self.maze_dict[i].parent = CUR.location
            elif (i in self.closed_list) | (i in barrier_list):
                continue
            else:
                calculate(self.maze_dict[i])
                self.push_open(i)
                self.maze_dict[i].parent = CUR.location


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


    def push_open(self, location):
        # search_around 함수와 동일하게 around_nodes 리스트 생성
        around_nodes = list(map(tuple, np.array(list(Astar.DIR.keys())) + location))

        location_NE = tuple(np.array(location) + np.array([1, 1]))
        location_NW = tuple(np.array(location) + np.array([-1, 1]))
        location_SE = tuple(np.array(location) + np.array([1, -1]))
        location_SW = tuple(np.array(location) + np.array([-1, -1]))

        diagonal_path = [location_NE, location_NW, location_SW, location_SE]
        diagonal_location_direction = [[(-1,0),(0,-1)],[(1,0),(0,-1)],[(0,1),(1,0)],[(0,1),(-1,0)]]
        print(diagonal_path)

        for location in around_nodes:
            if (location not in self.barrier_list) and (location not in self.opened_list) and (location not in diagonal_path):
                self.opened_list.append(location)

        for location in zip(diagonal_path, diagonal_location_direction):
            if tuple(np.array(location[0]) + np.array(location[1][0])) not in self.barrier_list:
                if tuple(np.array(location[0]) + np.array(location[1][1])) not in self.barrier_list:
                    self.opened_list.append(location[0])


    def sorting_open(self, opened_list):
        sort_open = [(i, self.maze_dict[i].F) for i in opened_list]
        opened_list = [j[0] for j in sorted(sort_open, key=lambda i: i[1])]
        return opened_list


    # , maze_map, start_location, goal_location
    def maze_solver(self):
        self.encode_map()  # self.maze_map 생성
        self.start_goal()  # start, goal 노드 생성 완료
        CUR = self.START   # CUR를 START 노드로 설정 완료

        cur_around = self.search_around(CUR) # start의 search_around

        while self.GOAL.location not in cur_around:
            self.astar_algorithm(CUR, cur_around)
            sorting_open(re)

        return cur_around
        # return self.GOAL.G, self.path
