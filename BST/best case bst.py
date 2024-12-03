import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

tree_sizes = list(range(1, 101))
heights = [int(np.log2(size)) + 1 for size in tree_sizes]

X = np.log2(np.array(tree_sizes)).reshape(-1, 1)
y = np.array(heights)

model = LinearRegression()
model.fit(X, y)

a = model.coef_[0]
b = model.intercept_

fitted_heights = model.predict(X)

plt.scatter(tree_sizes, heights, color='blue', label='Экспериментальные данные')
plt.plot(tree_sizes, fitted_heights, color='red', label=f'Логарифмическая регрессия: y = {a:.2f}log2(x) + {b:.2f}')
plt.title('Зависимость высоты сбалансированного дерева от количества ключей')
plt.xlabel('Количество ключей')
plt.ylabel('Высота дерева')
plt.legend()
plt.grid(True)
plt.show()
