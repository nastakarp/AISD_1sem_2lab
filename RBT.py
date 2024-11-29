class RBNode:
    def __init__(self, key, color='RED'):
        self.key = key
        self.color = color  # 'RED' or 'BLACK'
        self.left = None
        self.right = None
        self.parent = None

class RBTree:
    def __init__(self):
        self.TNULL = RBNode(None, 'BLACK')
        self.root = self.TNULL

    def insert(self, key):
        # Алгоритм вставки, включая балансировку
        pass

    def delete(self, key):
        # Алгоритм удаления, включая балансировку
        pass

    def search(self, key):
        current = self.root
        while current != self.TNULL and current.key != key:
            if key < current.key:
                current = current.left
            else:
                current = current.right
        return current
