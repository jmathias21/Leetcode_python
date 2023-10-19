from collections import defaultdict
from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: 29:00
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_len = len(p)

        if p_len > len(s):
            return []

        s_dict = {}
        p_dict = defaultdict(int)
        answer = []

        for char in p:
            p_dict[char] += 1

        for i in range(p_len):
            if s[i] not in s_dict:
                s_dict[s[i]] = 0

            s_dict[s[i]] += 1

        i = p_len
        while True:
            if s_dict == p_dict:
                answer.append(i - p_len)

            if i >= len(s):
                break

            s_dict[s[i - p_len]] -= 1
            if s_dict[s[i - p_len]] == 0:
                s_dict.pop(s[i - p_len], None)

            if s[i] not in s_dict:
                s_dict[s[i]] = 0

            s_dict[s[i]] += 1
            i += 1

        return answer

        
solution = Solution()
answer = solution.findAnagrams("abacbabc", "abc")
answer = solution.findAnagrams("cbaebabacd", "abc")
print(answer)