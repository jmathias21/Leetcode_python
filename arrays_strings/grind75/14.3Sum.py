from typing import List

# https://leetcode.com/problems/3sum/
# Tags: two pointers, two sum, 
class Solution:

    # Runtime Complexity: O(n^2)
    # Space Complexity: O(n)
    # Time: Not timed
    def threeSumUsingTwoPointers(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []

        for i in range(len(nums)):
            # if nums[i] is greater than 0, it means that the left and
            # right pointer values are always greater than 0. It follows
            # that the sum of all 3 is always greater than 0, therefore
            # we can exclude positive numbers
            if nums[i] > 0:
                break

            # as we loop through nums, ignore the current number if the
            # previous number is a duplicate
            if i != 0 and nums[i] == nums[i - 1]:
                continue

            # set the initial left and right index values. We always set
            # the left pointer to greater than our outer i loop because
            # otherwise we'd end up with duplicate triplets
            left, right = i + 1, len(nums) - 1

            # we initiate a subloop to walk the left and the right pointers
            # inward, while checking the sums. Once left > right, we know
            # we've checked all values
            while left < right:
                s = nums[i] + nums[left] + nums[right]

                if s < 0:
                    left += 1
                elif s > 0:
                    right -= 1
                else:
                    answer.append([nums[i], nums[left], nums[right]])

                    # move both pointers inward when we find a triplet. We also move
                    # the right pointer because otherwise the left pointer moving
                    # will either introduce a sum that is still equal to 0, which
                    # results in a duplicate. Or the sum increases, meaning that
                    # we need to move the right pointer anyway. Not moving the right
                    # pointer won't cause errors, but it is more efficient
                    left, right = left + 1, right - 1

                    # when we append a triplet to our answer, we want to make sure
                    # that we don't add dulicates if the next value of nums[left]
                    # is the same. But what if there's more than two, three, or four
                    # duplicate values? For that reason, we keep looping until we
                    # find a safe left index
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return answer

    # Runtime Complexity: O(n^2)
    # Space Complexity: O(n)
    # Time: Not timed
    def threeSumUsingHashMap(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i != 0 and nums[i] == nums[i - 1]:
                continue

            hashMap = {}

            j = i + 1
            while j < len(nums):
                if nums[j] in hashMap:
                    answer.append([nums[i], nums[hashMap[nums[j]]], nums[j]])
                    while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                        j += 1

                hashMap[-nums[i] - nums[j]] = j
                j += 1

        return answer
        
solution = Solution()
#answer = solution.threeSumUsingHashMap([0,0,0])
answer = solution.threeSumUsingHashMap([-1,0,1,2,-1,-4])
answer = solution.threeSum([-4,-3,-2,-1,0,1,2,3,4])
print(answer)

# Example for threeSumUsingTwoPointers
# [-1,0,1,2,-1,-4]
# sort: [-4,-1,-1,0,1,2]

# [-4,-1,-1,0,1,2]
#  ^  ^         ^
#  i  L         R
# sum = -3
# sum < 0, so we move the left pointer forward

# [-4,-1,-1,0,1,2]
#  ^     ^      ^
#  i     L      R
# sum = -3
# sum < 0, so we move the left pointer forward

# [-4,-1,-1,0,1,2]
#  ^        ^   ^
#  i        L   R
# sum = -2
# sum < 0, so we move the left pointer forward

# [-4,-1,-1,0,1,2]
#  ^          ^ ^
#  i          L R
# sum = -1
# sum < 0, so we move the left pointer forward

# left == right, so we move i forward and reset
# [-4,-1,-1,0,1,2]
#     ^  ^      ^
#     i  L      R
# sum = 0
# sum == 0, so we append our triplet to our answer
# answer = [[-1, -1, 2]]

# [-4,-1,-1,0,1,2]
#     ^     ^ ^
#     i     L R
# sum = 0
# sum == 0, so we append our triplet to our answer
# answer = [[-1, -1, 2], [-1, 0, 1]]
#
# etc... We keep going until nums[i] > 0
# final answer: [[-1, -1, 2], [-1, 0, 1]]

