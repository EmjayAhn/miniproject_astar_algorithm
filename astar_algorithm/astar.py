from node import Node

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


    def search_around(self, node):
        pass

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

    def start_goal(self, maze_map, start_location, goal_location):
        pass

    def push_open(self, location):
        pass

    def maze_solver(self, maze_map, start_location, goal_location):

        pass
        #return self.GOAL.G, self.path
