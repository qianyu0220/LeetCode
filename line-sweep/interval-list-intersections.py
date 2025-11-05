class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # output = []
        # m = len(firstList)
        # n = len(secondList)
        # i = j = 0
        # while i < m and j < n:
        #     start = max(firstList[i][0], secondList[j][0])
        #     end = min(firstList[i][1], secondList[j][1])
        #     if start <= end:
        #         output.append([start, end])
        #     if firstList[i][1] < secondList[j][1]:
        #         i += 1
        #     else:
        #         j += 1
        # return output
        output = []
        m = len(firstList)
        n = len(secondList)
        i = j = 0
        while i < m and j < n:
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])
            if start <= end:
                output.append([start, end])
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        return output