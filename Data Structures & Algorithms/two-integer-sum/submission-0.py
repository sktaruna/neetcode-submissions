class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)-1):
            a=i+1
            while a<len(nums):
                if nums[i]+nums[a]==target:
                    return [i,a]
                else:
                    a+=1