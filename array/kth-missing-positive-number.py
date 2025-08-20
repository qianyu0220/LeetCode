class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)
        for i in range(n):
            if arr[i] - (i + 1) >= k:
                return k + i
        return k + n