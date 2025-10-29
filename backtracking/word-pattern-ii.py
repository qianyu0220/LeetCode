class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        mapping = {}
        used = set()
        def backtrack(i, j):
            if i == len(pattern) and j == len(s):
                return True
            if i == len(pattern) or j == len(s):
                return False
            char = pattern[i]
            if char in mapping:
                word = mapping[char]
                if not s.startswith(word, j):
                    return False
                return backtrack(i+1, j + len(word))
            for k in range(j+1, len(s) + 1):
                word = s[j:k]
                if word in used:
                    continue

                mapping[char] = word
                used.add(word)

                if backtrack(i+1, k):
                    return True
                del mapping[char]
                used.remove(word)
            return False
        return backtrack(0, 0)










