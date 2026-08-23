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
            if char not in dict1 or dict1[char] == 0:
                return False
            dict1[char] -= 1

        return True

        