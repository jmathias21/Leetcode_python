from typing import List

class Solution(object):
    def twoSum(self, nums, target):
        d = {}
        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in d:
                return [i, hashmap[complement]]
            else:
                d[nums[i]] = i
        

solution = Solution()
print(solution.twoSum([2,7,11,15], 9))