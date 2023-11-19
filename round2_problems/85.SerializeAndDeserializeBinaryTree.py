class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

# Time: 35:00
class Codec:

    def serialize(self, root):
        serialized = []

        def dfs(node):
            serialized.append(str(node.val) if node is not None else "None")

            if node is None:
                return

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(serialized)
        

    def deserialize(self, data):
        d = data.split(',')

        def dfs(i):
            if d[i] == "None" or i >= len(d):
                return None, i + 1
            
            node = TreeNode(int(d[i]))

            node.left, i = dfs(i + 1)
            node.right, i = dfs(i)

            return node, i

        return dfs(0)[0]
        

ser = Codec()
deser = Codec()
#ans = ser.serialize(TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5))))
ans = deser.deserialize(ser.serialize(TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4, TreeNode(6), TreeNode(7)), TreeNode(5)))))
do = 0