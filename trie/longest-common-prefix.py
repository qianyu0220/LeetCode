class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minx = min(strs)
        maxx = max(strs)
        for i in range(len(minx)):
            if minx[i] != maxx[i]:
                return minx[:i]
        return minx