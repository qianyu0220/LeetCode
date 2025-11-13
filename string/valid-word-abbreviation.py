class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        m = len(word)
        n = len(abbr)
        i = j = 1
        while i < m and j < n:
            if abbr[j].isalpha():
                if abbr[j] != word[i]:
                    return False
                else:
                    i += 1
                    j += 1
            else:
                if abbr[j] == "0":
                    return False
                num_str = ""
                while j < n and abbr[j].isdigit():
                    num_str += abbr[j]
                    j += 1
                i += int(num_str)
        return i == m and j == n


