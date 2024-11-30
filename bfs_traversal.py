#обход в ширину
from collections import deque

def bfs(node):
    if node is None:
        return []

    result = []
    queue = deque([node])

    while queue:
        current = queue.popleft()

        if current:  # Проверяем, что узел существует
            result.append(current.key)  # Добавляем ключ узла в результат
            if current.left or current.right:  # Добавляем только не пустые узлы
                queue.append(current.left)
                queue.append(current.right)

    return result
