class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minx = min(strs)
        maxs = max(strs)
        output = ""
        for i in range(len(minx)):
            if minx[i] != maxs[i]:
                return minx[:i]
        return minx
