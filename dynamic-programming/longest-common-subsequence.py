class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        p1 = p2 = 0
        m = len(text1)
        n = len(text2)
        output = 0
        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    output += 1
        return output
