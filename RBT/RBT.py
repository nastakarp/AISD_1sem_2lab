from dfs_traversals import dfs_preorder, dfs_inorder, dfs_postorder
from bfs_traversal import bfs
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
    def _height(self, node):
        if node == self.TNULL:
            return 0
        left_height = self._height(node.left)
        right_height = self._height(node.right)
        return 1 + max(left_height, right_height)

    def insert(self, key):
        new_node = RBNode(key)
        new_node.left = self.TNULL
        new_node.right = self.TNULL
        new_node.color = 'RED'

        parent = None
        current = self.root
        while current != self.TNULL:
            parent = current
            if key < current.key:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        self._balance_insert(new_node)

    def _balance_insert(self, k):
        while k != self.root and k.parent.color == 'RED':
            if k.parent == k.parent.parent.left:
                uncle = k.parent.parent.right
                if uncle.color == 'RED':
                    k.parent.color = 'BLACK'
                    uncle.color = 'BLACK'
                    k.parent.parent.color = 'RED'
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self._rotate_left(k)
                    k.parent.color = 'BLACK'
                    k.parent.parent.color = 'RED'
                    self._rotate_right(k.parent.parent)
            else:
                uncle = k.parent.parent.left
                if uncle.color == 'RED':
                    k.parent.color = 'BLACK'
                    uncle.color = 'BLACK'
                    k.parent.parent.color = 'RED'
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self._rotate_right(k)
                    k.parent.color = 'BLACK'
                    k.parent.parent.color = 'RED'
                    self._rotate_left(k.parent.parent)
        self.root.color = 'BLACK'

    def _rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _rotate_right(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y
    def delete(self, key):
        node_to_delete = self._search_tree(self.root, key)
        if node_to_delete == self.TNULL:
            return

        y = node_to_delete
        y_original_color = y.color
        if node_to_delete.left == self.TNULL:
            x = node_to_delete.right
            self._rb_transplant(node_to_delete, node_to_delete.right)
        elif node_to_delete.right == self.TNULL:
            x = node_to_delete.left
            self._rb_transplant(node_to_delete, node_to_delete.left)
        else:
            y = self._get_min(node_to_delete.right)
            y_original_color = y.color
            x = y.right
            if y.parent == node_to_delete:
                x.parent = y
            else:
                self._rb_transplant(y, y.right)
                y.right = node_to_delete.right
                y.right.parent = y
            self._rb_transplant(node_to_delete, y)
            y.left = node_to_delete.left
            y.left.parent = y
            y.color = node_to_delete.color

        if y_original_color == 'BLACK':
            self._balance_delete(x)

    def _balance_delete(self, x):
        while x != self.root and x.color == 'BLACK':
            if x == x.parent.left:
                sibling = x.parent.right
                if sibling.color == 'RED':
                    sibling.color = 'BLACK'
                    x.parent.color = 'RED'
                    self._rotate_left(x.parent)
                    sibling = x.parent.right
                if sibling.left.color == 'BLACK' and sibling.right.color == 'BLACK':
                    sibling.color = 'RED'
                    x = x.parent
                else:
                    if sibling.right.color == 'BLACK':
                        sibling.left.color = 'BLACK'
                        sibling.color = 'RED'
                        self._rotate_right(sibling)
                        sibling = x.parent.right
                    sibling.color = x.parent.color
                    x.parent.color = 'BLACK'
                    sibling.right.color = 'BLACK'
                    self._rotate_left(x.parent)
                    x = self.root
            else:
                sibling = x.parent.left
                if sibling.color == 'RED':
                    sibling.color = 'BLACK'
                    x.parent.color = 'RED'
                    self._rotate_right(x.parent)
                    sibling = x.parent.left
                if sibling.left.color == 'BLACK' and sibling.right.color == 'BLACK':
                    sibling.color = 'RED'
                    x = x.parent
                else:
                    if sibling.left.color == 'BLACK':
                        sibling.right.color = 'BLACK'
                        sibling.color = 'RED'
                        self._rotate_left(sibling)
                        sibling = x.parent.left
                    sibling.color = x.parent.color
                    x.parent.color = 'BLACK'
                    sibling.left.color = 'BLACK'
                    self._rotate_right(x.parent)
                    x = self.root
        x.color = 'BLACK'

    def _rb_transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def _get_min(self, node):
        while node.left != self.TNULL:
            node = node.left
        return node

    def search(self, key):
        return self._search_tree(self.root, key)

    def _search_tree(self, node, key):
        if node == self.TNULL or node.key == key:
            return node

        if key < node.key:
            return self._search_tree(node.left, key)

        return self._search_tree(node.right, key)

    def draw_tree(self):
        def _draw_tree(node, prefix="", is_left=True):
            if node != self.TNULL:
                color = "RED" if node.color == "RED" else "BLACK"
                result = prefix + ("├── " if is_left else "└── ") + f"{node.key} ({color})\n"
                next_prefix = prefix + ("│   " if is_left else "    ")
                result += _draw_tree(node.left, next_prefix, True)
                result += _draw_tree(node.right, next_prefix, False)
                return result
            return prefix + ("├── " if is_left else "└── ") + "NIL (BLACK)\n"

        print(_draw_tree(self.root))
rb_tree = RBTree()

# Вставка ключей
keys_to_insert = [5, 3, 7, 2, 4, 6, 8, 1, 9]
for key in keys_to_insert:
    print(f"\nВставка ключа {key}:")
    rb_tree.insert(key)
    rb_tree.draw_tree()

# Поиск ключа
key_to_search = 70
print(f"\nПоиск ключа {key_to_search}:")
result = rb_tree.search(key_to_search)
if result != rb_tree.TNULL:
    print(f"Ключ {key_to_search} найден. Цвет: {result.color}")
else:
    print(f"Ключ {key_to_search} не найден.")

# Удаление ключа
key_to_delete = 6
print(f"\nУдаление ключа {key_to_delete}:")
rb_tree.delete(key_to_delete)
rb_tree.draw_tree()

# Обходы дерева
print("\nОбходы дерева:")
print("Прямой обход (Pre-order):", dfs_preorder(rb_tree.root))
print("Симметричный обход (In-order):", dfs_inorder(rb_tree.root))
print("Обратный обход (Post-order):", dfs_postorder(rb_tree.root))
print("Обход в ширину (BFS):", bfs(rb_tree.root))