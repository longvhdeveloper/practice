class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        myDict = {}
        
        for i in range(0, len(nums)):
            if nums[i] in myDict:
                dis = abs(myDict[nums[i]] - i)
                if dis <= k:
                    return True
            myDict[nums[i]] = i
        return False