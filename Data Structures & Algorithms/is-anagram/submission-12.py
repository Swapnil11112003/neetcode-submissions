class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        freq_dict1, freq_dict2 = {}, {}

        for item in s:
            if item in freq_dict1:
                freq_dict1[item] += 1
            else:
                freq_dict1[item] = 1

        for item in t:
            if item in freq_dict2:
                freq_dict2[item] += 1
            else:
                freq_dict2[item] = 1

        return freq_dict1 == freq_dict2


            
