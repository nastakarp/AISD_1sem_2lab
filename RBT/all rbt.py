import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from RBT import RBTree

def log_model(x, a, b):
    return a * np.log(x) + b

tree_sizes = list(range(1, 101, 2))

# Высоты для случайных ключей
heights_random = []
for size in tree_sizes:
    tree = RBTree()
    for _ in range(size):
        tree.insert(np.random.randint(1, 1000))
    heights_random.append(tree._height(tree.root))

# Высоты для монотонных ключей
heights_monotonic = []
for size in tree_sizes:
    tree = RBTree()
    for key in range(1, size + 1):
        tree.insert(key)
    heights_monotonic.append(tree._height(tree.root))

# Регрессия для случайных ключей
popt_random, _ = curve_fit(log_model, tree_sizes, heights_random)
a_random, b_random = popt_random
fitted_heights_random = log_model(np.array(tree_sizes), a_random, b_random)

# Регрессия для монотонных ключей
popt_monotonic, _ = curve_fit(log_model, tree_sizes, heights_monotonic)
a_monotonic, b_monotonic = popt_monotonic
fitted_heights_monotonic = log_model(np.array(tree_sizes), a_monotonic, b_monotonic)

# Построение графика
plt.figure(figsize=(12, 8))

# Случайные ключи
plt.scatter(tree_sizes, heights_random, color='blue', s=10, label='Случайные ключи')
plt.plot(tree_sizes, fitted_heights_random, color='red', linestyle='-', label=f'Регрессия (случайная): y = {a_random:.2f} * log(x) + {b_random:.2f}')

# Монотонные ключи
plt.scatter(tree_sizes, heights_monotonic, color='green', s=10, label='Монотонные ключи')
plt.plot(tree_sizes, fitted_heights_monotonic, color='orange', linestyle='-', label=f'Регрессия (монотонная): y = {a_monotonic:.2f} * log(x) + {b_monotonic:.2f}')
log_curve = 2*np.log(np.array(tree_sizes)+1)
plt.plot(tree_sizes, log_curve, color='purple', linestyle='--', label='y = 2*log(x+1))')
# Настройка графика
plt.title('Зависимость высоты красно-чёрного дерева от количества ключей', fontsize=14)
plt.xlabel('Количество ключей', fontsize=12)
plt.ylabel('Высота дерева', fontsize=12)
plt.legend(fontsize=10)
plt.grid(True)
plt.show()
