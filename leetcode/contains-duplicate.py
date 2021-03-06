class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        myDict = {}
        
        for num in nums:
            if num in myDict:
                return True
            myDict[num] = 1
        return False