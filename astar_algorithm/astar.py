from node import Node

class Astar:


    def __init__(self):
        self.maze = dict()
        self.opened_list = list()
        self.closed_list = list()
        self.start = Node()
        self.goal = Node()


    # maze_map input 넣기
    # maze는 리스트 형태로 받기로 한다
    # for example,
    # maze = [[0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 1, 0, 0],
    #         [0, 0, 0, 1, 0, 0],
    #         [0, 0, 0, 1, 0, 0],
    #         [0, 0, 0, 0, 0, 0]]


    def maze_map(self, maze_map):
        self.maze_map = maze_map

        # maze에 외곽 만들어주기
        pass

        # maze dictionary 전체 노드 할당
        pass


    # start와 goal 좌표 넣기
    def start_and_goal(self, start_location, goal_location):
        start, goal = Node(), Node()
        start.location = start_location
        self.maze[start_location] = start
        goal.location = goal_location
        self.maze[goal_location] = goal


    def sorting_open(self, opened_list):
        sort_open = [(i, maze[i].F) for i in opened_list]
        opened_list = [j[0] for j in sorted(sort_open, key=lambda i: i[1])]
        return opened_list


    def openPush(self, node):
        self.opened_list.append(node)

        print(self.open)


    def closePush(self, node):
        self.closed_list.append(node)
        print(self.close)


    def G_calculate(self, node):
        pass


    def H_calculate(self, node):
        pass


    def __value(self, node):
        pass
        node.G = G_calculate(node)
        node.H = H_calculate(node)
        node.F = node.G + node.H


    # 주변 8개 노드 location 가져오기
    def __around_nodes(self, node):
        DIR = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
        self.around_nodes = DIR + ([node.loc] * 8)

    # 주변 8개 노드 F, G, H 다 계산해서 tmp_list 생성 후 (open노드/Non-open노드/close노드/barrier노드) 분류
    def search_around(self, node):
        tmp_open = {}
        tmp_noopen = {}
        for i in tmp_list:
            if i not in (barrier or closed_list):
                if i in opened_list:
                    tmp_open[i] = Node()
                else:
                    tmp_noopen[i] = Node()


    # open_list에 이미 있는 애들은 G value 비교
    def tmp_open(self, tmp_open):
        pass


    # non-open 애들은 F값 계산
    def tmp_noopen(self, tmp_noopen):
