from typing import Optional

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: Not timed
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        first, last = None, None

        def dfs(node):
            if node is None:
                return

            dfs(node.left)

            nonlocal first, last
            if last:
                last.right = node
                node.left = last
            else:
                first = node
            last = node

            dfs(node.right)

            return node
            
        dfs(root)
        first.left = last
        last.right = first
        return first


        
solution = Solution()
# answer = solution.treeToDoublyList(Node(5, Node(2, Node(1), Node(4, Node(3))), Node(6)))
answer = solution.treeToDoublyList(Node(4, Node(2, Node(1), Node(3)), Node(5)))
print(answer)