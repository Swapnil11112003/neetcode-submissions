class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dict1, dict2 = {}, {}

        for elem in s:
            if elem in dict1:
                dict1[elem] += 1
            else:
                dict1[elem] = 1

        for char in t:
            if char in dict2:
                dict2[char] += 1
            else:
                dict2[char] = 1

        return dict1 == dict2

        