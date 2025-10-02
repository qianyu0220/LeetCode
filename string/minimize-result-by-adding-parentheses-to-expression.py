class Solution:
    def minimizeResult(self, expression: str) -> str:
        n = len(expression)
        place = 0
        smallest = float("inf")
        output = ""
        for i in range(n):
            if expression[i] == "+":
                place = i
        for i in range(place):
            for j in range(place+1, n):
                left = int(expression[:i]) if i > 0 else 1
                mid1 = int(expression[i: place])
                mid2 = int(expression[place+1:j+1])
                right = int(expression[j+1:]) if j+1 < n else 1
                val = left * (mid1 + mid2) * right

                if val < smallest:
                    smallest = val
                    output = (expression[:i] + "(" + expression[i:j+1] + ")" + expression[j+1:])
        return output