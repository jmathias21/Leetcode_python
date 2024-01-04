# https://leetcode.com/problems/maximum-swap/
# Tags: 
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: Not timed
    def maximumSwap(self, num: int) -> int:
        if num <= 10:
            return num
        
        s = list(str(num))
        max_val = "0"
        max_index = -1

        for i in range(1, len(s)):
            if s[i] > s[i - 1]:
                j = i
                while j < len(s):
                    if max_val <= s[j]:
                        max_val = s[j]
                        max_index = j
                    j += 1
                if max_index != -1:
                    for k in range(i):
                        if s[k] < max_val:
                            s[k], s[max_index] = s[max_index], s[k]
                            return int("".join(s))

        return num

        
solution = Solution()
answer = solution.maximumSwap(1993) # 9913
answer = solution.maximumSwap(98368) # 98863
answer = solution.maximumSwap(5) # 5
answer = solution.maximumSwap(12) # 21
print(answer)