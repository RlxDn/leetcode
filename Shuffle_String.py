class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        k=0
        res=[None]*len(s)
        for i in indices:
            res[i]=s[k]
            k+=1
        return "".join(res)