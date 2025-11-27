class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        p1 = p2 = 0
        m = len(text1)
        n = len(text2)
        output = 0
        while p1 < m and p2 < n:
            if text1[p1] == text2[p2]:
                output += 1
                p1 += 1
                p2 += 1
            else:
                p1 += 1
        return output

