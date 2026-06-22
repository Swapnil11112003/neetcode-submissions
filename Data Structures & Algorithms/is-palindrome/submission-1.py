class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''.join(filter(str.isalnum, s)).lower()
        i = 0
        j = len(new_s) - 1
        while i < j:
            if new_s[i] != new_s[j]:
                return False
            i += 1
            j -= 1

        return True

        