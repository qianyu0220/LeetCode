# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        output = float("inf")
        for i in range(n):
            if isBadVersion(i):
                output = min(output, i)
            elif i+1 == n:
                return n
        return output
