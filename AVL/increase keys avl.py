import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from AVL import AVLTree
def log_model(x, a, b):
    return a * np.log(x) + b

tree_sizes = list(range(1, 101,1))
heights = []

for size in tree_sizes:
    tree = AVLTree()
    for key in range(1, size + 1):
        tree.insert(key)
    heights.append(tree._height(tree.root))

plt.scatter(tree_sizes, heights, color='blue', label='Экспериментальные данные')

popt, _ = curve_fit(log_model, tree_sizes, heights)
a, b = popt

fitted_heights = log_model(np.array(tree_sizes), a, b)
plt.plot(tree_sizes, fitted_heights, color='red', label=f'Логарифмическая регрессия: y = {a:.2f}*log(x) + {b:.2f}')

plt.title('Зависимость высоты AVL дерева от количества ключей')
plt.xlabel('Количество ключей')
plt.ylabel('Высота дерева')
plt.legend()
plt.grid(True)
plt.show()
