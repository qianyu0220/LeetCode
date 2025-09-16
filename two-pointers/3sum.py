class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        output = []
        for i in range(n):
            right = n - 1
            k = i + 1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while k < right:
                total = nums[i] + nums[k] + nums[right]
                if total == 0:
                    output.append([nums[i], nums[k], nums[right]])
                    k += 1
                    while k < right and nums[k] == nums[k-1]:
                        k += 1
                elif total < 0:
                    k += 1
                else:
                    right -= 1
        return output