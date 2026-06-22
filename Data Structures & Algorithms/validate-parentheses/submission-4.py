class Solution:
    def isValid(self, s: str) -> bool:
        res = True
        stack = []

        for strs in s:
            if (strs == "(") or (strs == "{") or (strs == "["):
                stack.append(strs)

            else:
                if strs == ")" or strs == "}" or strs == "]":
                    if len(stack) == 0:
                        return False
                    else: 
                        popped = stack.pop()

                        if strs == ")" and popped != "(":
                            return False

                        if strs == "}" and popped != "{":
                            return False

                        if strs == "]" and popped != "[":
                            return False


        if len(stack) == 0:
            res = True
        else:
            res =  False

        return res

            