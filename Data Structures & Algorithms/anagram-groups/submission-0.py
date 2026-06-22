class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = dict()
        for s in strs:
            key = str(sorted(s))
            if key not in anagramDict:
                anagramDict[key] = [s]
            else:
                anagramDict[key].append(s)

        anagramList = []
        for el in anagramDict.values():
            anagramList.append(el)

        return anagramList







