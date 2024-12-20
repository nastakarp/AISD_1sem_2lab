from dfs_traversals import dfs_preorder, dfs_inorder, dfs_postorder
from bfs_traversal import bfs

class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
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
        while node.left is not None:
            node = node.left
        return node

    def search(self, key):
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
        def _draw_tree(node, prefix="", is_left=True):
            if node is not None:
                result = prefix + ("├── " if is_left else "└── ") + str(node.key) + "\n"
                next_prefix = prefix + ("│   " if is_left else "    ")
                result += _draw_tree(node.left, next_prefix, True)
                result += _draw_tree(node.right, next_prefix, False)
                return result
            return ""
        print(_draw_tree(self.root))

# Примеры использования
bst = BST()

# Вставка элементов
keys_to_insert = [4, 2, 6, 1, 3, 5, 7]
for key in keys_to_insert:
    print(f"\nВставка ключа {key}:")
    bst.insert(key)
    bst.draw_tree()

# Поиск элемента
key_to_search = 3
print(f"\nПоиск ключа {key_to_search}:")
result = bst.search(key_to_search)
print(f"Результат поиска: {'найден' if result else 'не найден'}")

# Удаление элемента
key_to_delete = 6
print(f"\nУдаление ключа {key_to_delete}:")
bst.delete(key_to_delete)
bst.draw_tree()

# Печать обходов
print("\nОбходы дерева:")
print("Прямой обход (Pre-order):", dfs_preorder(bst.root))
print("Симметричный обход (In-order):", dfs_inorder(bst.root))
print("Обратный обход (Post-order):", dfs_postorder(bst.root))
print("Обход в ширину (BFS):", bfs(bst.root))
