class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        left = 0
        n = len(nums)
        output = []
        nums.sort()
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j, k = n - 1, i+1
            while k < j:
                total = nums[i] + nums[k] + nums[j]
                if total == 0:
                    output.append([nums[i], nums[k], nums[j]])
                    k += 1
                    while k < j and nums[k] == nums[k-1]:
                        k += 1
                elif total < 0:
                    k += 1
                else:
                    j -= 1
        return output
                