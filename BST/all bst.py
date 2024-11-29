import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from sklearn.linear_model import LinearRegression
from BST import BST


# Логарифмическая модель для регрессии
def log_model(x, a, b):
    return a * np.log(x) + b


# Функция для генерации ключей в разных сценариях
def generate_keys(case, size):
    if case == "random":
        return np.random.randint(1, 1001, size)
    elif case == "uniform":
        return np.linspace(1, 1000, size)
    elif case == "sorted":
        return range(1, size + 1)


# Сценарии для экспериментов
cases = {
    "random": "Случайные ключи",
    "uniform": "Равномерно распределённые ключи",
    "sorted": "Ключи в порядке возрастания"
}

tree_sizes = list(range(1, 101,5))  # Количество ключей от 1 до 100

# Хранилище результатов для всех сценариев
results = {}

# Основной цикл для каждого сценария
for case, label in cases.items():
    heights = []
    for size in tree_sizes:
        tree = BST()
        keys = generate_keys(case, size)
        for key in keys:
            tree.insert(int(key))
        heights.append(tree.get_height())
    results[case] = heights

# Построение общего графика
plt.figure(figsize=(10, 6))

for case, label in cases.items():
    heights = results[case]
    plt.scatter(tree_sizes, heights, label=f'{label} (данные)', s=10)

    if case == "random":
        # Логарифмическая регрессия
        popt, _ = curve_fit(log_model, tree_sizes, heights)
        a, b = popt
        fitted_heights = log_model(np.array(tree_sizes), a, b)
        plt.plot(tree_sizes, fitted_heights, label=f'{label}', color='red')
    else:
        # Линейная регрессия
        X = np.array(tree_sizes).reshape(-1, 1)
        y = np.array(heights)
        model = LinearRegression()
        model.fit(X, y)
        a = model.coef_[0]
        b = model.intercept_
        fitted_heights = model.predict(X)
        plt.plot(tree_sizes, fitted_heights, label=f'{label}')

# Настройки графика
plt.title('Зависимость высоты бинарного дерева от количества ключей в разных случаях')
plt.xlabel('Количество ключей')
plt.ylabel('Высота дерева')
plt.legend()
plt.grid(True)
plt.show()
