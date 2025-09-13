class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p = 0
        q = 0
        output = []
        while p < m and q < n:
            if nums1[p] <= nums2[q]:
                output.append(nums1[p])
                p += 1
            else:
                output.append(nums2[q])
                q += 1
        while p < m:
            output.append(nums1[p])
            p += 1
        while q < n:
            output.append(nums2[q])
            q += 1
            
        for i in range(m + n):
            nums1[i] = output[i]
        return nums1
