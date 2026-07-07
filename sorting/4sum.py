class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        output = []
        nums.sort()
        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                x, y = j+1, n-1     
                while x < y:
                    total = nums[i] + nums[j] + nums[x] + nums[y]
                    if total == target:
                        output.append([nums[i], nums[j], nums[x], nums[y]])
                        x += 1
                        while x < y and nums[x] == nums[x-1]:
                            x += 1
                    elif total < target:
                        x += 1
                    else:
                        y -= 1
        return output

