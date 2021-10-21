class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        n = len(nums1)
        m = len(nums2)
        
        if n > m:
            for num in nums2:
                if num in nums1:
                    ans.append(num)
                    nums1.remove(num)
        else:
            for num in nums1:
                if num in nums2:
                    ans.append(num)
                    nums2.remove(num)
        return ans