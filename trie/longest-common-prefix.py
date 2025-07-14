class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_strs = min(strs)
        max_strs = max(strs)
        for i in range(len(min_strs)):
            if min_strs[i] != max_strs[i]:
                return min_strs[:i]
