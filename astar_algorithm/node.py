class Node:
    def __init__(self, G=None, H=None, parent=None, location=None):
        self.G = G
        self.H = H
        self.parent = parent
        self.location = location

    @property
    def data(self):
        print("F({}) = G({}) + H({})".format(self.F, self.G, self.H))

    @data.setter
    def data(self, G, H):
        self.G = G
        self.H = H
        self.F = self.G + self.H

    @property
    def parent(self):
        print("parrent Node is {}.".format(parent))

    @parent.setter
    def parent(self, parent):
        self.parent = parent

    @property
    def location(self):
        print("current location is {}.".format(location))

    @location.setter
    def location(self, location):
        self.location = location
        print('a')
