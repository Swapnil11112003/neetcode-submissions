class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if t == "" or len(t) > len(s):
            return ""
        
        freq_dict = {}
        window = {}
        for elem in t:
            freq_dict[elem] = freq_dict.get(elem, 0) + 1

        need = len(freq_dict)
        have = 0
        resLen = float("inf")
        res = [-1, -1]
        
        left = 0
        for right in range(len(s)):
            window[s[right]] = 1 + window.get(s[right], 0)

            if s[right] in freq_dict and window[s[right]] == freq_dict[s[right]]:
                have += 1

            while have == need:
                if (right - left + 1) < resLen:
                    resLen = right - left + 1
                    res = [left, right]

                window[s[left]] -= 1
                if s[left] in freq_dict and window[s[left]] < freq_dict[s[left]]:
                    have -= 1
                
                left += 1

        left, right = res

        return s[left : right + 1]



