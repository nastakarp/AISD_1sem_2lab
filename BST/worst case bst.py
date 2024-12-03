import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from BST import BST

tree_sizes = list(range(1, 101))
heights = []

for size in tree_sizes:
    tree = BST()
    keys = range(1, size + 1)
    for key in keys:
        tree.insert(key)
    heights.append(tree.get_height())
X = np.array(tree_sizes).reshape(-1, 1)
y = np.array(heights)

model = LinearRegression()
model.fit(X, y)

a = model.coef_[0]
b = model.intercept_

fitted_heights = model.predict(X)

plt.scatter(tree_sizes, heights, color='blue', label='Экспериментальные данные')

plt.plot(tree_sizes, fitted_heights, color='red', label=f'Линейная регрессия: y = {a:.2f}x + {b:.2f}')

plt.title('Зависимость высоты бинарного дерева от количества ключей (упорядоченные данные)')
plt.xlabel('Количество ключей')
plt.ylabel('Высота дерева')
plt.legend()
plt.grid(True)
plt.show()
