class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        freq_dict = {}

        for item in s:
            if item in freq_dict:
                freq_dict[item] += 1
            else:
                freq_dict[item] = 1

        for item in t:
            if item in freq_dict:
                freq_dict[item] -= 1
            else:
                freq_dict[item] = 1

        for key, val in freq_dict.items():
            if freq_dict[key] != 0:
                return False

        return True


            
