class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_s = ""
        for s in strs:
            encoded_s += str(len(s)) + "#" + s
        return encoded_s



    def decode(self, s: str) -> List[str]:
        decoded_s = []
        i = 0
        j = 0
        while i < len(s):
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            decoded_s.append(s[j + 1:j+length +1])
            i = j + length + 1
            j = i
            
            
        return decoded_s


