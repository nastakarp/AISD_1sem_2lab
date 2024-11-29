from BST import BST
from AVL import AVLTree
from RBT import RBTree

import matplotlib.pyplot as plt
import random
import numpy as np
from scipy.optimize import curve_fit

# Функции для измерения высоты деревьев (например, для BST, AVL и RB)
def measure_height_bst(n):
    bst = BST()
    keys = random.sample(range(1, 10000), n)
    for key in keys:
        bst.insert(key)
    return calculate_height(bst.root)

def measure_height_avl(n):
    avl = AVLTree()
    keys = random.sample(range(1, 10000), n)
    for key in keys:
        avl.insert(key)
    return calculate_height(avl.root)

def measure_height_rb(n):
    rb = RBTree()
    keys = random.sample(range(1, 10000), n)
    for key in keys:
        rb.insert(key)
    return calculate_height(rb.root)

def calculate_height(node):
    if node is None:
        return 0
    left_height = calculate_height(node.left)
    right_height = calculate_height(node.right)
    return max(left_height, right_height) + 1

# Сбор данных
n_values = [i for i in range(10, 500, 50)]
bst_heights = [measure_height_bst(n) for n in n_values]
avl_heights = [measure_height_avl(n) for n in n_values]
rb_heights = [measure_height_rb(n) for n in n_values]

# Логарифмическая модель
def log_model(x, a, b):
    return a * np.log(x) + b

# Функция для вычисления регрессии и построения кривой
def plot_log_regression(x, y, label):
    # Применяем логарифмическую регрессию
    popt, _ = curve_fit(log_model, x, y)
    plt.plot(x, log_model(x, *popt), label=f'{label} Log Regression', linestyle='--')
    return popt

# Построение графиков
plt.scatter(n_values, bst_heights, label='BST', color='blue')  # Используем scatter для точек
plot_log_regression(n_values, bst_heights, 'BST')

plt.scatter(n_values, avl_heights, label='AVL', color='green')  # Используем scatter для точек
plot_log_regression(n_values, avl_heights, 'AVL')

plt.scatter(n_values, rb_heights, label='Red-Black', color='red')  # Используем scatter для точек
plot_log_regression(n_values, rb_heights, 'Red-Black')

plt.xlabel('Количество узлов')
plt.ylabel('Высота дерева')
plt.title("Зависимость высоты  от кол-ва узлов для различных типов деревьев")
plt.legend()
plt.show()
