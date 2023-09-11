from typing import List

# https://leetcode.com/problems/two-sum/
# Tags: hashing, hashmap, complement
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
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

        
solution = Solution()
answer = solution.twoSum([-1,-2,-3,-4,-5], -8)
print(answer)

answer = solution.twoSum([2,7,11,15], 9)
print(answer)

answer = solution.twoSum([3,2,4], 6)
print(answer)