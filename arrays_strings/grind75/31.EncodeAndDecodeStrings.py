from typing import List

# https://leetcode.com/problems/encode-and-decode-strings/
# Tags: non-ascii delimiter
# Time Complexity: O(n)
# Space Complexity: O(1)
# Time: Not timed
class Codec:
    def encode(self, strs: List[str]) -> str:
        return "π".join(strs)
        

    def decode(self, s: str) -> List[str]:
        return s.split("π")
    

    def encodeUsingEscaping(self, strs: List[str]) -> str:
        encoded_strs = []
        for str in strs:
            encoded_str = []
            for i in range(len(str)):
                encoded_str.append(str[i])
                if str[i] == "/":
                    encoded_str.append("/")

            encoded_strs.append("".join(encoded_str))
        return "/:".join(encoded_strs) + "/:"
        

    def decodeUsingEscaping(self, s: str) -> List[str]:
        decoded_strs = []
        decoded_str = []
        i = 0
        while i < len(s):
            if s[i] == '/':
                if s[i + 1] == '/':
                    decoded_str.append("/")
                    i += 2
                elif s[i + 1] == ':':
                    decoded_strs.append("".join(decoded_str))
                    decoded_str = []
                    i += 2
            else:
                decoded_str.append(s[i])
                i += 1
        return decoded_strs

        
        
codec = Codec()
codec.decode(codec.encode(["He/llo","Wo/:rld"]))