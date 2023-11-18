from typing import List

# 
# Tags: 
# Time: started 10:50
class Codec:

    def encode(self, strs: List[str]) -> str:
        return "π".join(strs)
        

    def decode(self, s: str) -> List[str]:
        return s.split('π')

        
codec = Codec()
result = codec.decode(codec.encode(["V","Grz/"]))
result = codec.decode(codec.encode(["th/:is", "is", "a", "te/st"]))
print(result)