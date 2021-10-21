class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        curr_max = nums[0]
        
        for i in range(1, len(nums)):
            if curr_max < 0:
                curr_max = nums[i]
            else:
                curr_max += nums[i]
                
            ans = max(curr_max, ans)
        
        
        return ans