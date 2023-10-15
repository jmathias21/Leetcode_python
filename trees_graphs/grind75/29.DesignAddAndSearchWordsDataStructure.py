class TrieNode:
    def __init__(self):
        self.is_terminal = False
        self.children = {}

# https://leetcode.com/problems/design-add-and-search-words-data-structure/
# Tags: 
# Time: 35:00
# Space Complexity: O(M)
#
# Uses a prefix tree (trie) to add and find words. We combine this with backtracking when searching
# to allow wildcard searches
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    # Runtime Complexity: O(M) where M is the length of the word
    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]

        node.is_terminal = True

    # Runtime Complexity: O(26 ^ M) where M is the length of the word
    def search(self, word: str) -> bool:
        return self.backtrack(word, 0, self.root)
    
    def backtrack(self, word, i, node):
        if i == len(word):
            return node.is_terminal
        
        # if we see a ".", then we want to recursively search all children
        if word[i] == ".":
            for child_char in node.children:
                if self.searchHelper(word, i + 1, node.children[child_char]):
                    return True
        else:
            if word[i] in node.children and self.searchHelper(word, i + 1, node.children[word[i]]):
                return True
                
        return False


# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord("at")
obj.addWord("and")
obj.addWord("an")
obj.addWord("add")
p1 = obj.search("a")
p2 = obj.search(".at")

obj2 = WordDictionary()
obj2.addWord("base")
obj2.addWord("ball")
p1 = obj2.search("ba.e")

# Example:

#     b
#     |
#     a
#    / \
#   s   l
#   |   |
#   e   l

# search("ba.l") returns true