class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        h = 0

        for i in range(n-1, -1, -1):
            if citations[i] > h:
                h += 1
        return h