from dfs_traversals import dfs_preorder, dfs_inorder, dfs_postorder
from bfs_traversal import bfs
import random
class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        """Вставка узла в дерево."""
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return BSTNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node

    def delete(self, key):
        """Удаление узла из дерева."""
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            min_larger_node = self._get_min(node.right)
            node.key = min_larger_node.key
            node.right = self._delete(node.right, min_larger_node.key)
        return node

    def _get_min(self, node):
        """Получить узел с минимальным ключом."""
        while node.left is not None:
            node = node.left
        return node

    def search(self, key):
        """Поиск узла по ключу."""
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def get_height(self):
        return self._get_height(self.root)

    def _get_height(self, node):
        if not node:
            return 0
        left_height = self._get_height(node.left)
        right_height = self._get_height(node.right)
        return 1 + max(left_height, right_height)

    def draw_tree(self):
        """Отрисовка дерева в консоли."""
        def _draw_tree(node, prefix="", is_left=True):
            if node is not None:
                result = prefix + ("├── " if is_left else "└── ") + str(node.key) + "\n"
                next_prefix = prefix + ("│   " if is_left else "    ")
                result += _draw_tree(node.left, next_prefix, True)
                result += _draw_tree(node.right, next_prefix, False)
                return result
            return ""
        print(_draw_tree(self.root))

# Пример использования
bst = BST()

bst.insert(4)
bst.insert(2)
bst.insert(6)
bst.insert(1)
bst.insert(3)
bst.insert(5)
bst.insert(7)
'''
for i in range(10):
    bst.insert(random.randint(1, 10))
'''
# Отрисовка дерева после вставок
bst.draw_tree()

print("Прямой обход (Pre-order):", dfs_preorder(bst.root))
print("Симметричный обход (In-order):", dfs_inorder(bst.root))
print("Обратный обход (Post-order):", dfs_postorder(bst.root))

print("Обход в ширину (BFS):", bfs(bst.root))