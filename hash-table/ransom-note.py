class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        output = ""
        p1 = 0
        p2 = 0
        while p1 < len(ransomNote) and p2 < len(magazine):
            if ransomNote[p1] == magazine[p2]:
                output += ransomNote[p1]
                p1 += 1
                p2 += 1
            else:
                p2 += 1
        return output == ransomNote
