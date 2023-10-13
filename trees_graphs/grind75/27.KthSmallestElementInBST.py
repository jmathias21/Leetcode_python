class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# Tags: Recursive DFS, Iterative DFS, In-order traversal
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: 28:00
    def kthSmallestUsingRecursiveInorderDFS(self, root, k):
        def inorder(r):
            if r is None:
                return []

            left = inorder(r.left)
            right = inorder(r.right)

            return left + [r.val] + right
    
        return inorder(root)[k - 1]
    
    # Runtime Complexity: O(H + K)
    # Space Complexity: O(H)
    # Time: Not timed
    def kthSmallestUsingIterativeInorderDFS(self, root, k):
        stack = []

        while True:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right

        
solution = Solution()
answer = solution.kthSmallestUsingIterativeInorderDFS(TreeNode(5, TreeNode(3, TreeNode(1, TreeNode(0), TreeNode(2)), TreeNode(4)), TreeNode(6)), 4)
answer = solution.kthSmallestUsingIterativeInorderDFS(TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4)))
print(answer)