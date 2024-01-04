from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: started 1:27
    def maximumSwap(self, num: int) -> int:
        nums = list(str(num))

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                right_max = nums[i]
                right_max_index = i
                # find max to right
                for j in range(i, len(nums)):
                    if nums[j] >= right_max:
                        right_max = nums[j]
                        right_max_index = j
                for j in range(i):
                    if nums[j] < right_max:
                        nums[j], nums[right_max_index] = nums[right_max_index], nums[j]
                        break
                break

        return int("".join(nums))



        
solution = Solution()
answer = solution.maximumSwap(10909091)
answer = solution.maximumSwap(1993) # 9913
answer = solution.maximumSwap(98368) # 98863
print(answer)