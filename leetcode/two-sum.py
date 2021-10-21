class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        
        myDict = {}
        
        n = len(nums)
        
        for i in range(0, n):
            if nums[i] in myDict:
                myDict[nums[i]].append(i)
            else:
                myDict[nums[i]] = [i]
        
        for i in range(0, n):
            other = target - nums[i]
            
            if other == nums[i]:
                if other in myDict and len(myDict[other]) > 1:
                    ans = [myDict[other][0], myDict[other][1]]
                    break
            else:
                if other in myDict:
                    ans = [i, myDict[other][0]]
                    break
        
        return ans