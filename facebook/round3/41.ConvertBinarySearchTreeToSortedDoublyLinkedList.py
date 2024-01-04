from typing import List, Optional

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 1:48
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        
        first = prev = None

        def dfs(node):
            if node is None:
                return
            
            dfs(node.left)

            nonlocal first, prev
            if prev:
                prev.right = node
                node.left = prev
            else:
                first = node
            prev = node

            dfs(node.right)

            return node
        
        dfs(root)
        first.left = prev
        prev.right = first
        return first

        
solution = Solution()
answer = solution.treeToDoublyList()
print(answer)