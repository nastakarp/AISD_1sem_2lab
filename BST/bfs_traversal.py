#обход в ширину
from collections import deque

def bfs(node):
    """Обход в ширину (Breadth-First Search)."""
    if node is None:
        return []

    result = []
    queue = deque([node])  # Используем очередь для обхода

    while queue:
        current = queue.popleft()  # Извлекаем узел из очереди
        result.append(current.key)  # Добавляем ключ узла в результат

        # Добавляем дочерние узлы в очередь, если они существуют
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return result
