class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []
        
        for i in range(len(tokens)):
            res.append(tokens[i])
            if tokens[i] == "+":
                res.pop()
                op1, op2 = int(res.pop()), int(res.pop())
                res.append(op1 + op2)
            if tokens[i] == "-":
                res.pop()
                op1, op2 = int(res.pop()), int(res.pop())
                res.append(op2 - op1)
            if tokens[i] == "*":
                res.pop()
                op1, op2 = int(res.pop()), int(res.pop())
                res.append(op1 * op2)
            if tokens[i] == "/":
                res.pop()
                op1, op2 = int(res.pop()), int(res.pop())
                res.append(op2 / op1)

        return int(res.pop())
