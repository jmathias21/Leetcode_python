from collections import Counter, defaultdict
import heapq

# https://leetcode.com/problems/reorganize-string/
# Tags: Heap, Hash Map
class Solution:

    # Runtime Complexity: O(n logk)
    # Space Complexity: O(k)
    # Time: Not timed
    def reorganizeStringUsingHeap(self, s: str) -> str:
        frequencies = Counter(s)
        heap = []
        
        for char, freq in frequencies.items():
            heapq.heappush(heap, (-freq, char))

        output = []
        while heap:
            freq, char = heapq.heappop(heap)

            # if the highest frequency character wasn't added last, add it
            if not output or output[-1] != char:
                output.append(char)
                freq += 1
            elif heap:
                next_freq, next_char = heapq.heappop(heap)
                output.append(next_char)
                next_freq += 1
                if next_freq != 0:
                    heapq.heappush(heap, (next_freq, next_char))
            else:
                return ""

            if freq != 0:
                heapq.heappush(heap, (freq, char))

        return "".join(output)
    
    # Runtime Complexity: O(n)
    # Space Complexity: O(k)
    # Time: Not timed
    def reorganizeStringUsingEvensOdds(self, s: str) -> str:
        output = [''] * len(s)
        frequencies = defaultdict(int)
        max_char = None
        max_freq = float('-inf')

        for char in s:
            frequencies[char] += 1
            if frequencies[char] > max_freq:
                max_freq = frequencies[char]
                max_char = char

        if max_freq > (len(s) + 1) // 2:
            return ""

        # populate even spaces with most frequent character
        index = 0
        while frequencies[max_char] > 0:
            output[index] = max_char
            frequencies[max_char] -= 1
            index += 2

        # populate odd spaces up to max freq
        for char, freq in frequencies.items():
            while freq > 0:
                # start populating odd spaces if all even's filled out
                if index >= len(s):
                    index = 1
                output[index] = char
                index += 2
                freq -= 1

        return "".join(output)
         
        
solution = Solution()
# answer = solution.reorganizeStringUsingEvensOdds("vvvlo")
answer = solution.reorganizeStringUsingEvensOdds("aaaabbcccc")
answer = solution.reorganizeStringUsingEvensOdds("aaaaabcc")
answer = solution.reorganizeStringUsingEvensOdds("aaabcc")
print(answer)