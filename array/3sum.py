class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        output = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            k, j = i + 1, n-1
            while k<j:
                total = nums[i] + nums[k] + nums[j]
                if total > 0:
                    j -= 1
                elif total < 0:
                    k += 1
                else:
                    output.append([nums[i], nums[k], nums[j]])
                    k += 1
                    while k<j and nums[k] == nums[k-1]:
                        k += 1
        return output