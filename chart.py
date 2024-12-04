from BST.BST import BST
from AVL.AVL import AVLTree
from RBT.RBT import RBTree

import matplotlib.pyplot as plt
import random
import numpy as np
from scipy.optimize import curve_fit

# Функции для измерения высоты деревьев
def measure_height_bst(n):
    """Измерение высоты BST дерева с n узлами."""
    bst = BST()  # Создаем экземпляр BST
    keys = random.sample(range(1, 10000), n)  # Генерируем n уникальных ключей
    for key in keys:
        bst.insert(key)  # Вставляем ключи в дерево
    return bst.get_height()  # Используем метод get_height из BST

def measure_height_avl(n):
    """Измерение высоты AVL дерева с n узлами."""
    avl =AVLTree()  # Создаем экземпляр AVL
    keys = random.sample(range(1, 10000), n)  # Генерируем n уникальных ключей
    for key in keys:
        avl.insert(key)  # Вставляем ключи в дерево
    return calculate_height(avl.root)  # Возвращаем высоту дерева

def measure_height_rb(n):
    """Измерение высоты Red-Black дерева с n узлами."""
    rb = RBTree() # Создаем экземпляр RBT
    keys = random.sample(range(1, 10000), n)  # Генерируем n уникальных ключей
    for key in keys:
        rb.insert(key)  # Вставляем ключи в дерево
    return calculate_height(rb.root)  # Возвращаем высоту дерева

def calculate_height(node):
    """Рекурсивное вычисление высоты дерева."""
    if node is None:
        return 0
    left_height = calculate_height(node.left)
    right_height = calculate_height(node.right)
    return max(left_height, right_height) + 1

# Сбор данных
n_values = list(range(10, 500, 50))  # Количество узлов (10, 60, 110, ...)
bst_heights = [measure_height_bst(n) for n in n_values]
avl_heights = [measure_height_avl(n) for n in n_values]
rb_heights = [measure_height_rb(n) for n in n_values]

# Логарифмическая модель для регрессии
def log_model(x, a, b):
    return a * np.log(x) + b

# Функция для вычисления регрессии и построения кривой
def plot_log_regression(x, y, label, color):
    """Построение логарифмической регрессии."""
    popt, _ = curve_fit(log_model, x, y)
    plt.plot(x, log_model(np.array(x), *popt), linestyle='--', color=color, label=f'{label} Log Regression')
    return popt

# Построение графиков
plt.figure(figsize=(10, 6))
plt.scatter(n_values, bst_heights, label='BST Heights', color='blue')  # Точки для BST
plot_log_regression(n_values, bst_heights, 'BST', 'blue')

plt.scatter(n_values, avl_heights, label='AVL Heights', color='green')  # Точки для AVL
plot_log_regression(n_values, avl_heights, 'AVL', 'green')

plt.scatter(n_values, rb_heights, label='Red-Black Heights', color='red')  # Точки для Red-Black
plot_log_regression(n_values, rb_heights, 'Red-Black', 'red')

# Настройки графика
plt.xlabel('Количество узлов')
plt.ylabel('Высота дерева')
plt.title("Зависимость высоты дерева от количества узлов")
plt.legend()
plt.grid(True)
plt.show()
