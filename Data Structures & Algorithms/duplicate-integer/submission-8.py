class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mapper={}
        return len(nums)!=len(set(nums))