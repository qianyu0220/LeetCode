class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        p_count = [0] * 26
        window = [0] * 26
        output = []
        for i in range(len(p)):
            p_count[ord(p[i]) - ord("a")] += 1
        for i in range(n):
            window[ord(s[i]) - ord("a")] += 1
            if i >= len(p):
                window[ord(s[i-len(p)]) - ord("a")] -= 1
            if window == p_count:
                output.append(i-len(p)+1)
        return output