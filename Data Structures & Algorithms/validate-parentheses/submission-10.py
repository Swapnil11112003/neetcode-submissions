class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True

        if len(s) % 2 != 0:
            return False
        else:
            new_s = []
            for n in s:
                if (n == '('  or n =='{' or n == '['):
                    new_s.append(n)
                if (n == ')'  or n =='}' or n == ']'):
                    if len(new_s) == 0:
                        return False
                    popped = new_s.pop()
                    if (popped == '(' and n != ')' or (popped == '[' and n != ']') or (popped == '{' and n != '}')):
                        return False

                
            return len(new_s) == 0
