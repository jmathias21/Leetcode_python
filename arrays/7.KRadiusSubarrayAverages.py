from typing import List

# https://leetcode.com/problems/k-radius-subarray-averages/
# Tags: Prefix Sum, Sliding Window
class Solution:
    
    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    def getAverages(self, nums: List[int], k: int) -> List[int]:
            numLen = len(nums)
            if (numLen - 1 < k):
                 return [-1] * numLen

            windowLen = (k * 2) + 1
            output = [-1] * numLen
            currSum = 0
            for i in range(0, min(numLen, windowLen)):
                 currSum += nums[i]

            left = 1
            right = windowLen
            x = k + 1

            if (right <= numLen):
                output[k] = int(currSum / windowLen)

            while (right < numLen):
                currSum += nums[right] - nums[left - 1]

                output[x] = int(currSum / windowLen)

                x += 1
                left += 1
                right += 1

            return output

solution = Solution()
answer = solution.getAverages([100000], 0)
answer = solution.getAverages([8], 10000)
answer = solution.getAverages([7,4,3,9,1,8,5,2,6], 3)
print(answer)