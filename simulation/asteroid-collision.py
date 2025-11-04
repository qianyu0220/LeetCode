class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = []
        for a in asteroids:
            while result and a < 0 < result[-1]:
                if -a > result[-1]:
                    result.pop()
                    continue
                elif -a == result[-1]:
                    result.pop()
                break
            else:
                result.append(a)
        return result