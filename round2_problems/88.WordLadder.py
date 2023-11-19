from collections import defaultdict, deque
from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: 24:00
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        intermediate_map = defaultdict(set)

        # O(wordList * max(word_length))
        for word in wordList:
            for i in range(len(word)):
                intermediate_word = word[:i] + "*" + word[i + 1:]
                intermediate_map[intermediate_word].add(word)

        queue = deque([(beginWord, 0)])
        seen = set()

        while queue:
            w, depth = queue.popleft()

            if w in seen:
                continue

            if w == endWord:
                return depth + 1

            seen.add(w)
            for i in range(len(w)):
                intermediate_word = w[:i] + "*" + w[i + 1:]
                for word in intermediate_map[intermediate_word]:
                    queue.append((word, depth + 1))

        return 0
        
solution = Solution()
answer = solution.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"])
print(answer)