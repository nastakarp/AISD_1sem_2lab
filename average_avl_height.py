import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from AVL import AVLTree
# Функция для вычисления высоты AVL-дерева при монотонном увеличении ключей
def average_avl_height(n):
    avl_tree = AVLTree()
    heights = []
    for i in range(1, n + 1):
        avl_tree.insert(i)
        heights.append(avl_tree.root.height)
    return heights

# Массив для записи значений n
n_values = range(10, 500, 10)
height_values = []

# Получаем высоту дерева для разных значений n
for n in n_values:
    height_values.append(average_avl_height(n)[-1])

# Подготовка данных для линейной регрессии
X = np.array(n_values).reshape(-1, 1)
y = np.array(height_values)

# Применение линейной регрессии (по log(n))
log_X = np.log(X)  # Преобразуем X в логарифмическую шкалу
regressor = LinearRegression()
regressor.fit(log_X, y)

# Получаем значения регрессии для построения кривой
predicted_heights = regressor.predict(log_X)

# Построение графика с точками и регрессирующей кривой
plt.scatter(n_values, height_values, label="Высота AVL-дерева", color="blue", s=10)
plt.plot(n_values, predicted_heights, label="Логарифмическая регрессия", linestyle="-", color="green")
plt.xlabel("Количество ключей n")
plt.ylabel("Высота дерева")
plt.title("Зависимость высоты AVL-дерева от количества ключей")
plt.legend()
plt.grid(True)
plt.show()
