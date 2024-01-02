from collections import defaultdict, deque
from typing import List

# https://leetcode.com/problems/word-ladder/
# Tags: 
class Solution:

    # Runtime Complexity: O(m^2 * n)
    # Space Complexity: O(m^2 + n)
    # Time: 20:00
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        d = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                d[word[:i] + '*' + word[i + 1:]].append(word)

        queue = deque([(beginWord, 1)])

        seen = set()
        while queue:
            word, depth = queue.popleft()

            if word in seen:
                continue

            if word == endWord:
                return depth

            seen.add(word)
            for i in range(len(word)):
                interm = word[:i] + '*' + word[i + 1:]
                for w in d[interm]:
                    queue.append((w, depth + 1))

        return 0

        
solution = Solution()
answer = solution.ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"])
print(answer)