class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        mins = min(strs)
        maxs = max(strs)
        for i in range(len(mins)):
            if mins[i] != maxs[i]:
                return mins[:i]
        return mins