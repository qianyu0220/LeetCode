class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        mins = min(strs)
        maxs = max(strs)
        output = ""
        for i in range(len(mins)):
            if mins[i] != maxs[i]:
                output = mins[0:i]
                return output

