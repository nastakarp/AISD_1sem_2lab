import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from RBT import RBTree

def log_model(x, a, b):
    return a * np.log(x) + b

tree_sizes = list(range(1, 101, 2))

heights_random = []
for size in tree_sizes:
    tree = RBTree()
    for _ in range(size):
        tree.insert(np.random.randint(1, 1000))
    heights_random.append(tree._height(tree.root))

heights_monotonic = []
for size in tree_sizes:
    tree = RBTree()
    for key in range(1, size + 1):
        tree.insert(key)
    heights_monotonic.append(tree._height(tree.root))

plt.scatter(tree_sizes, heights_random, color='blue', label='Случайные ключи')
plt.scatter(tree_sizes, heights_monotonic, color='green', label='Монотонные ключи')

popt_random, _ = curve_fit(log_model, tree_sizes, heights_random)
a_random, b_random = popt_random
fitted_heights_random = log_model(np.array(tree_sizes), a_random, b_random)
plt.plot(tree_sizes, fitted_heights_random, color='red', label=f'регрессия (случайная)')

popt_monotonic, _ = curve_fit(log_model, tree_sizes, heights_monotonic)
a_monotonic, b_monotonic = popt_monotonic
fitted_heights_monotonic = log_model(np.array(tree_sizes), a_monotonic, b_monotonic)
plt.plot(tree_sizes, fitted_heights_monotonic, color='orange', label=f'регрессия (монотонная)')

plt.title('Зависимость высоты красно-чёрного дерева от количества ключей')
plt.xlabel('Количество ключей')
plt.ylabel('Высота дерева')
plt.legend()
plt.grid(True)
plt.show()
