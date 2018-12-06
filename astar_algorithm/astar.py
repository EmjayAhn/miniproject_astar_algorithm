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

    def calculate(self, node):
        pass

    def start_goal(self, maze_map, start_location, goal_location):
        pass

    def push_open(self, location):
        pass

    def maze_solver(self, maze_map, start_location, goal_location):

        pass
        #return self.GOAL.G, self.path
