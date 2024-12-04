import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from AVL import AVLTree

# Логарифмическая модель
def log_model(x, a, b):
    return a * np.log(x) + b

# Размеры деревьев
tree_sizes = list(range(1, 101, 2))

# Высоты для случайной вставки
heights_random = []
for size in tree_sizes:
    tree = AVLTree()
    for _ in range(size):
        tree.insert(np.random.randint(1, 1000))
    heights_random.append(tree._height(tree.root))

# Высоты для монотонной вставки
heights_monotonic = []
for size in tree_sizes:
    tree = AVLTree()
    for key in range(1, size + 1):
        tree.insert(key)
    heights_monotonic.append(tree._height(tree.root))

# Построение точек для случайных и монотонных вставок
plt.scatter(tree_sizes, heights_random, color='blue', label='Случайные ключи')
plt.scatter(tree_sizes, heights_monotonic, color='green', label='Монотонные ключи')

# Регрессия для случайных вставок
popt_random, _ = curve_fit(log_model, tree_sizes, heights_random)
a_random, b_random = popt_random
fitted_heights_random = log_model(np.array(tree_sizes), a_random, b_random)
plt.plot(tree_sizes, fitted_heights_random, color='red', label=f'Регрессия (случайная): y = {a_random:.2f} * log(x) + {b_random:.2f}')

# Регрессия для монотонных вставок
popt_monotonic, _ = curve_fit(log_model, tree_sizes, heights_monotonic)
a_monotonic, b_monotonic = popt_monotonic
fitted_heights_monotonic = log_model(np.array(tree_sizes), a_monotonic, b_monotonic)
plt.plot(tree_sizes, fitted_heights_monotonic, color='orange', label=f'Регрессия (монотонная): y = {a_monotonic:.2f} * log(x) + {b_monotonic:.2f}')

# Построение кривой обычного логарифма для сравнения
log_curve = (np.log(np.array(tree_sizes)) / np.log(1.63)) + 1
plt.plot(tree_sizes, log_curve, color='purple', label='y = log_1.63(x) + 1', linestyle='--')

# Настройка графика
plt.title('Зависимость высоты AVL дерева от количества ключей')
plt.xlabel('Количество ключей')
plt.ylabel('Высота дерева')
plt.legend()
plt.grid(True)
plt.show()
