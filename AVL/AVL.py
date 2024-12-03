from dfs_traversals import dfs_preorder, dfs_inorder, dfs_postorder
from bfs_traversal import bfs
class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # Высота узла

class AVLTree:
    def __init__(self):
        self.root = None

    # Вспомогательная функция для получения высоты узла
    def _height(self, node):
        return node.height if node else 0

    # Вычисление баланса узла
    def _get_balance(self, node):
        if not node:
            return 0
        return self._height(node.left) - self._height(node.right)

    # Поворот вправо
    def _rotate_right(self, z):
        y = z.left
        T3 = y.right

        # Выполнение вращения
        y.right = z
        z.left = T3

        # Обновление высоты
        z.height = 1 + max(self._height(z.left), self._height(z.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))

        return y

    # Поворот влево
    def _rotate_left(self, z):
        y = z.right
        T2 = y.left

        # Выполнение вращения
        y.left = z
        z.right = T2

        # Обновление высоты
        z.height = 1 + max(self._height(z.left), self._height(z.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))

        return y

    # Вставка ключа
    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        # Обычная вставка в BST
        if not node:
            return AVLNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            return node  # Дубли ключей не допускаются

        # Обновление высоты текущего узла
        node.height = 1 + max(self._height(node.left), self._height(node.right))

        # Проверка баланса
        balance = self._get_balance(node)

        # Левое-левое
        if balance > 1 and key < node.left.key:
            return self._rotate_right(node)

        # Правое-правое
        if balance < -1 and key > node.right.key:
            return self._rotate_left(node)

        # Левое-правое
        if balance > 1 and key > node.left.key:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        # Правое-левое
        if balance < -1 and key < node.right.key:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    # Удаление ключа
    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        # Обычное удаление из BST
        if not node:
            return node
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # Узел с одним дочерним элементом или без дочерних
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            # Узел с двумя дочерними элементами
            temp = self._get_min(node.right)
            node.key = temp.key
            node.right = self._delete(node.right, temp.key)

        # Обновление высоты
        node.height = 1 + max(self._height(node.left), self._height(node.right))

        # Проверка баланса
        balance = self._get_balance(node)

        # Левое-левое
        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._rotate_right(node)

        # Левое-правое
        if balance > 1 and self._get_balance(node.left) < 0:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        # Правое-правое
        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._rotate_left(node)

        # Правое-левое
        if balance < -1 and self._get_balance(node.right) > 0:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    # Получение минимального значения в дереве
    def _get_min(self, node):
        while node.left:
            node = node.left
        return node

    # Поиск ключа
    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if not node or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    # Функция для отрисовки дерева
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


# Пример использования
avl = AVLTree()

# Вставка ключей
keys = [10, 20, 30, 40, 50,25]
for key in keys:
    avl.insert(key)

# Отрисовка дерева
avl.draw_tree()

print("Прямой обход (Pre-order):", dfs_preorder(avl.root))
print("Симметричный обход (In-order):", dfs_inorder(avl.root))
print("Обратный обход (Post-order):", dfs_postorder(avl.root))

print("Обход в ширину (BFS):", bfs(avl.root))