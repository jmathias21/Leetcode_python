# https://leetcode.com/problems/count-and-say/
# Tags: 
class Solution:

    # Runtime Complexity: O(4^(n / 3))
    # Space Complexity: O(4^(n / 3))
    # Time: Not timed
    def countAndSay(self, n: int) -> str:
        s = "1"

        for _ in range(n - 1):
            numbers = [s[0]]
            counts = [0]
            for i in range(len(s)):
                if s[i] == numbers[-1]:
                    counts[-1] += 1
                else:
                    counts.append(1)
                    numbers.append(s[i])
            s = ""
            for i in range(len(numbers)):
                s += str(counts[i]) + numbers[i]

        return s

        
solution = Solution()
answer = solution.countAndSay(4)
print(answer)

# countAndSay(1) = "1"
# countAndSay(2) = say "1" = one 1 = "11"
# countAndSay(3) = say "11" = two 1's = "21"
# countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"