class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for char in s:
            if char.isalnum():
                new_s += char

        j = len(new_s) - 1
        for i in range(len(new_s)):
            if new_s[i].casefold() == new_s[j].casefold():
                j = j - 1
                continue
            else:
                return False
        
        return True    
