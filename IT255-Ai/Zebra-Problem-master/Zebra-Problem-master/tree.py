class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []
        self.noChildren = 0

    def add_child(self, obj):
        self.children.append(obj)
        self.noChildren += 1
        return self.children[self.noChildren -1]
    def get_data(self):
        return self.data
    