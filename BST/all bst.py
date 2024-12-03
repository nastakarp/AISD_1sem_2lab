import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from scipy.optimize import curve_fit
from BST import BST
import random
tree_sizes = list(range(1, 101,5))
#Идеально сбалансированное дерево
heights_balanced = [int(np.log2(size)) + 1 for size in tree_sizes]

X_balanced = np.log2(np.array(tree_sizes)).reshape(-1, 1)
y_balanced = np.array(heights_balanced)

model_balanced = LinearRegression()
model_balanced.fit(X_balanced, y_balanced)
fitted_balanced = model_balanced.predict(X_balanced)

#Упорядоченные ключи
heights_ordered = []

for size in tree_sizes:
    tree = BST()
    for key in range(1, size + 1):
        tree.insert(key)
    heights_ordered.append(tree.get_height())

X_ordered = np.array(tree_sizes).reshape(-1, 1)
y_ordered = np.array(heights_ordered)

model_ordered = LinearRegression()
model_ordered.fit(X_ordered, y_ordered)
fitted_ordered = model_ordered.predict(X_ordered)

#Случайные ключи
def log_model(x, a, b):
    return a * np.log(x) + b
heights_random = []

for size in tree_sizes:
    tree = BST()
    for _ in range(size):
        tree.insert(random.randint(1, 1000))
    heights_random.append(tree.get_height())

popt_random, _ = curve_fit(log_model, tree_sizes, heights_random)
a_random, b_random = popt_random
fitted_random = log_model(np.array(tree_sizes), a_random, b_random)

plt.figure(figsize=(12, 8))

plt.scatter(tree_sizes, heights_balanced, color='blue', s=10, label='Ключи распределены равномерно (лучший случай)')
plt.plot(tree_sizes, fitted_balanced, color='blue', linestyle='--', label='регрессия')

plt.scatter(tree_sizes, heights_random, color='red', s=10, label='Случайная величина ключа (средний случай)')
plt.plot(tree_sizes, fitted_random, color='red', linestyle='--', label='регрессия')

plt.scatter(tree_sizes, heights_ordered, color='green', s=10, label='Упорядоченные ключи (худший случай)')
plt.plot(tree_sizes, fitted_ordered, color='green', linestyle='--', label='регрессия')

plt.title('Сравнение высоты дерева для разных случаев', fontsize=14)
plt.xlabel('Количество ключей', fontsize=12)
plt.ylabel('Высота дерева', fontsize=12)
plt.legend(fontsize=10)
plt.grid(True)
plt.show()
