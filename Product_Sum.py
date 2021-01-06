import numpy
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        res=[int(i) for i in str(n)]
        return numpy.prod(res)-numpy.sum(res)