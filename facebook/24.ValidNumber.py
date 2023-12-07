class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    # Time: 10:00
    def isNumber(self, s: str) -> bool:
        if "inf" in s.lower() or s == 'nan':
            return False

        try:
            float(s)
        except ValueError:
            return False
        return True