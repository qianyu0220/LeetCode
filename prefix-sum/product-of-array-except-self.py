class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        result = 1
        for i in range(len(nums)):
            result_left = 1
            result_right = 1
            for x in range(0, i):
                result_left *= nums[x]
            for y in range(i+1, len(nums)):
                result_right *= nums[y]
            result = result_left * result_right
            output.append(result)
        return output