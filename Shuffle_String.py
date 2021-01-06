class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        k=0
        res=[for i in range(len(s))]
        for i in indices:
            res[i]=s[k]
            k+=1
        return res