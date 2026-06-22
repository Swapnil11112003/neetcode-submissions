class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        eval_list = []
        res = 0
        for token in tokens:
                if token == "+":
                    op1, op2 = eval_list.pop(), eval_list.pop()
                    res = op1 + op2
                    eval_list.append(res)
                elif token == "-":
                    op1, op2 = eval_list.pop(), eval_list.pop()
                    res = op2 - op1
                    eval_list.append(res)
                elif token == "*":
                    op1, op2 = eval_list.pop(), eval_list.pop()
                    res = op1 * op2
                    eval_list.append(res)
                elif token == "/":
                    op1, op2 = eval_list.pop(), eval_list.pop()
                    res = int(float(op2) / op1)
                    eval_list.append(res)
                else: 
                    eval_list.append(int(token))

        return eval_list[0]




        