import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from BST import BST


# Функция для вычисления высоты дерева поиска (средняя высота)
def average_bst_height(num_keys, trials=1000):
    heights = []
    for _ in range(trials):
        keys = np.random.permutation(num_keys)  # Случайная перестановка ключей
        bst = BST()
        for key in keys:
            bst.insert(key)
        heights.append(bst.get_height())
    return np.mean(heights)


# Массив для записи значений n
n_values = range(10, 500, 10)
height_values = []

# Получаем среднюю высоту дерева для разных значений n
for num_keys in n_values:
    height_values.append(average_bst_height(num_keys))

# Подготовка данных для линейной регрессии
X = np.array(n_values).reshape(-1, 1)
y = np.array(height_values)

# Применение линейной регрессии к данным (по log(n))
log_X = np.log(X)  # Преобразуем X в логарифмическую шкалу
regressor = LinearRegression()
regressor.fit(log_X, y)

# Получаем значения регрессии для построения кривой
predicted_heights = regressor.predict(log_X)

# Построение графика с точками и регрессирующей кривой
plt.scatter(n_values, height_values, label="Средняя высота дерева", color="blue", s=10)
plt.plot(n_values, predicted_heights, label="Логарифмическая регрессия", linestyle="-", color="green")
plt.xlabel("Количество ключей n")
plt.ylabel("Средняя высота дерева")
plt.title("Зависимость высоты дерева поиска от количества ключей")
plt.legend()
plt.grid(True)
plt.show()
