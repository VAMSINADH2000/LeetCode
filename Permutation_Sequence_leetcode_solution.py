from itertools import permutations 
#importing permutations
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
         #intializing list with n numbers
        lst = [i for i in range(1,n+1)]
        #Generating permutations
        m = list(permutations(lst))
        #returning kth sequence 
        return "".join([str(i) for i in list(m[k-1])])  
