class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        cnt=0
        jls=[jewels[i] for i in range(len(jewels))]
        stn=[stones[i] for i in range(len(stones))]
        for i in stn:
            if i in jls:
                cnt+=1
        return cnt