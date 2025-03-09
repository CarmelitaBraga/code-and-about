visited = set()

def dfs(node):
    if not node or node in visited:
        return
    
    visited.add(node)
    dfs(node.left)
    dfs(node.right)
