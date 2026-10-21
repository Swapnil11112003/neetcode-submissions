class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s = []
        res = 0

        for op in operations:
            if op == "+":
                a, b = s[-1], s[-2]
                s.append(a + b)
            elif op == "C":
                s.pop()
            elif op == "D":
                x = s[-1]
                s.append(x * 2)
            else:
                s.append(int(op))

        for elem in s:
            res += elem

        return res

            

            

        