
class TrieNode:
    def __init__(self):
        self.is_terminal = False
        self.children = {}

# Time: 20:00
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for i, char in enumerate(word):
            if char not in node.children:
                node.children[char] = TrieNode()

            if i == len(word) - 1:
                node.children[char].is_terminal = True

            node = node.children[char]

    def search(self, word: str) -> bool:
        node = self.root
        for i, char in enumerate(word):
            if char not in node.children:
                return False
            
            if i == len(word) - 1:
                return node.children[char].is_terminal
            
            node = node.children[char]
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            
            node = node.children[char]

        return True


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("abc")
param_2 = obj.search("ab")
param_2 = obj.search("abc")
obj.insert("abcde")
param_2 = obj.search("abcde")
param_3 = obj.startsWith("ab")
donothing = 0