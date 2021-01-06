class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums)):
            cnt=0
            for j in range(len(nums)):
                if nums[j]<nums[i]:
                    cnt+=1
            res.append(cnt)
        return res