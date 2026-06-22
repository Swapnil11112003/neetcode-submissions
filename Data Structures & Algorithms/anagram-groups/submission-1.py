class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ana_dict = {}
        
        for s in strs:
            key = str(sorted(s))
            if key not in ana_dict:
                ana_dict[key] = [s]
            else:
                ana_dict[key].append(s)

        list = []
        for key, value in ana_dict.items():
            list.append(value)

        return list

        