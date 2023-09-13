# https://leetcode.com/problems/first-bad-version/
# Tags: 
class Solution:

    # The returned bad version is just an example. In leetcode,
    # firstBadVersion will use their isBadVersion API instead
    def isBadVersion(self, version: int) -> bool:
        return version >= 4

    # Runtime Complexity: O(log n)
    # Space Complexity: O(1)
    # Time: 20:30
    #
    # Performs a binary search to find the very first bad version
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n

        while (left < right):
            mid = int((left + right) / 2)
            if self.isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return left
        
        
solution = Solution()
answer = solution.firstBadVersion(7)
print(answer)