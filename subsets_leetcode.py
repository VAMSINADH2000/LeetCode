from itertools import chain, combinations

class Solution(object):

    def subsets(self,nums):
        temp = list(nums)
        return chain.from_iterable(combinations(temp, i) for i in range(len(nums)+1))
  
