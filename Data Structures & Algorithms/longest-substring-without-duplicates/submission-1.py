class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        max_len = 0
        i = 0
        for j in range(len(s)):
            while s[j] in window:
                window.remove(s[i])
                i += 1

            window.add(s[j])
            max_len = max(max_len, j - i + 1)

        return max_len


        

        