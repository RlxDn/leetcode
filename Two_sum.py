import sys
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res=[]
        for i in range(0, len(nums)):
            for j in range(1, len(nums)):
                if i!=j:
                    if nums[i]+nums[j]==target:
                        res.append(i)
                        res.append(j)
                        return res
                        sys.exit()