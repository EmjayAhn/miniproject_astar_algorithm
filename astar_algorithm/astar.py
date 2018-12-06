# from node import Node
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


    def encode_map(self, maze_map):
        pass


    def search_around(self, NODE):

        # 일단 search하는 중심 노드는 closed_list에 추가
        self.closed_list.append(NODE.location)

        # 주변 노드 좌표 리스트 생성
        around_nodes = list(map(tuple, np.array(list(Astar.DIR.keys())) + NODE.location))

        # 좌표가 음수인 노드까지 찾는 경우 빼줌 (지도를 벗어나는 경우)
        around_nodes = [i for i in around_nodes if ((i[0] >= 0) and (i[1] >= 0))]

        return around_nodes


    def astar_algorithm(self, CUR, cur_around):
        pass


    def calculate(NODE):
        ```
        parameter : NODE - Node() 자료구조
        return : 없음 - NODE 객체 안에 data (F, G, H)를 변경

        NODE 가 들어왔을 때, 그 G, H, F 를 계산하여, 다시 해당 NODE.G, NODE.H, NODE.F에
        할당해 줍니다.
        NODE.G 의 경우, 부모로부터 온 방향을 찾아 DIR dictionary 에서 10 혹은 14 값을 받아, 부모의 G 값에서 더합니다.
        NODE.H 의 경우, self.GOAL 까지의 거리 입니다. 이 거리는 Manhattan Path Scoring 방법을 사용합니다.
        NODE.F 의 경우, NODE.G와 NODE.H를 더합니다.
        ```
        #Testing 을 클래스 밖에서 간단하게 해서 잘 돌아갔으나, class 안에서 다시한번 해볼 필요가 있습니다.

        #NODE 가 부모로부터 어느 방향으로부터 왔는가
        #이것을 알아야 10을 더할지 14를 더할지 DIR 에서 선택할 수 있다.
        direction = NODE.location[0] - NODE.parent[0], NODE.location[1] - NODE.location[1]

        #G 값계산
        NODE.G = self.maze_dict[NODE.parent].G + DIR[direction]
        #H 값계산
        NODE.H = abs(self.GOAL.location[0] - NODE.location[0]) + \
        abs(self.GOAL.location[1] - NODE.location[1])
        #F 값계산
        NODE.F = NODE.G + NODE.H


    def calculate(self, node):
        pass


    def start_goal(self, maze_map, start_location, goal_location):
        pass


    def push_open(self, location):

        # search_around 함수와 동일하게 around_nodes 리스트 생성
        around_nodes = list(map(tuple, np.array(list(Astar.DIR.keys())) + location))
        around_nodes = [i for i in around_nodes if ((i[0] >= 0) and (i[1] >= 0))]

        # around_nodes 중 barrier인 노드를 걸러내기 위해 tmp_barrier 리스트 생성
        tmp_barrier = []

        # around_nodes 중 barrier_list에 있는 노드가 있다면
        # 그 노드를 포함해서 상/하/좌/우 에 있는 노드까지 tmp_barrier로 취급하여
        # 5개의 노드를 tmp_barrier에 추가
        for i in around_nodes:
            if i in barrier_list:
                i_east = tuple(np.array(i) + np.array([1, 0]))
                i_west = tuple(np.array(i) + np.array([-1, 0]))
                i_north = tuple(np.array(i) + np.array([0, 1]))
                i_south = tuple(np.array(i) + np.array([0, -1]))
                tmp_barrier.extend([i, i_east, i_west, i_north, i_south])

        # 다시 around_nodes를 검색하여
        # opened_list, tmp_barrier 모두에 없는 노드만 opened_list에 추가
        for i in around_nodes:
            if (i not in tmp_barrier) and (i not in opened_list):
                self.opened_list.append(i)


    def sorting_open(self, opened_list):
        sort_open = [(i, maze_dict[i].F) for i in opened_list]
        opened_list = [j[0] for j in sorted(sort_open, key=lambda i: i[1])]
        return opened_list


    def maze_solver(self, maze_map, start_location, goal_location):
        pass
        # return self.GOAL.G, self.path
