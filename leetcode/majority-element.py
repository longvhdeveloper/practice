class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majorItem = 0
        maxCount = 0
        myDict = {}
        
        n = len(nums)
        
        for num in nums:
            if num in myDict:
                myDict[num] += 1
            else:
                myDict[num] = 1
            if myDict[num] > maxCount and myDict[num] >= n//2:
                majorItem = num
                maxCount = myDict[num]
        return majorItem
                