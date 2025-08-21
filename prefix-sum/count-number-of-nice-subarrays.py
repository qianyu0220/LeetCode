class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.atmost(nums, k) - self.atmost(nums, k - 1)
    def atmost(self, nums, k):
        left = 0
        output = 0
        count_odd = 0
        for right, num in enumerate(nums):
            if num % 2 == 1:
                count_odd += 1
            while count_odd > k:
                if nums[left] % 2 == 1:
                    count_odd -= 1
                left += 1
            output += right - left + 1
        return output