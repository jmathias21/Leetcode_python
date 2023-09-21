from typing import List

# https://leetcode.com/problems/two-sum/
# Tags: hashing, hashmap, complement
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    def twoSumUsingHashMap(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i, num in enumerate(nums):
            # if current num is in hashmap, it means it matches
            # a complement in the hash map. That means i represents
            # the index of the complement, and the value associated
            # with the complement represents the original index
            if num in hashMap:
                return [i, hashMap[num]]

            # store complement as key and current index as value
            hashMap[target - num] = i

        return []
    
    # Runtime Complexity: O(n log n)
    # Space Complexity: O(1)
    def twoSumUsingTwoPointers(self, nums: List[int], target: int) -> List[int]:
        nums.sort() # worst case of O(n log n)
        left = 0
        right = len(nums) - 1

        while left < right:
            s = nums[left] + nums[right]
            if s < target:
                left += 1
            elif s > target:
                right -= 1
            else:
                return [left + 1, right + 1]


        
solution = Solution()
answer = solution.twoSumUsingTwoPointers([2,7,11,15], 9)

answer = solution.twoSum([-1,-2,-3,-4,-5], -8)
print(answer)

answer = solution.twoSum([2,7,11,15], 9)
print(answer)

answer = solution.twoSum([3,2,4], 6)
print(answer)
