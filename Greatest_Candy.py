class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res=[]
        maxcandy=max(candies)
        for i in range(len(candies)):
            if candies[i]+extraCandies<maxcandy:
                res.append(False)
            else:
                res.append(True)
        return res