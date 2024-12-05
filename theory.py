import numpy as np
import matplotlib.pyplot as plt

n = np.linspace(1, 100,100)

binary_tree_height = n

avl_tree_height =(np.log(np.array(n)) / np.log(1.63)) + 1

rbt_tree_height = 2*np.log(np.array(n)+1)

plt.figure(figsize=(12, 6))
plt.plot(n, binary_tree_height, label="Бинарное дерево", color="red")
plt.plot(n, avl_tree_height, label="АВЛ-дерево", color="blue")
plt.plot(n, rbt_tree_height, label="Красно-черное дерево", color="green")

plt.title("Сравнение высот деревьев в зависимости от количества узлов", fontsize=14)
plt.xlabel("Количество узлов (n)", fontsize=12)
plt.ylabel("Высота дерева", fontsize=12)
plt.legend(fontsize=12)
plt.grid(True)
plt.xlim(0, 100)
plt.ylim(0, 100)
plt.show()
