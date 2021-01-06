class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res=[]
        buff=[nums[i] for i in range(n)]
        buff2=[nums[i] for i in range(n,2*n)]
        for i in range(2*n):
            if i%2==0:
                res.append(buff.pop(0))
            else:
                res.append(buff2.pop(0))
        return res