class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        
        if m == 0:
            for i in range(0, n):
                nums1[i] = nums2[i]
        else:
            i = m
            for j in range(0, n):
                nums1[i] = nums2[j]
                i += 1
        
        nums1.sort()