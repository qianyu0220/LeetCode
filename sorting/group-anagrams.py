class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        visit = dict()
        for word in strs:
            tmp = tuple(sorted(word))
            if tmp in visit:
                visit[tmp].append(word)
            else:
                visit[tmp] = [word]
        return [val for _, val in visit.items()]