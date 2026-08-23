class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ana_dict = {} 

        for s in strs:
            sorted_s = " ".join(sorted(s))

            if sorted_s in ana_dict:
                ana_dict[sorted_s].append(s)
            else:
                ana_dict[sorted_s] = [s]

        res = []

        for _, value in ana_dict.items():
            res.append(value)
        
        return res