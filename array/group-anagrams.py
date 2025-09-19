class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # record = dict()

        # for word in strs:
        #     tmp = tuple(sorted(word))
        #     if tmp in record:
        #         record[tmp].append(word)
        #     else:
        #         record[tmp] = [word]
        # return [val for key, val in record.items()]
        visit = dict()
        for word in strs:
            tmp = tuple(sorted(word))
            if tmp in visit:
                visit[tmp].append(word)
            else:
                visit[tmp] = [word]
        return [val for _, val in visit.items()]
        