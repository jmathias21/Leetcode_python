from collections import Counter, defaultdict, deque
from typing import List

# https://leetcode.com/problems/alien-dictionary/
# Tags: Kadane's algorithm for topological sorting, BFS
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: Not timed
    def alienOrder(self, words: List[str]) -> str:
        adj = defaultdict(set)
        in_degree = Counter({c : 0 for word in words for c in word})

        for first_word, second_word in zip(words, words[1:]):
            for c, d, in zip(first_word, second_word):
                if c != d:
                    if d not in adj[c]:
                        adj[c].add(d)
                        in_degree[d] += 1
                    break
            else:
                # check if second word is a prefix of the first word. e.g. ["ab", "a"]
                if len(second_word) < len(first_word):
                    return ""

        queue = deque([c for c in in_degree if in_degree[c] == 0])

        output = []
        while queue:
            c = queue.popleft()
            output.append(c)
            for neighbor in adj[c]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # check for cycle. e.g. ["abc", "ab", "abc"]
        return "".join(output) if len(output) == len(in_degree) else ""

        
solution = Solution()
answer = solution.alienOrder(["ozvcdpgfq","mridvkklqj","dpwecbwor","xxtistijm","xxuon","tudbazpggu","hnuumktbjy","bogbcoi"])
answer = solution.alienOrder(["ab","adc"])
answer = solution.alienOrder(["wrt","er","ct","cw","cd","cwe","cewew","cewed"])
answer = solution.alienOrder(["wrt","wrf","er","ett","rftt"])
answer = solution.alienOrder(["z","x"])
answer = solution.alienOrder(["z","x","z"])
print(answer)