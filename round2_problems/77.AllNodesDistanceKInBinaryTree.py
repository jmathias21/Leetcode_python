from collections import defaultdict, deque
from typing import List

class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: 30:00
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        answer = []

        adj = defaultdict(set)
        def dfs(node, parent):
            if parent:
                adj[node.val].add(parent.val)
            if node.left:
                adj[node.val].add(node.left.val)
                dfs(node.left, node)
            if node.right:
                adj[node.val].add(node.right.val)
                dfs(node.right, node)

        dfs(root, None)

        queue = deque([(target.val, 0)])
        seen = set()

        while queue:
            n, depth = queue.popleft()

            if n in seen:
                continue

            if depth == k:
                answer.append(n)
                continue

            seen.add(n)
            for neighbor in adj[n]:
                queue.append((neighbor, depth + 1))

        return answer


        
solution = Solution()
answer = solution.distanceK(TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(0), TreeNode(8))), TreeNode(5), 2)
print(answer)