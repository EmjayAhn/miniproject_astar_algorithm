class Node:
    def __init__(self, G=None, H=None, parent=None, location=None):

        self.G = G
        self.H = H
        self.F = self.G + self.H
        self.parent = parent
        self.location = location
