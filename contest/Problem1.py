from typing import List
import heapq


class Solution:

    def numberGame(self, nums: List[int]) -> List[int]:
        output = []
        heapq.heapify(nums)

        while nums:
            alice = heapq.heappop(nums)
            bob = heapq.heappop(nums)

            output.append(bob)
            output.append(alice)

        return output


        
solution = Solution()
answer = solution.numberGame([5,4,2,3])
print(answer)

# Input: nums = [5,4,2,3]
# Output: [3,2,5,4]
# Explanation: In round one, first Alice removes 2 and then Bob removes 3. Then in arr firstly Bob appends 3 and then Alice appends 2. So arr = [3,2].
# At the begining of round two, nums = [5,4]. Now, first Alice removes 4 and then Bob removes 5. Then both append in arr which becomes [3,2,5,4].