class TrieNode:
    def __init__(self):
        self.is_terminal = False
        self.children = {}

# https://leetcode.com/problems/implement-trie-prefix-tree/
# Tags: 
# Time: Not timed
class Trie:

    def __init__(self):
        self.root = TrieNode()

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    def insert(self, word: str) -> None:
        node = self.root

        for char in word:
            # if the current node doesn't have any children, add the
            # character as a child
            if char not in node.children:
                node.children[char] = TrieNode()

            # point the current node at the child with the given character
            node = node.children[char]

        # the last character of the passed in word is the terminal node
        node.is_terminal = True

    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    def search(self, word: str) -> bool:
        node = self.findNode(word)
        return node is not None and node.is_terminal
        
    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    def startsWith(self, prefix: str) -> bool:
        return self.findNode(prefix) is not None

    def findNode(self, word: str):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return None
            
        return node

        
obj = Trie()
obj.insert("apple")
param_1 = obj.search("apple") # return true
param_1 = obj.search("appler") # return false
param_2 = obj.search("app") # return false
param_3 = obj.startsWith("app") # return true
obj.insert("app")
param_4 = obj.search("app") # return true

# Example:

# insert "apple"
# root
#  |
#  a
#  |
#  p
#  |
#  p
#  |
#  l
#  |
#  e <-- terminal

# insert "ape"
# root
#  |
#  a
#  |
#  p 
#  |\
#  p e  <-- terminal
#  |
#  l
#  |
#  e <-- terminal