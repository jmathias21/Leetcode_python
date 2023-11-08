import random

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# https://leetcode.com/problems/insert-delete-getrandom-o1/
# Tags: O(1) list deletion
# Time: Not timed
class RandomizedSet:

    def __init__(self):
        self.map = {}
        self.nums = []
        

    # Runtime Complexity: O(1)
    def insert(self, val: int) -> bool:
        if val not in self.map:
            self.nums.append(val)
            self.map[val] = len(self.nums) - 1
            return True
        return False
        

    # Runtime Complexity: O(1)
    def remove(self, val: int) -> bool:
        if val in self.map:
            i = self.map[val]
            self.nums[i] = self.nums[-1]
            self.map[self.nums[i]] = i
            self.nums.pop()
            del self.map[val]
            return True
        return False
        

    # Runtime Complexity: O(1)
    def getRandom(self) -> int:
        rand = random.randint(0, len(self.map) - 1)
        return self.nums[rand]

        


obj = RandomizedSet()
p1 = obj.insert(1)
p4 = obj.remove(2)
p4 = obj.insert(2)
p4 = obj.remove(1)
p4 = obj.insert(2)
p5 = obj.getRandom()
do = 0