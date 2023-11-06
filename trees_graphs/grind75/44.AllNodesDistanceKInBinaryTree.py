from collections import defaultdict
from typing import List

class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
# Tags: Adjacency list, Graph, DFS
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: Not timed
    #
    # Build adjacency list from tree. Starting at target node, search through adjacency list for
    # nodes that are k distance away
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        adj = defaultdict(list)
        answer = []

        def buildAdj(node, parent):
            if parent is not None:
                adj[node.val].append(parent.val)

            if node.left:
                adj[node.val].append(node.left.val)
                buildAdj(node.left, node)
            if node.right:
                adj[node.val].append(node.right.val)
                buildAdj(node.right, node)

        def search(node, dist):
            if dist == k:
                answer.append(node)

            seen.add(node)
            for neighbor in adj[node]:
                if neighbor in seen:
                    continue

                search(neighbor, dist + 1)

        seen = set()
        buildAdj(root, None)
        search(target.val, 0)

        return answer
        
solution = Solution()
answer = solution.distanceK(TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))),
                                     TreeNode(1, TreeNode(0), TreeNode(8))), TreeNode(5), 2)
print(answer)