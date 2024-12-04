import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from scipy.optimize import curve_fit
from BST import BST
import random

# Размеры деревьев
tree_sizes = list(range(1, 101, 5))

# Идеально сбалансированное дерево
heights_balanced = [int(np.log2(size)) + 1 for size in tree_sizes]

X_balanced = np.log2(np.array(tree_sizes)).reshape(-1, 1)
y_balanced = np.array(heights_balanced)

# Регрессия для сбалансированного дерева
model_balanced = LinearRegression()
model_balanced.fit(X_balanced, y_balanced)
fitted_balanced = model_balanced.predict(X_balanced)

# Упорядоченные ключи (худший случай)
heights_ordered = []

for size in tree_sizes:
    tree = BST()
    for key in range(1, size + 1):
        tree.insert(key)
    heights_ordered.append(tree.get_height())

X_ordered = np.array(tree_sizes).reshape(-1, 1)
y_ordered = np.array(heights_ordered)

# Регрессия для упорядоченных ключей
model_ordered = LinearRegression()
model_ordered.fit(X_ordered, y_ordered)
fitted_ordered = model_ordered.predict(X_ordered)

# Случайные ключи
def log_model(x, a, b):
    return a * np.log(x) + b

heights_random = []

for size in tree_sizes:
    tree = BST()
    for _ in range(size):
        tree.insert(random.randint(1, 1000))
    heights_random.append(tree.get_height())

# Регрессия для случайных ключей
popt_random, _ = curve_fit(log_model, tree_sizes, heights_random)
a_random, b_random = popt_random
fitted_random = log_model(np.array(tree_sizes), a_random, b_random)

# Построение графика
plt.figure(figsize=(12, 8))

# Сбалансированные ключи
plt.scatter(tree_sizes, heights_balanced, color='blue', s=10, label='Ключи распределены равномерно (лучший случай)')
plt.plot(tree_sizes, fitted_balanced, color='blue', linestyle='-', label='Регрессия (лучший случай)')

# Случайные ключи
plt.scatter(tree_sizes, heights_random, color='red', s=10, label='Случайные величины ключа (средний случай)')
plt.plot(tree_sizes, fitted_random, color='red', linestyle='-', label='Регрессия (средний случай)')

# Упорядоченные ключи
plt.scatter(tree_sizes, heights_ordered, color='green', s=10, label='Упорядоченные ключи (худший случай)')
plt.plot(tree_sizes, fitted_ordered, color='green', linestyle='-', label='Регрессия (худший случай)')

# Обычная логарифмическая кривая (для идеального сбалансированного дерева)
log_curve = np.log(np.array(tree_sizes))
plt.plot(tree_sizes, log_curve, color='purple', linestyle='--', label='y = log(x))')

# Подпись регрессионных полиномов
print( f'Регрессия (лучший случай): y = {model_balanced.coef_[0]:.2f} * log(x) + {model_balanced.intercept_:.2f}')
print( f'Регрессия (средний случай): y = {a_random:.2f} * log(x) + {b_random:.2f}')
print(f'Регрессия (худший случай): y = {model_ordered.coef_[0]:.2f} * x + {model_ordered.intercept_:.2f}')

# Настройка графика
plt.title('Сравнение высоты дерева для разных случаев', fontsize=14)
plt.xlabel('Количество ключей', fontsize=12)
plt.ylabel('Высота дерева', fontsize=12)
plt.legend(fontsize=10)
plt.grid(True)
plt.show()
