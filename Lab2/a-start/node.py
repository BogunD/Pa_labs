class node:
    def __init__(self, parent=None, position=None):
        self.G = 0
        self.H = 0
        self.F = 0
        self.parent = parent
        self.pos = position

    def __eq__(self, other):
        return self.pos == other.pos


