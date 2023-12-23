from typing import List

class TrieNode:
    def __init__(self):
        self.is_terminal = False
        self.children = {}

# https://leetcode.com/problems/concatenated-words/
# Tags: 
class Solution:

    # Runtime Complexity: O(N log N + S) where N is the number of words, and S is the total number of chars in all words
    # Space Complexity: O(S)
    # Time: Not timed
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words.sort(key=lambda x: len(x))
        root = TrieNode()

        def add_word(root, word):
            node = root
            for char in word:
                if char not in node.children:
                    new_node = TrieNode()
                    node.children[char] = new_node
                node = node.children[char]
            node.is_terminal = True

        def can_form_word(word, index, word_count):
            if index == len(word):
                return word_count >= 2
            
            node = root
            for i in range(index, len(word)):
                if word[i] in node.children:
                    node = node.children[word[i]]
                    if node.is_terminal:
                        if can_form_word(word, i + 1, word_count + 1):
                            return True
                else:
                    break
            return False

        output = []
        for word in words:
            if len(word) > 0:
                if can_form_word(word, 0, 0):
                    output.append(word)
                else:
                    add_word(root, word)
        return output

        
solution = Solution()
answer = solution.findAllConcatenatedWordsInADict(["a","b","ab","abc"])
answer = solution.findAllConcatenatedWordsInADict(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"])
print(answer)