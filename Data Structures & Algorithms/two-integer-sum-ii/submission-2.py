class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums=sorted(list(set(numbers)))
        pop_count=0
        while len(nums)>0:
            for i in range(0,len(nums)-1):
                if nums[0]+nums[i+1]==target:
                    return ([pop_count+1,pop_count+i+2])
            nums.remove(nums[0])
            pop_count+=1