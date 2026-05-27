import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result=[]
        for i in nums:
            copy=nums.copy()
            copy.remove(i)
            result.append(math.prod(copy))
        return result
        