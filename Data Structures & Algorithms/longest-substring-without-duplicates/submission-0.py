class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash = set()
        i = 0
        max_len = 0

        for j in range(len(s)):
            while s[j] in hash:
                hash.remove(s[i])
                i += 1

            hash.add(s[j])
            max_len = max(max_len, j - i + 1)

        return max_len

        

        