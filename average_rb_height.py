import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# Класс узла красно-черного дерева
class RBNode:
    def __init__(self, key, color='RED'):
        self.key = key
        self.color = color  # 'RED' or 'BLACK'
        self.left = None
        self.right = None
        self.parent = None

# Класс красно-черного дерева
class RBTree:
    def __init__(self):
        self.TNULL = RBNode(None, 'BLACK')  # Сентинельный узел
        self.root = self.TNULL

    # Функция для вставки нового узла
    def insert(self, key):
        new_node = RBNode(key)
        y = None
        x = self.root

        while x != self.TNULL:
            y = x
            if new_node.key < x.key:
                x = x.left
            else:
                x = x.right

        new_node.parent = y
        if y is None:
            self.root = new_node
        elif new_node.key < y.key:
            y.left = new_node
        else:
            y.right = new_node

        new_node.left = self.TNULL
        new_node.right = self.TNULL
        new_node.color = 'RED'

        self.fix_insert(new_node)

    # Функция для восстановления свойств красно-черного дерева после вставки
    def fix_insert(self, k):
        while k.parent and k.parent.color == 'RED':  # Проверка на None для родителя
            if k.parent == k.parent.parent.left:
                u = k.parent.parent.right
                if u.color == 'RED':
                    u.color = 'BLACK'
                    k.parent.color = 'BLACK'
                    k.parent.parent.color = 'RED'
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = 'BLACK'
                    k.parent.parent.color = 'RED'
                    self.right_rotate(k.parent.parent)
            else:
                u = k.parent.parent.left
                if u.color == 'RED':
                    u.color = 'BLACK'
                    k.parent.color = 'BLACK'
                    k.parent.parent.color = 'RED'
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = 'BLACK'
                    k.parent.parent.color = 'RED'
                    self.left_rotate(k.parent.parent)

            # Если текущий узел стал корнем дерева, завершить балансировку
            if k.parent is None:
                break

        self.root.color = 'BLACK'

    # Вращение влево
    def left_rotate(self, x):
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

    # Вращение вправо
    def right_rotate(self, x):
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

    # Функция для вычисления высоты дерева
    def height(self, node):
        if node == self.TNULL:
            return 0
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return max(left_height, right_height) + 1

# Функция для вычисления высоты красно-черного дерева при монотонном увеличении ключей
def average_rb_height(n):
    rb_tree = RBTree()
    heights = []
    for i in range(1, n + 1):
        rb_tree.insert(i)
        heights.append(rb_tree.height(rb_tree.root))
    return heights

# Массив для записи значений n
n_values = range(10, 500, 10)
height_values = []

# Получаем высоту дерева для разных значений n
for n in n_values:
    height_values.append(average_rb_height(n)[-1])

# Подготовка данных для линейной регрессии
X = np.array(n_values).reshape(-1, 1)
y = np.array(height_values)

# Применение линейной регрессии (по log(n))
log_X = np.log(X)  # Преобразуем X в логарифмическую шкалу
regressor = LinearRegression()
regressor.fit(log_X, y)

# Получаем значения регрессии для построения кривой
predicted_heights = regressor.predict(log_X)

# Построение графика с точками и регрессирующей кривой
plt.scatter(n_values, height_values, label="Высота красно-черного дерева", color="blue", s=10)
plt.plot(n_values, predicted_heights, label="Логарифмическая регрессия", linestyle="-", color="green")
plt.xlabel("Количество ключей n")
plt.ylabel("Высота дерева")
plt.title("Зависимость высоты красно-черного дерева от количества ключей")
plt.legend()
plt.grid(True)
plt.show()
