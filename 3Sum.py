class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if nums[i]>0: break #[7]
            if i>0 and nums[i]==nums[i-1]: continue
            low,high = i+1,len(nums)-1 
            while low < high:
                if nums[i]+nums[low]+nums[high]==0:
                    res.append([nums[i],nums[low],nums[high]])
                    while low<high and nums[low]==nums[low+1]:
                        low+=1
                    while low<high and nums[high]==nums[high-1]:
                        high-=1
                    low+=1
                    high-=1
                elif nums[i]+nums[low]+nums[high]<0:
                    low+=1
                else:
                    high-=1
        return res
