#обход в ширину
from collections import deque

def bfs(node):
    if node is None:
        return []

    result = []
    queue = deque([node])

    while queue:
        current = queue.popleft()

        if current:
            result.append(current.key)
            if current.left or current.right:
                queue.append(current.left)
                queue.append(current.right)

    return result
