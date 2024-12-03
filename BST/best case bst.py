import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# Генерация данных: количество узлов и высоты идеально сбалансированных деревьев
tree_sizes = list(range(1, 101))  # Количество узлов от 1 до 1024 с шагом 25
heights = [int(np.log2(size)) + 1 for size in tree_sizes]  # Вычисление высот

# Преобразуем данные для регрессии
X = np.log2(np.array(tree_sizes)).reshape(-1, 1)  # Преобразуем размеры в логарифмический масштаб
y = np.array(heights)

# Применяем линейную регрессию
model = LinearRegression()
model.fit(X, y)

# Получаем параметры модели
a = model.coef_[0]  # Угловой коэффициент
b = model.intercept_  # Свободный член

# Строим прогнозы регрессии
fitted_heights = model.predict(X)

# Построение графика
plt.scatter(tree_sizes, heights, color='blue', label='Экспериментальные данные')  # Точки
plt.plot(tree_sizes, fitted_heights, color='red', label=f'Логарифмическая регрессия: y = {a:.2f}log2(x) + {b:.2f}')  # Линия регрессии

# Настройки графика
plt.title('Зависимость высоты сбалансированного дерева от количества ключей')
plt.xlabel('Количество ключей')
plt.ylabel('Высота дерева')
plt.legend()
plt.grid(True)
plt.show()
