class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # tmp = ''
        # p1 = p2 = 0

        # while p1 < len(s) and p2 < len(t):
        #     if s[p1] == t[p2]:
        #         tmp += s[p1]
        #         p1 += 1
        #         p2 += 1
        #     else:
        #         p2 += 1
        # return tmp == s
        m = len(s)
        n = len(t)
        p = 0
        while p < m:
            for i in range(n):
                if t[i] == s[p]:
                    p += 1
            return p == m