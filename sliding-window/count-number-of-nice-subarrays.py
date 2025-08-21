class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.atMost(nums, k) - self.atMost(nums, k-1)
    def atMost(self, nums, k):
        left = 0
        count = 0
        ans = 0
        for right, num in enumerate(nums):
            if num % 2 == 1:
                count += 1
            while count > k:
                if nums[left] % 2 == 1:
                    count -= 1
                left += 1
            ans += right - left + 1
        return ans