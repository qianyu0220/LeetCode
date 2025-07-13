class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        current = 0
        start = 0
        n = len(gas)
        for i in range(n):
            current += gas[i] - cost[i]
            if current < 0:
                current = 0
                start = i + 1
        return start
