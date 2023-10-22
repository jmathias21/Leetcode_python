from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# https://leetcode.com/problems/maximum-width-of-binary-tree/
# Tags: Level order traversal, BFS
class Solution:

    # Runtime Complexity: O(N)
    # Space Complexity: O(N)
    # Time: Not timed
    #
    # To find the max width of a binary tree:
    # 1. Initialize a queue for level-order traversal, beginning with the root node and its column index.
    # 2. For each level:
    #    a. Record the smallest column index at the start of the level.
    #    b. Process each node at that level:
    #       - Remove the node from the queue.
    #       - Add its left child with column index = 2 * parent's column index.
    #       - Add its right child with column index = (2 * parent's column index) + 1.
    #    c. After processing all nodes at the level, compute the width of that level as (largest column index - smallest column index) + 1 and update the max_width.
    # 3. Return the max_width.
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root: return 0

        max_width = 0
        queue = deque([(root, 0)])

        while queue:
            level_node_count = len(queue)

            level_smallest_col_index = queue[0][1]

            # process each node at the current level and add children nodes back to queue with
            # new col indexes that will be processed in the next level
            for i in range(level_node_count):
                node, col_index = queue.popleft()

                if node.left:
                    queue.append((node.left, 2 * col_index))

                if node.right:
                    queue.append((node.right, (2 * col_index) + 1))

            max_width = max(max_width, (col_index - level_smallest_col_index) + 1)

        return max_width

        
solution = Solution()
answer = solution.widthOfBinaryTree(TreeNode(1, TreeNode(3, TreeNode(5, TreeNode(6))), TreeNode(2, None, TreeNode(9, TreeNode(7)))))
print(answer)