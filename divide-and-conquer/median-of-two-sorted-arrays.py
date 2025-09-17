class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        output = []
        for i in range(m):
            output.append(nums1[i])
        for j in range(n):
            output.append(nums2[j])
        output.sort()
        k = len(output)
        mid = (0 + k - 1) // 2
        if k % 2 == 0:
            result = (output[mid] + output[mid+1]) / 2
        elif k % 2 != 0:
            result = output[mid]
        return result