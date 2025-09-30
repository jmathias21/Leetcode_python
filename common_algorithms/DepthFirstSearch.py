from typing import List, Set, Dict, Optional

class Node:
    def __init__(self, val):
        self.val = val
        self.left = left
        self.right = right

class DepthFirstSearch:
    """
    Simple Depth-First Search implementations for various data structures
    """
    def dfs(root, result: Optional[List] = None) -> List:
        if result is None:
            result = []
        
        if root:
            result.append(root.val)
            dfs(root.left, result)
            dfs(root.right, result)
        
        return result

