class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        result = []
        for i in range(len(expression)):
            oper = expression[i]
            if oper == "+" or oper == "-" or oper == "*":
                sub1 = expression[:i]
                sub2 = expression[i+1:]
                s1 = self.diffWaysToCompute(sub1)
                s2 = self.diffWaysToCompute(sub2)
                for l in s1:
                    for r in s2:
                        if oper == "+":
                            result.append(int(l) + int(r))
                        elif oper == "-":
                            result.append(int(l) - int(r))
                        else:
                            result.append(int(l) * int(r))
        if not result:
            return [int(expression)]
        return result