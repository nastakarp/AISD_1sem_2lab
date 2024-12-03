import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from BST import BST

# Функция для построения графика с линейной регрессией

tree_sizes = list(range(1, 101))  # Количество ключей от 1 до 100
heights = []

for size in tree_sizes:
    tree = BST()
    # Вставляем ключи строго в порядке возрастания
    keys = range(1, size + 1)  # Последовательность от 1 до size
    for key in keys:
        tree.insert(key)  # Преобразуем ключи в целые числа
    heights.append(tree.get_height())

# Преобразуем данные для линейной регрессии
X = np.array(tree_sizes).reshape(-1, 1)  # Преобразуем размеры деревьев в формат (n_samples, n_features)
y = np.array(heights)  # Высоты деревьев

# Применяем линейную регрессию
model = LinearRegression()
model.fit(X, y)

# Получаем параметры линейной модели
a = model.coef_[0]  # Угловой коэффициент
b = model.intercept_  # Свободный член

# Строим кривую регрессии
fitted_heights = model.predict(X)

# Строим график с точками
plt.scatter(tree_sizes, heights, color='blue', label='Экспериментальные данные')

# Строим линейную регрессию
plt.plot(tree_sizes, fitted_heights, color='red', label=f'Линейная регрессия: y = {a:.2f}x + {b:.2f}')

# Настройки графика
plt.title('Зависимость высоты бинарного дерева от количества ключей (упорядоченные данные)')
plt.xlabel('Количество ключей')
plt.ylabel('Высота дерева')
plt.legend()
plt.grid(True)
plt.show()
