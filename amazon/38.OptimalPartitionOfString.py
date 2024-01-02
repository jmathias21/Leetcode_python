from typing import List

# https://leetcode.com/problems/optimal-partition-of-string/
# Tags: 
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: started 1:40
    def partitionStringUsingHashSet(self, s: str) -> int:
        partitions = [set()]

        for char in s:
            if char in partitions[-1]:
                partitions.append(set())
            partitions[-1].add(char)

        return len(partitions)
    
    def partitionString(self, s: str) -> int:
        last_seen = [-1] * 26
        count = 0
        substr_index = 0

        for i in range(len(s)):
            char_num = ord(s[i]) - ord('a')
            if last_seen[char_num] >= substr_index:
                count += 1
                substr_index = i
            last_seen[char_num] = i

        return count

        
solution = Solution()
answer = solution.partitionString("abacaba")
print(answer)