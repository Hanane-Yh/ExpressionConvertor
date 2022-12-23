class Node:
    def __init__(self, data, left=None, right=None, id=None):
        self.data = data
        self.left = left
        self.right = right
        self.id = id

    def __str__(self):
        return str(self.data)

