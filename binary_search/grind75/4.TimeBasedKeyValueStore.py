from sortedcontainers import SortedDict

# https://leetcode.com/problems/time-based-key-value-store/
# Tags: 
# Time: Not timed
#
# Uses a standard hash map to store the keys, and then a SortedDict for the timestamp keys and values.
# We use bisect_right to perform a binary search on the timestamps to return the value associated with
# the timestamp (or the next lowest timestamp)
class TimeMap:

    def __init__(self):
        self.time_map = {}
        

    # Runtime Complexity: O(1)
    # Space Complexity: O(n)
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key] = SortedDict()

        self.time_map[key][timestamp] = value
        

    # Runtime Complexity: O(log n)
    # Space Complexity: O(n)
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
        
        # if bisect_right cannot find the timestamp, it'll return the index where
        # we should insert the target to maintain sorted order. If the target is less
        # than any existing timestamp, it'll return the index where that target will
        # have been inserted, which is conveniently the same position as if we had found
        # the target. So in either case we can just use "pos - 1" to return the correct value
        pos = self.time_map[key].bisect_right(timestamp)

        if pos == 0:
            return ""
        
        return self.time_map[key].peekitem(pos - 1)[1]


obj = TimeMap()
obj.set("foo", "bar", 1)
p1 = obj.get("foo", 1)
p2 = obj.get("foo", 3)
obj.set("foo", "bar2", 4)
p3 = obj.get("foo", 4)
p4 = obj.get("foo", 5)