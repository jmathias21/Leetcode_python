from collections import defaultdict, deque
from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(n * m^2)
    # Space Complexity: O()
    # Time: started 8:11
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        interm_words = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                interm_words[word[:i] + '*' + word[i + 1:]].append(word)

        queue = deque([(beginWord, 1)])

        visited = set()
        while queue:
            word, depth = queue.popleft()

            if word == endWord:
                return depth

            if word in visited:
                continue

            visited.add(word)

            for i in range(len(word)):
                interm = word[:i] + '*' + word[i + 1:]
                for w in interm_words[interm]:
                    queue.append((w, depth + 1))
        return 0

        
solution = Solution()
answer = solution.ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"])
print(answer)