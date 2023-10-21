
class TrieNode:
    def __init__(self):
        self.is_terminal = False
        self.children = {}

# Time: 23:00
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            
            node = node.children[char]
        node.is_terminal = True
        

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word) and node.is_terminal:
                return True

            if i >= len(word):
                return False

            if word[i] == ".":
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
            elif word[i] in node.children:
                if dfs(node.children[word[i]], i + 1):
                    return True
                
            return False
        
        return dfs(self.root, 0)

# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord("bad")
obj.addWord("dad")
obj.addWord("mad")
#p1 = obj.search("pad")
p1 = obj.search("bad")
p1 = obj.search(".ad")
p1 = obj.search("b..")