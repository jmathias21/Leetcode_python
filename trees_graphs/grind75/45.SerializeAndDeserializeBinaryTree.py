from collections import deque

class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
# Tags: DFS, BFS, Serialization, Deserialization
# Time: 25:00
class Codec:

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def serializeUsingDFS(self, root):
        output = []

        def dfs(node):
            output.append(str(node.val) if node else 'None')

            if node is None:
                return

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(output)

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def deserializeUsingDFS(self, data):
        data = deque(data.split(","))
        def dfs():
            node = TreeNode(data.popleft())

            if node.val == "None":
                return
            
            if data:
                node.left = dfs()
            if data:
                node.right = dfs()

            return node
        return dfs()
    
    
    def serializeUsingBFS(self, root):
        output = []

        def dfs(node, depth):
            if depth == len(output):
                output.append([])
            
            output[depth].extend([str(node.val) if node else "None"])

            if node is None:
                return

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return ",".join([item for sublist in output for item in sublist])

    def deserializeUsingBFS(self, data):
        data = deque(data.split(","))

        if data[0] == "None":
            return None

        root = TreeNode(data[0])
        queue = deque([root])
        data.popleft()

        while queue:
            node = queue.popleft()

            if not data:
                continue

            left_val, right_val = data.popleft(), data.popleft()
            if left_val != "None":
                node.left = TreeNode(left_val)
                queue.append(node.left)
            if right_val != "None":
                node.right = TreeNode(right_val)
                queue.append(node.right)
        
        return root


ser = Codec()
deser = Codec()
ans1 = deser.deserializeUsingBFS(ser.serializeUsingBFS(None))
ans1 = deser.deserializeUsingBFS(ser.serializeUsingBFS(TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))))
do = 0