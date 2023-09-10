from typing import List

# https://leetcode.com/problems/k-radius-subarray-averages/
# Tags: Prefix Sum, Sliding Window
class Solution:
    
    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    #
    # Use a sliding window with prefix sum to find the averages
    # for each element in the array, given a k radius.
    def getAverages(self, nums: List[int], k: int) -> List[int]:
            numLen = len(nums)

            # if k is greater than the length of array of nums,
            # then the array should only return -1's
            if (numLen - 1 < k):
                 return [-1] * numLen

            # The window is i - k, i + k, and inclusive
            # of i itself:
            # [i - k, i, i + k]
            windowLen = (k * 2) + 1

            # build an output that defaults to -1 so that they are
            # automatically set. The first k elements and last k elements
            # are always -1, so only the elements in-between will
            # be a value other than -1
            output = [-1] * numLen

            # sum the elements in the initial window
            currSum = 0
            for i in range(0, min(numLen, windowLen)):
                 currSum += nums[i]

            left = 1
            right = windowLen
            x = k + 1

            # calculate the first known average in the output array,
            # given that the window length is smaller than the array length.
            if (windowLen <= numLen):
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