import random
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from RBT import RBTree

# Логарифмическая модель для регрессии
def log_model(x, a, b):
    return a * np.log(x) + b

tree_sizes = list(range(1, 101,2))  # Количество ключей от 1 до 100
heights = []

for size in tree_sizes:
    tree = RBTree()
    # Вставляем монотонно возрастающие ключи в дерево
    for key in range(1, size + 1):  # Ключи от 1 до `size`
        tree.insert(key)
    heights.append(tree._height(tree.root))  # Высота дерева

# Строим график с точками
plt.scatter(tree_sizes, heights, color='blue', label='Экспериментальные данные')

# Применяем логарифмическую регрессию
popt, _ = curve_fit(log_model, tree_sizes, heights)
a, b = popt

# Строим кривую регрессии
fitted_heights = log_model(np.array(tree_sizes), a, b)
plt.plot(tree_sizes, fitted_heights, color='red', label=f'Логарифмическая регрессия: y = {a:.2f}*log(x) + {b:.2f}')

# Настройки графика
plt.title('Зависимость высоты чёрно-красного дерева от количества ключей')
plt.xlabel('Количество ключей')
plt.ylabel('Высота дерева')
plt.legend()
plt.grid(True)
plt.show()
