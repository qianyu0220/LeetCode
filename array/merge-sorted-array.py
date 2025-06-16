class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = 0
        p2 = 0
        output = []
        while p1 < m and p2 < n:
            if nums1[p1] <= nums2[p2]:
                output.append(nums1[p1])
                p1 += 1
            else:
                output.append(nums2[p2])
                p2 += 1
        while p1 < m:
            output.append(nums1[p1])
            p1 += 1
        while p2 < n:
            output.append(nums2[p2])
            p2 += 1

        for i in range(len(output)):
            nums1[i] = output[i]

        