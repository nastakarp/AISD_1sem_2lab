#Прямой обход (Pre-order).
def dfs_preorder(node):
    result = []
    _dfs_preorder(node, result)
    return result

def _dfs_preorder(node, result):
    if node:
        result.append(node.key)  # Посетить узел
        _dfs_preorder(node.left, result)  # Обойти левое поддерево
        _dfs_preorder(node.right, result)  # Обойти правое поддерево


#Симметричный обход (In-order).
def dfs_inorder(node):

    result = []
    _dfs_inorder(node, result)
    return result

def _dfs_inorder(node, result):
    if node:
        _dfs_inorder(node.left, result)  # Обойти левое поддерево
        result.append(node.key)  # Посетить узел
        _dfs_inorder(node.right, result)  # Обойти правое поддерево


#Обратный обход (Post-order).
def dfs_postorder(node):

    result = []
    _dfs_postorder(node, result)
    return result

def _dfs_postorder(node, result):
    if node:
        _dfs_postorder(node.left, result)  # Обойти левое поддерево
        _dfs_postorder(node.right, result)  # Обойти правое поддерево
        result.append(node.key)  # Посетить узел
